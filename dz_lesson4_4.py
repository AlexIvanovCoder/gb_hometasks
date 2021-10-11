# 4
list_of_numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
filtered_list_of_numbers = []

[filtered_list_of_numbers.append(i) for i in list_of_numbers if i not in filtered_list_of_numbers]

print(filtered_list_of_numbers)