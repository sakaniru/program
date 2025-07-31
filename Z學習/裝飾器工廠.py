def factory(max):
    def cal(call):
        def run():
            a=0
            for i in range(max+1):
                a+=i
            call(a)
        return run
    return cal



@factory(100)
def show(g):
    print("結果是",g)

show()
@factory(10)
def show2(g):
    print("Result is",g)
show2()









# def fac(n1): 
#     def a(base):
#         def de():
#             print("裝飾器內部",n1)
#             res=n1*2
#             base(res)
#         return de
#     return a
# @fac(5)
# def gay(res):
#    print("普通函式",res)

# gay()