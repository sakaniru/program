import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
import asyncio
import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from flask import ctx


# 讀取 .env 檔案
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
#print(f"目前讀到的TOKEN是：{TOKEN}")


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=["!","！"], intents=intents)# 
scheduler = AsyncIOScheduler()  # 🔥 建立排程器實例

@bot.event
async def on_ready():
    await asyncio.sleep(1)
    print("目前載入的指令：", [c.name for c in bot.commands])
    print(f"✅ 已登入為 {bot.user}")
    # scheduler.start()
    # print("🕒 排程器已啟動")
    # target_time = datetime.datetime(2025, 10, 26, 17, 50, 0)#時間格式 00:00:00

    # user_ids = [int(os.getenv(f"DISCORD_風流")), int(os.getenv(f"DISCORD_米哭")), int(os.getenv(f"DISCORD_毛毛"))]
    # channel_id = int(os.getenv("DISCORD_頻道"))
    # async def tag_users():  
    #     channel = bot.get_channel(channel_id)
    #     if channel is None:
    #         print("❌ 找不到頻道，請確認頻道ID是否正確")
    #         return

    #     mentions = []
    #     for uid in user_ids:
    #         user = await bot.fetch_user(uid)
    #         mentions.append(user.mention)

    #     mention_text = " ".join(mentions)
    #     await channel.send(f"{mention_text} 星塔旅人 啟動！\nhttps://www.youtube.com/live/GeYczC8v1EM")
    #     print("✅ 已自動發送風流標註訊息")
    # scheduler.add_job(tag_users, "date", run_date=target_time)
    # print("🗓️ 已設定自動在 2025/10/26 17:50:00 發送訊息")

# @bot.command()
# async def hello(ctx):
#     await ctx.send("你爹來了，我是風流GG人")

@bot.command()
async def 吃(ctx):
    foods = [
        "麥當勞","KFC","漢堡王","摩斯漢堡","SUBWAY","必勝客","達美樂","吃屎",
        "牛排","火鍋","燒烤","壽司","拉麵","炒飯","炒麵","便當","炸雞",
        "鹽酥雞","滷味","關東煮","炸物","牛肉麵","牛排蓋飯","雞排飯","排骨飯",
        "炸醬麵","涼麵","牛肉捲餅","蔥油餅","肉圓","蚵仔煎","米粉湯","粥",

    ]
    choice = random.choice(foods)
    await ctx.send(f"{ctx.author.mention}\n{choice}")

@bot.command()
async def 喝(ctx):
    foods = [
        "豆漿", "奶茶", "紅茶拿鐵", "抹茶拿鐵",
        "仙草奶凍", "芋泥球", "珍奶鬆餅", "雞蛋布丁", "奶酪", "焦糖布丁",
        "黑糖珍珠鮮奶", "抹茶紅豆冰", "楊枝甘露", "愛玉檸檬", "百香果綠茶",
        "水果茶", "蜂蜜綠茶", "冬瓜檸檬", "梅子綠", "蘋果紅茶", "凍檸茶",
        # 👇 甜點 / 飲品
        "珍奶",  "綠茶", "紅茶", "烏龍茶", "奶蓋紅茶",
        "芒果冰", "草莓冰", "鳳梨冰", "黑糖刨冰", "綜合水果冰", "豆漿紅茶",
        "西米露", "仙草奶凍", "愛玉冰", "抹茶冰淇淋", "紅豆冰沙",
        "綠豆冰沙", "奶茶冰沙", "巧克力冰沙", "香蕉牛奶", "木瓜牛奶",
        "甘蔗汁", "青草茶", "冬瓜檸檬茶", "仙草冰茶",
    ]
    choice = random.choice(foods)
    await ctx.send(f"{ctx.author.mention}\n{choice}")
    

@bot.command()
async def 主詞(ctx):
    await ctx.send("講話他媽的說主詞")
