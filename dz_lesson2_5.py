# 5
my_list = [7, 5, 3, 3, 2]
my_list = sorted(my_list, reverse=True) # на случай ввода другого списка
elt_to_list = int(input("input element: "))

for i in range(len(my_list)):
    if elt_to_list > my_list[i]:
        my_list.insert(i, elt_to_list)
        break
print(f'element {elt_to_list} inserted at index: {i}')
print(my_list)