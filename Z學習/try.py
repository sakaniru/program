# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     #定義實體方法
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,tx,ty):
#         return((self.x-tx)**2+(self.y-ty)**2)**0.5
# p=point(3,4)
# p.show()#呼叫實體方法
# result=p.distance(0,0)#計算座標3,4到0,0之間的距離  因有return回傳  要設result
# print(result)

#實體物件的設計
class File:
    def __init__(self,name):
        self.name=name
        self.file=None#尚未開啟檔案  預設為none
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()
#讀取第一個檔案
f0=File("data.txt")
f0.open()
data=f0.read()
print(data)
f1=File("data1.txt")
f1.open()
data=f1.read()
print(data)
f2=File("data2.txt")
f2.open()
data=f2.read()
print(data)