# 1
variable1 = "string"
variable2 = 2
print(variable1, variable2)
variable1 = input("Input string: ")
variable2 = input("Input number: ")
print(variable1, variable2)

#2
seconds = int(input("Input seconds: "))
sec_per_minute = 60
sec_per_hour = 60 * sec_per_minute

hours = seconds // sec_per_hour
seconds_left_after_hours = seconds % sec_per_hour
minutes = seconds_left_after_hours // sec_per_minute
seconds_left_after_minutes = seconds_left_after_hours % sec_per_minute

print(f'{hours}:{minutes}:{seconds_left_after_minutes}')

#3
num = input("input number: ")
single_num = int(num)
double_num = int(num * 2)
triple_num = int(num * 3)

print(single_num + double_num + triple_num)

#4
num = int(input("input number: "))

max_num_container = 0

while num != 0: #знаков в цифре не осталось
    last_number = num % 10 #берем посл. цифру
    if last_number > max_num_container: #если больше того, что уже хранится, то заменяем на большую
        max_num_container = last_number

    num //= 10 #отбрасываем посл. цифру

print(max_num_container)

#5

revenue = int(input("Input revenue: ")) #выручка
loss = int(input("Input loss: ")) #издержки
profit = revenue - loss #прибыль

company_result = ""
if revenue > loss:
    company_result = "profit"
    profitability = profit / revenue #не написано в задании выводить рентабельность, поэтому не вывожу
elif revenue < loss:
    company_result = "loss"
else: #сработала в 0. Этого не было в задании. По-стогому, надо исключить это условие
    company_result = "breakeven"

print(f'Company result: {company_result}')

############численность#############
headcount = int(input("Input headcount: ")) #численность
profit_per_head = profit / headcount #прибыль на одного сотрудника. В задании не было написано, напечатать, поэтому не печатал.


#6
a = int(input("Input first_day_result: "))
b = int(input("Input desirable_result: "))

days_count = 1

while a < b:
    a *= 1.1
    days_count += 1

print(f'days_count: {days_count}')