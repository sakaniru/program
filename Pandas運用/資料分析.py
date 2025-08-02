import pandas as pd

# data=pd.Series([200,40,100])#只有欄

# print("開頭",data.max())
# print(int(data.median()))
# data*=2
# print(data)

# data=data==80# 放大後會變80
# print(data)

# data=pd.DataFrame({             #可建立欄列
#      "name" :["阿志","阿包","阿羽"],
#      "SSSS" :["100","200","300"]
# })
# data["SSSS"]=data["SSSS"].astype(int)
# print(data["SSSS"].median())

data = {
    '姓名': ['小明', '小華'],
    '年齡': [25, 30],
    '城市': ['台北', '高雄']
}

df = pd.DataFrame(data)

# 顯示讀取的資料
print("讀取的資料：")
print(df)
# 顯示資料的統計資訊
print("資料統計資訊：")
print(df.describe())   




