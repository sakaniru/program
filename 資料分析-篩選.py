import pandas as pd

# data=pd.Series([30,15,20])
# condition=[True,False,True]
# condition=data>=18
# filteredData=data[condition]
# print(filteredData)

# data=pd.Series(["你好","Python","Pandas"])
# con=data.str.contains("P")
# print(con)
# fileter=data[con]
# print(fileter)

data=pd.DataFrame({
    "name":["Amy","Bob","charles"],
    "salary":[30000,50000,40000]
})
print("===================")
bal=data["name"]=="Amy"
print(bal)
kay=data[bal]
print(kay)

