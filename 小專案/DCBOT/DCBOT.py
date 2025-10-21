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

bot = commands.Bot(command_prefix=["!","！"], intents=intents)
scheduler = AsyncIOScheduler()  # 🔥 建立排程器實例

@bot.event
async def on_ready():
    await asyncio.sleep(1)
    print("目前載入的指令：", [c.name for c in bot.commands])
    print(f"✅ 已登入為 {bot.user}")
    # scheduler.start()
    # print("🕒 排程器已啟動")
    # target_time = datetime.datetime(2025, 10, 20, 12, 0, 0)#時間格式 00:00:00

    # user_ids = [
    # #     311545120057196544,
    # #     311142287084093450,#風流
    # #     143737169545003008,
    # #     372319880222998528,
    # #     302767864165695488
    # # ]

    # # channel_id = 398100437342879745
    # # async def tag_users():  
    # #     channel = bot.get_channel(channel_id)
    # #     if channel is None:
    # #         print("❌ 找不到頻道，請確認頻道ID是否正確")
    # #         return

    # #     mentions = []
    # #     for uid in user_ids:
    # #         user = await bot.fetch_user(uid)
    # #         mentions.append(user.mention)

    # #     mention_text = " ".join(mentions)
    # #     await channel.send(f"{mention_text} 星塔旅人 啟動！\nhttps://stellasora.jp/")
    # #     print("✅ 已自動發送風流標註訊息")
    # # scheduler.add_job(tag_users, "date", run_date=target_time)
    # # print("🗓️ 已設定自動在 2025/10/20 12:00:00 發送訊息")

@bot.command()
async def hello(ctx):
    await ctx.send("你爹來了，我是風流GG人")

@bot.command()
async def 吃(ctx):
    foods = [
        "滷肉飯", "雞排", "鹽酥雞", "香雞排", "雞蛋糕", "蚵仔煎", "蔥油餅",
        "肉圓", "炒米粉", "肉燥飯", "雞絲飯", "牛肉麵", "陽春麵", "擔仔麵",
        "乾麵", "米苔目", "滷味", "黑輪", "甜不辣", "鹹酥雞", "炸豆腐",
        "章魚燒", "燒烤", "碳烤雞排", "滷蛋", "貢丸湯", "魚丸湯", "肉羹湯",
        "排骨飯", "焢肉飯", "鴨肉飯", "雞腿飯", "排骨酥湯", "豬血湯",
        "豬血糕", "炸花枝丸", "魷魚羹", "刈包", "碗粿", "臭豆腐",
        "豆花", "紅豆湯", "綠豆湯", "燒仙草", "冰豆花", "仙草凍",
        "芋圓", "剉冰", "八寶冰", "珍珠奶茶", "冬瓜茶", "紅茶冰", "青草茶",
        "米血糕", "大腸包小腸", "甜不辣", "炸甜不辣", "炸魷魚", "香腸",
        "蚵仔麵線", "炒飯", "蛋炒飯", "蝦仁炒飯", "牛肉炒飯", "炒河粉",
        "鐵板麵", "鐵板牛排", "蛋包飯", "咖哩飯", "燴飯", "滷白菜", "紅燒豆腐",
        "炸醬麵", "麻醬麵", "湯包", "小籠包", "鍋貼", "水餃", "煎餃",
        "蔥抓餅", "韭菜盒", "蘿蔔糕", "蛋餅", "燒餅油條", "飯糰", "鹹豆漿",
        "油條", "肉鬆飯糰", "豆漿", "奶茶", "紅茶拿鐵", "抹茶拿鐵",
        "仙草奶凍", "芋泥球", "珍奶鬆餅", "雞蛋布丁", "奶酪", "焦糖布丁",
        "黑糖珍珠鮮奶", "抹茶紅豆冰", "楊枝甘露", "愛玉檸檬", "百香果綠茶",
        "水果茶", "蜂蜜綠茶", "冬瓜檸檬", "梅子綠", "蘋果紅茶", "凍檸茶",
        # 👇 夜市 & 特色餐點
        "地瓜球", "烤玉米", "臭豆腐", "炸臭豆腐", "鹹水雞", "滷味拼盤",
        "滷豆干", "鐵蛋", "蔥抓餅", "蚵仔湯", "花枝焿", "牛肉湯", "肉羹麵",
        "雞肉飯", "肉燥乾麵", "香菇貢丸湯", "味噌湯", "貢丸米粉", "炒年糕",
        "海鮮粥", "皮蛋瘦肉粥", "廣東粥", "蛋花湯", "紫菜湯", "海帶湯",
        # 👇 台式便當常見菜色
        "滷排骨", "炸雞腿", "香腸炒飯", "三杯雞", "宮保雞丁", "糖醋排骨",
        "蔥爆牛肉", "青椒牛柳", "魚香茄子", "蒜泥白肉", "紅燒獅子頭",
        "炸豆皮", "炒高麗菜", "炒青菜", "豆干炒肉絲", "炒空心菜",
        "炒豆芽", "滷豆腐", "滷海帶", "筍干", "滷花生", "滷蛋"
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
        "珍珠奶茶", "波霸奶茶", "綠茶", "紅茶", "烏龍茶", "奶蓋紅茶",
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
    

@bot.command(name="風流")
async def 風流(ctx):
    user_id =  311142287084093450 # ← 風流文雅(電視) 因為使用authon.mention <<是用來標註發送指令的使用者 有需要的時候再去discord複製ID 
    user = await bot.fetch_user(user_id) 
    
    gif_urls = ["https://cdn.discordapp.com/attachments/1191594326631907360/1429732184968921319/efba38525f5e1c73.jfif?ex=68f7355c&is=68f5e3dc&hm=df0e4c95d6de4389a88b0ec7ea23e1b5ea28666a98db18490797e8dbe9e8cb40&",
                "https://cdn.discordapp.com/attachments/1191594326631907360/1429732184717135934/images.jfif?ex=68f7355b&is=68f5e3db&hm=62cd44ed00723d0ff1d1de369c58731244c62986221976d1419f49e8f5308d2f&",
                "https://cdn.discordapp.com/attachments/1191594326631907360/1429732184482123786/1.jfif?ex=68f7355b&is=68f5e3db&hm=ab607fa7b7a9cd7b78e1fd4da0d79889b9f149c2086ce7c41efdc14e29584f0e&",
                "https://cdn.discordapp.com/attachments/1191594326631907360/1429732184205557860/2.jfif?ex=68f7355b&is=68f5e3db&hm=6763a318ce041d69ac57c5abd4dd161e098e2b47fa0e9960ed10afd596c91add&"
    ]
    gif_choice = random.choice(gif_urls)
    if ctx.author.id == user.id:
         await ctx.send(f"{ctx.author.mention} 標你媽呢標，沒被扁過是吧")

    else:
        await ctx.send(f"{ctx.author.mention} 標你媽呢標，沒被扁過是吧 {user.mention}")

    await ctx.send(gif_choice)
@bot.event
async def on_message(message):
    if message.author.bot:
        return  # 忽略其他 Bot 的訊息

    # 檢查是否為 "風流" 三種變化
    if message.content.strip() in ["風流", "!風流", "！風流"]:
        ctx = await bot.get_context(message)
        await 風流(ctx)  # ✅ 直接呼叫指令函式
        return

    await bot.process_commands(message)
    
@bot.command(name="友人")
async def 友人(ctx):
    user_id = 265480343027449858
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