import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import random
import asyncio
import json
from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# 1. 讀取環境變數
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# 2. 設定權限與 Bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=["!", "！"], intents=intents)
scheduler = AsyncIOScheduler()

# 設定檔案名稱 (強制使用絕對路徑)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REMINDER_FILE = os.path.join(BASE_DIR, "reminders.json")
recent_mentions = {}

# --- 讀寫檔案的輔助函式 ---
def load_reminders():
    if not os.path.exists(REMINDER_FILE):
        return []
    try:
        with open(REMINDER_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_reminders(data):
    with open(REMINDER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# --- 事件區 ---

@bot.event
async def on_ready():
    await asyncio.sleep(1)
    print(f"✅ 已登入為 {bot.user}")
    print("目前載入的指令：", [c.name for c in bot.commands])

    # 1. 啟動 APScheduler (每日固定任務)
    if not scheduler.running:
        scheduler.start()
        print("🕒 APScheduler 排程器已啟動")
        
        user_ids_str = os.getenv("DISCORD_風流")
        channel_id_str = os.getenv("DISCORD_頻道")
        
        if user_ids_str and channel_id_str:
            async def tag_users():  
                channel = bot.get_channel(int(channel_id_str))
                if channel:
                    user = await bot.fetch_user(int(user_ids_str))
                    await channel.send(f"{user.mention} 讀書") 
                    print("✅ 已自動發送風流標註訊息")
                else:
                    print("❌ 找不到頻道")

            scheduler.add_job(tag_users, "cron", hour=22, minute=0)
            print("🗓️ 已設定自動在 每天 22:00:00 發送訊息")

    # 2. 啟動 !schedule 的檢查任務 (Discord Tasks)
    if not check_reminders_task.is_running():
        check_reminders_task.start()
        print("📅 !schedule 提醒檢查任務已啟動！")
        
        # 印出目前清單 (這裡用 f"{...}" 是因為你是 Python 3.13 所以沒問題)
        reminders = load_reminders()
        display_list = [f"{r['event']}的時間為{r['time']}" for r in reminders]
        print("目前的提醒清單：", display_list)


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    now = datetime.now()
    
    # --- 處理提及通知邏輯 ---
    me_id_str = os.getenv("DISCORD_風流")
    if me_id_str:
        me_id = int(me_id_str)
        me = await bot.fetch_user(me_id)

        if message.reference and message.reference.resolved:
            replied_msg = message.reference.resolved
            if replied_msg.author.id == me_id:
                guild_name = message.guild.name if message.guild else "私人對話"
                msg_content = message.content.strip() if message.content else "(無文字內容)"
                jump_link = replied_msg.jump_url
                
                notify_msg = (
                    f"時間：{now.strftime('%Y-%m-%d %H:%M:%S')}\n"
                    f"你在「{guild_name}」有一則被回覆的訊息\n"
                    f"**{message.author.display_name} 回覆：** {msg_content}\n"
                    f"**[點我跳轉訊息]({jump_link})**"
                )
                await me.send(notify_msg)
                await bot.process_commands(message)
                return 

        if any(user.id == me_id for user in message.mentions):
            guild_name = message.guild.name if message.guild else "私人對話"
            channel_name = message.channel.name if hasattr(message.channel, "name") else "未知頻道"
            recent_mentions[message.author.id] = now
            await me.send(f"⚠️ {message.author.display_name} 在「{guild_name} / #{channel_name}」標註了你！")

        elif (message.author.id in recent_mentions and (now - recent_mentions[message.author.id]).seconds < 15):
            msg_content = message.content.strip() if message.content else "(無文字內容)"
            await me.send(f"💬 {message.author.display_name} 標註後續：{msg_content}")
            del recent_mentions[message.author.id]

    msg = message.content.strip()
    if msg in ["早","!早","早安","!早安","！早安","！早"]:
        await message.channel.send(f"{message.author.mention} 早安啦")
        return
    if msg in ["午安","!午安","！午安"]:
        await message.channel.send(f"{message.author.mention} 午安啦")
        return
    if msg in ["晚安","!晚安","！晚安"]:
        await message.channel.send(f"{message.author.mention} 晚安啦")
        return

    await bot.process_commands(message)

# --- 指令區 (Hello, 吃, AV 等省略，直接放在這裡) ---
# ... (這裡保留你原本的 hello, 吃, 喝, AV 等指令) ...
# 為了版面整潔，我這裡先省略中間那些娛樂指令，記得保留原本的喔！

@bot.command()
async def hello(ctx):
    await ctx.send("你爹來了，我是風流GG人")

@bot.command(aliases=["!av","！av","！AV"])
async def AV(ctx):
    names_env = os.getenv("AV_GIRLS")
    if names_env:
        names = names_env.split(",")
        pick = random.choice(list(set(names)))
        await ctx.send(f" 今天用 —— **{pick}**")
    else:
        await ctx.send("❌ .env 中未設定 AV_GIRLS")

# --- Schedule 相關指令與任務 ---

@bot.command()
async def 安排(ctx, *, args: str):
    """
    格式: !安排 <事件內容> <MM/DD> <HH:MM>
    範例: !安排 提交報告 12/20 14:00 (可附圖片)
    """
    parts = args.split()
    
    if len(parts) < 3:
        await ctx.send("❌ 格式錯誤！請依照格式：`!安排 事件內容 MM/DD HH:MM`\n範例：`!安排 聖誕節派對 12/25 18:30`")
        return

    time_str = parts[-1]   
    date_str = parts[-2]   
    event_name = " ".join(parts[:-2]) 

    try:
        now = datetime.now()
        current_year = now.year

        target_datetime_str = f"{current_year}/{date_str} {time_str}"
        target_time = datetime.strptime(target_datetime_str, "%Y/%m/%d %H:%M")

        if target_time < now:
            target_time = target_time.replace(year=current_year + 1)

        # 🔥 修正重點：在這裡加入圖片檢查
        attachment_url = ""
        if ctx.message.attachments:
            attachment_url = ctx.message.attachments[0].url

        new_reminder = {
            "user_id": ctx.author.id,
            "channel_id": ctx.channel.id,
            "event": event_name,
            "time": target_time.strftime("%Y-%m-%d %H:%M"),
            "created_at": now.strftime("%Y-%m-%d %H:%M:%S"),
            "image": attachment_url # 🔥 存入圖片網址
        }

        reminders = load_reminders()
        reminders.append(new_reminder)
        save_reminders(reminders)

        reply_msg = f"✅ 已儲存提醒！\n📅 事件：**{event_name}**\n⏰ 時間：`{new_reminder['time']}`"
        if attachment_url:
            reply_msg += f"\n📎 包含附件：{attachment_url}"
        await ctx.send(reply_msg)

    except ValueError:
        await ctx.send("❌ 時間或日期格式錯誤！\n日期請用 `MM/DD` (如 02/14)\n時間請用 `HH:MM` (如 13:30)")

# 🔥 修正重點：拿掉 self，因為這不是在 class 裡面
@tasks.loop(seconds=60)
async def check_reminders_task():
    reminders = load_reminders()
    if not reminders:
        return

    now = datetime.now()
    updated_reminders = []
    
    for r in reminders:
        reminder_time = datetime.strptime(r["time"], "%Y-%m-%d %H:%M")
        
        if now >= reminder_time:
            # 🔥 修正重點：單一檔案直接用 bot，不能用 self.bot
            channel = bot.get_channel(r["channel_id"])
            if channel:
                try:
                    user_mention = f"<@{r['user_id']}>"
                    msg_content = f"🔔 {user_mention} 時間到了！\n提醒事項：**{r['event']}**"
                    
                    # 🔥 讀取圖片邏輯
                    image_url = r.get("image")
                    if image_url:
                        msg_content += f"\n{image_url}"

                    await channel.send(msg_content)
                except Exception as e:
                    print(f"發送提醒失敗: {e}")
        else:
            updated_reminders.append(r)

    if len(reminders) != len(updated_reminders):
        save_reminders(updated_reminders)

# --- 啟動 Bot ---
if __name__ == "__main__":
    bot.run(TOKEN)