# 2
list_of_numbers = [1, 2, 15, 4, 5, 1, 20, 3, 5]
print([list_of_numbers[i + 1] for i in range(len(list_of_numbers) - 1) if list_of_numbers[i + 1] > list_of_numbers[i]])