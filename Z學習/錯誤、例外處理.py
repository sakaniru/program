#使用者如果輸入的格式不能轉換成數字，重新輸入 直到輸入成功
while True:
    data=input("輸入數字:")
    try:                           #把可能轉換錯誤的格式包進try中
        number=int(data)
        break
    except Exception:
        print("請重新輸入數字")

number=number*2
print(number)