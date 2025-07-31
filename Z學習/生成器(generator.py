# def test():
#     yield 3
#     yield 5
#     yield 5
# gen=test()
# for i in gen:
#     print(i)

def generateEven(max):
    number=0
    while number<=max:
        yield number
        number+=2
    

key=generateEven(10)
for i in key:
    print(i)