# 4
string = input("input string: ")
splt_string = string.split(" ")

for i in range(len(splt_string)):
    print(i, splt_string[i][:10]) # к i можно добавить + 1, если надо нумеровать с единицы
