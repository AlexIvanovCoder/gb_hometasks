# 5

def sum_of_numbers():
    sum_of_numbers = 0
    while 1 == 1:
        string_of_numbers = input(f'Введите числа разделенные пробелом: ').split(" ")
        for i in string_of_numbers:        
            try:
                sum_of_numbers += int(i)
            except ValueError:
                print('Суммирование остановлено пользователем')
                return sum_of_numbers
        print(sum_of_numbers)    

print(sum_of_numbers())



