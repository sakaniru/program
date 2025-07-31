import json
with open("ASD.json",mode="r",encoding="utf-8")as file:
    data=json.load(file)
print("原本的",data["name"],data["vision"])
data["name"]=int(input("請輸入第一個數字"))
data["vision"]=int(input("請輸入第二個數字"))


with open("ASD.json",mode="w",encoding="utf-8")as file:
    json.dump(data,file,ensure_ascii=False)
print("第一個數字更換為",data["name"])
print("第二個數字更換為",data["vision"])

k=data
n3=input("請輸入運算式:,+,-,*,/\n")
if   n3=="+":
    print("相加為",data["name"]+data["vision"])
elif n3=="-":
   print("相減為",data["name"]-data["vision"])
elif n3=="*":
    print("相乘為",data["name"]*data["vision"])
elif n3=="/":
    print("相除為",data["name"]/data["vision"])
else: 
    print("請輸入正確的算式")