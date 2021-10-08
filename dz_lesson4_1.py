from sys import argv


def salary_calc(hours, price, bonus):
    salary = (hours * price) + bonus
    print(f'salary = {salary}')
    return salary


hours, price, bonus = [int(i) for i in argv[1:]]
salary_calc(hours, price, bonus)

# проверка: python "C:/Users/User/PycharmProjects/pythonProject/lesson2.py" 10 2 3 
