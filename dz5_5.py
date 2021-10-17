# записать
with open("test_dz5_5.py", 'w', encoding='utf-8') as f:
    f.write(input("Введите числа разделенные пробелами: "))
#прочитать
with open("test_dz5_5.py", 'r', encoding='utf-8') as fr:
    print(sum([int(i) for i in fr.read().split(" ")]))