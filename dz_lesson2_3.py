# 3
#словарь месяц-время года
month_num = int(input("input month number: "))

seasons = {
    'autumn' : [9, 10, 11]
    ,'winter' : [12, 1, 2]
    ,'spring' : [3, 4, 5]
    ,'summer' : [6, 7, 8]  
}

for i,j in seasons.items():
    if month_num in j:
        print(i)
        break