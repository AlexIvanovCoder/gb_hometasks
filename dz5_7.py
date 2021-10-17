from statistics import mean
import json

# читаем из файла
with open(r"C:\Users\Dell 7720\Documents\gb\python\lesson5\text_7.txt", 'r', encoding='utf-8') as f:
    content = [i.split(" ") for i in f.read().splitlines()]

# считаем статистику
general_profit = []
company_list = {}

for i in content:
    company = i[0]
    profit = int(i[2]) - int(i[3])
    if profit >= 0:
        general_profit.append(profit)
    company_list[company] = profit

average_profit = {}
average_profit["average_profit"] = mean(general_profit)

# пишем в json
with open("test_dz5_7.json", "w", encoding='utf-8') as f:
    json.dump([company_list, average_profit], f)

# читаем из json
with open("test_dz5_7.json", "r", encoding='utf-8') as f2:
    data2 = json.load(f2)
    print(data2)
