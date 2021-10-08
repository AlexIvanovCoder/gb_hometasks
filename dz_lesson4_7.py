# 7

def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        yield (f)


for el in fact(4):
    print(el)
