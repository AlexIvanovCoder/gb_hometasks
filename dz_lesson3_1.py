# 1
def division_of_numbers():
    a = int(input(f'Введите делимое: '))
    b = int(input(f'Введите делитель: '))
    
    try:
        c = a / b
    except ZeroDivisionError:
        c = "На ноль делить нельзя"
    return c

print(division_of_numbers())

