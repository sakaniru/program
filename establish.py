# #實體物件運用

# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
# p1=point(3,4)
# print(p1.x,p1.y)
# p2=point(5,6)
# print(p2.x,p2.y)


# class Fullname:
#     def __init__(self,first,last):
#         self.first=first
#         self.last=last
# name1=Fullname("nima","sl")
# print(name1.first,name1.last)
# name2=Fullname("G","AY")
# print(name2.first,name2.last)



class fullname:
    def __init__(self,first,last):
        self.first=first
        self.last=last

first1=input("請輸入第一位的姓氏:")
last1= input("請輸入第一位的名字:")
name1=fullname(first1,last1)
print("第一位全名:", name1.first + name1.last)

first2=input("請輸入第二位的姓氏:")
last2= input("請輸入第二位的名字:")

name2=fullname(first2,last2)
print("第二位全名:", name2.first + name2.last)

