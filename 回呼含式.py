def add  (n1,n2,cb):
    cb(n1+n2)

def handle1(b):
    print("結果是",b)

# def handle2(c):
#     print("Result of Add is",c)

add(3,4,handle1)
add(5,6,handle1)
# add(4,2,handle2)








# def test(arg):
#     arg("hello")

# #回呼
# def handle(da):
#     print(da)

# test(handle)