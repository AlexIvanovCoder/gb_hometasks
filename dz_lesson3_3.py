# 3
def my_func(a, b, c):
    sorted_list = sorted([a, b, c])
    first_num = sorted_list[-1]
    second_num = sorted_list[-2]
    return first_num + second_num

print(my_func(5, 2, 9))

