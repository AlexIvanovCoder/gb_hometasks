# 2
elements_num = int(input("Input number of list elements: "))
lst = []
for i in range(0,elements_num):
    element = input("Input element for list: ")
    lst.append(element) 

print(f'Initial list {lst}')

final_lst = [] #список для значений со сменой мест

to_start = lst[1::2] #ставим в начало
to_end = lst[0::2] #ставим в конец

#меняем значения:
for i in range(0, len(lst) // 2): #берем только четное количество
    final_lst.append(to_start[i])
    final_lst.append(to_end[i])

#если количество нечетное, добавляем в конец последний элемент
if len(lst) % 2 == 1:
    final_lst.append(lst[-1])
    
print(final_lst)