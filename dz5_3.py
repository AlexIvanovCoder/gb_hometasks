from statistics import mean

with open(r"C:\Users\Dell 7720\Documents\gb\python\lesson5\text_3.txt", 'r', encoding='utf-8') as f:
    content = [i.split(" ") for i in f.read().splitlines()]
    print(f"Сотрудники с з-п меньше 20т.р.: {[i[0]for i in content if float(i[1]) < 20000]}")
print(f"средняя зарплата сотрудника: {mean([float(item[1]) for item in content])}")