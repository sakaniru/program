
def c(g):
    def b():

        k=0
        for i in range(51):
            k+=i
        g(k)
    return b
@c
def show(k):
    print(k)

@c
def show2(G):
    print("result is",G)
show()
show2()



# def deco(ccc):
#     def gay():
#         print("裝飾器")
#         ccc(3)
#     return gay
# @deco

# def test(b):
#     print("普通函式",b)

# test()