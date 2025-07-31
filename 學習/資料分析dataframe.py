import pandas as pd

data=pd.DataFrame({
    "name":["Amy","Bob","charlees"],
    "salary":[30000,50000,40000]
},   index=["A","B","C"])
# print(data)
# print("==============")
# print("資料數列",data.size)
# print("資料形狀(列,欄)",data.shape)
# print("資料索引",data.index)
# print("取得第二列",data.iloc[1],sep="\n")
# print("======================")
# print("取得第c列",data.loc["C"],sep="\n")
# print("取得name欄位(直向)",data["name"],sep="\n")
# names=data["name"]
# print("把name全部轉成大寫",names.str.upper(),sep="\n")
# salaries=data["salary"]
# print("薪水平均值",salaries.mean())
# 建立新蘭為
data["revenue"]=[500000,400000,300000]#data[新欄位的名稱]=列表
data["RANK"]=pd.Series([1,3,5],index=["A","B","C"])
data["cp"]=data["revenue"]/data["salary"]
print(data)