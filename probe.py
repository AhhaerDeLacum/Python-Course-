#Числа фибоначи*
def Fibonacci(f1):
    f2 = 1
    print(f1)
    while f2 < 1000:
        print(f2)
        f1, f2 = f2, f1 + f2

Fibonacci(1)

# f1, f2 = 1, 1
#     print(f1)
#     while f2 < 1000:
#         print(f2)
#         f1, f2 = f2, f1+f2