n1=int(input("請輸入數字一:"))
n2=int(input("請輸入數字二:"))
n3=input("請輸入運算式:,+,-,*,/")
if   n3=="+":
    print(n1+n2)
elif n3=="-":
    print(n1-n2)
elif n3=="*":
    print(n1*n2)
elif n3=="/":
    print(n1/n2)
else: 
    print("請輸入正確的算式")