@bot.command()
async def 睡覺(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1425974624604389378/1431523428619386961/images.jpg?ex=68fdb995&is=68fc6815&hm=62970a640e9d8e5306ed9982c928b844a71923cd05a34fdcfba46a1c2ae211a4&")

@bot.command()
async def 動腦(ctx):
    await ctx.send("幹你他媽的動點腦")

    

@bot.command(name="風流")
async def 風流(ctx):
    user_id = int(os.getenv("DISCORD_風流"))  # 風流本人 ID
    user = await bot.fetch_user(user_id)

    gif_urls = [
        "https://cdn.discordapp.com/attachments/1191594326631907360/1429732184968921319/efba38525f5e1c73.jfif?ex=68f7355c&is=68f5e3dc&hm=df0e4c95d6de4389a88b0ec7ea23e1b5ea28666a98db18490797e8dbe9e8cb40&",
        "https://cdn.discordapp.com/attachments/1191594326631907360/1429732184717135934/images.jfif?ex=68f7355b&is=68f5e3db&hm=62cd44ed00723d0ff1d1de369c58731244c62986221976d1419f49e8f5308d2f&",
        "https://cdn.discordapp.com/attachments/1191594326631907360/1429732184482123786/1.jfif?ex=68f7355b&is=68f5e3db&hm=ab607fa7b7a9cd7b78e1fd4da0d79889b9f149c2086ce7c41efdc14e29584f0e&",
        "https://cdn.discordapp.com/attachments/1191594326631907360/1429732184205557860/2.jfif?ex=68f7355b&is=68f5e3db&hm=6763a318ce041d69ac57c5abd4dd161e098e2b47fa0e9960ed10afd596c91add&",
    ]

    gif_choice = random.choice(gif_urls)

    # 回覆訊息
    await ctx.send(f"{ctx.author.mention} 標你媽呢標，沒被扁過是不是？")
    await ctx.send(gif_choice)


recent_mentions = {}

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    me_id = int(os.getenv("DISCORD_風流"))
    me = await bot.fetch_user(me_id)

    now = datetime.datetime.now()

    #  情況1：有人標註你
    if any(user.id == me_id for user in message.mentions):
        guild_name = message.guild.name if message.guild else "私人對話"
        channel_name = message.channel.name if hasattr(message.channel, "name") else "未知頻道"
        recent_mentions[message.author.id] = now  # 記錄這個人剛標註過你

        await me.send(
            f"⚠️ {message.author.display_name} 在伺服器「{guild_name}」的頻道「#{channel_name}」標註了你！"
        )

    #  情況2：剛剛標註過你，又發文字
    elif (
        message.author.id in recent_mentions
        and (now - recent_mentions[message.author.id]).seconds < 15  # 15秒內視為延續訊息
    ):
        msg_content = message.content.strip() if message.content else "(無文字內容)"
        attachments = "\n".join(a.url for a in message.attachments) if message.attachments else ""

        notify_msg = f"💬 {message.author.display_name} 標註你說：{msg_content}"
        if attachments:
            notify_msg += f"\n📎 附件：\n{attachments}"

        await me.send(notify_msg)

        # 為避免誤觸，發完後移除紀錄
        del recent_mentions[message.author.id]

    if message.content.strip()in ["早","!早","早安","!早安","！早安","！早"]:
        ctx = await bot.get_context(message)
        await ctx.send(f"{ctx.author.mention}早安啦")
        return
    
    if message.content.strip()in ["午安","!午安","！午安"]:
        ctx = await bot.get_context(message)
        await ctx.send(f"{ctx.author.mention}午安啦")
        return
    
    if message.content.strip()in ["晚安","!晚安","！晚安"]:
        ctx = await bot.get_context(message)
        await ctx.send(f"{ctx.author.mention}晚安啦")
        return

    await bot.process_commands(message)
    
@bot.command(name="友人")
async def 友人(ctx):
    user_id = int(os.getenv("DISCORD_友人"))
    user = await bot.fetch_user(user_id)

    gif_urls = [
        "https://cdn.discordapp.com/attachments/1333519706455281737/1429456055397650552/-_full_1.gif?ex=68f63431&is=68f4e2b1&hm=53a5d179db702d180249291cc14959a444ae9c8fdc33baa59f3cbbb9e136ab70&",
        "https://cdn.discordapp.com/attachments/1333519706455281737/1429456055842111672/-_full.gif?ex=68f63431&is=68f4e2b1&hm=f4a88e1b2cdd281c93ca58536a8f0be892a92d34151c67bd717c6af628d23436&",
        "https://cdn.discordapp.com/attachments/1333519706455281737/1429456056198893608/Adobe_Express_-_full_3.gif?ex=68f63431&is=68f4e2b1&hm=a03c8e0f4faeb608a53ea8b13d74c1deb8c680c31155a9acfcc331f1bddb2c7b&"
    ]

    gif_choice = random.choice(gif_urls)
    await ctx.send(f"{user.mention}")
    await ctx.send(gif_choice)

# 程式進入點：只在直接執行時啟動
# -------------------------------
if __name__ == "__main__":
    bot.run(TOKEN)