# 5
from functools import reduce

list_of_numbers = [i for i in range(100, 1000 + 1, 2)]


def mult(i, j):
    return i * j


print(reduce(mult, list_of_numbers))