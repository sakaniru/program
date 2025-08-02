import pandas as pd
data=pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
# print(data)
# print("資料型態",data.dtype)
# print("資料數量",data.size)
# print("資料索引",data.index)
# print(data[2],data[0])
# print(data["c"])
# print("最大值=",data.max())
# print("最小值=",data.min())
# print("標準差=",data.std())
# print("中位數=",data.median())
# print("最大的前N個數字\n",data.nlargest(3))
# print("最小的前N個數字\n",data.nsmallest(3))
# data=pd.Series(["您好","Python","pandas"])
# print(data.str.lower())#變小寫
# print(data.str.upper())#變大寫
# print(data.str.len())#取長度
# print(data.str.cat(sep=","))#把字串接起來
# print(data.str.replace("您","你"))#取代A變成B
# print(data.str.contains("P"))#判斷字串中有沒有A