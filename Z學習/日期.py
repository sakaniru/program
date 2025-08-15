
import datetime as dt
# 印出今天的日期
today=dt.date.today()
# nextweek=  today + dt.timedelta(days=28)
# print("今天的日期是:", today.strftime("%Y-%m-%d"))
# print("今天是", today.year, "年", today.month, "月", today.day, "日")
# print("-"*30)
# print("四週後的日期是:", nextweek.strftime("%Y-%m-%d"))
# print("四週後是", nextweek)
# print("四週後是", nextweek.year, "年", nextweek.month, "月", nextweek.day, "日")
#取得下個月第一天的日期
# next_month = today.replace(day=1) + dt.timedelta(days=32)
# next_month = next_month.replace(day=1)  # 確保是下個月的第一天

# #取得下個月最後一天的日期
# next_month_last_day = next_month + dt.timedelta(days=31)
# next_month_last_day = next_month_last_day.replace(day=1) - dt.timedelta(days=1)

# while next_month_last_day.month != next_month.month:
#     next_month_last_day -= dt.timedelta(days=1)



# print("下個月第一天的日期是:", next_month.strftime("%Y-%m-%d"))
# print("下個月最後一天的日期是:", next_month_last_day.strftime("%Y-%m-%d"))
# print("今天的日期是:", today.strftime("%Y-%m-%d"))
# print("今天是", today.year, "年", today.month, "月", today.day, "日")
# print("下個月第一天的日期是:", next_month.strftime("%Y-%m-%d"))

import datetime as dt

# 印出今天的日期
today = dt.date.today()

# 取得下個月第一天的日期
next_month = today.replace(day=1) + dt.timedelta(days=32)
next_month = next_month.replace(day=1)  # 確保是下個月的第一天

# 取得下個月最後一天的日期
next_month_last_day = next_month + dt.timedelta(days=31)
next_month_last_day = next_month_last_day.replace(day=1) - dt.timedelta(days=1)

# 用 while 來列出下個月的每一天
current_day = next_month
while current_day <= next_month_last_day:
    print(current_day.strftime("%Y-%m-%d"))
    current_day += dt.timedelta(days=1)

    
weekday_name={
    0: "星期一",
    1: "星期二",
    2: "星期三",
    3: "星期四",
    4: "星期五",
    5: "星期六",
    6: "星期日"
}


# today=dt.date.today()
# dtt=dt.date(today.year, today.month,1)
# while dtt.month == today.month:
#     weekday=dtt.weekday()
#     print(dtt, weekday_name[weekday])
#     if (dtt.weekday(), weekday_name[weekday]) == (6, "星期日"):
#         print("-"*30)
#     dtt += dt.timedelta(days=1)


        
# def print_today_date():
#     today = dt.date.today()
#     print("今天的日期是:", today)
# print_today_date()
# #印出今天的日期和時間 紀錄到秒
# def print_today_datetime():
#     now = dt.datetime.now()
#     print("現在的日期和時間是:", now.strftime("%Y-%m-%d %H:%M:%S"))
# print_today_datetime()

