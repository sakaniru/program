# https://bit.ly/2UMcbDI
import pandas as pd
#讀取資料
data=pd.read_csv("googleplaystore.csv")#把副檔名格式的檔案讀取成一個datafram
#觀察資料
    # print("資料數量",data.shape)
    # print("資料欄位",data.columns)
    # print("==============================")
    # #分析資料:評分的各種統計數據
    # gay=data["Rating"]<=5
    # data=data[gay]
    # print("平均數",data["Rating"].mean())
    # print("中位數",data["Rating"].median())
    # print("取得前一百個APP的平均",data["Rating"].nlargest(100).mean())
#分析資料:安裝數量的各種統計數據
# data["Installs"]=data["Installs"].replace("Free","")
# data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","",regex=True))
# print("平均數",data["Installs"].mean())
# con=data["Installs"]>100000
# print("安裝數量大於100000的應用程式有幾個",data[con].shape[0])

#基於資料的運用:關鍵字搜尋應用程式名稱
# keyword=input("請輸入一個關鍵字:")
# con=data["App"].str.contains(keyword,case=False)

# print("包含關鍵字的應用程式數量",data[con].shape[0])