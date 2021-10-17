# создаем словарь
dict_numbers = {"One": "Один",
                "Two": "Два",
                "Three": "Три",
                "Four": "Четыре"}
# редактируем содержимое файла
with open(r"C:\Users\Dell 7720\Documents\gb\python\lesson5\text_4.txt", 'r', encoding='utf-8') as f:
    content = [i.split(" ") for i in f.read().splitlines()]
    for i in content:
        i[0] = dict_numbers[i[0]]
# пишем в новый файл
with open("test_dz5_4.py", 'w', encoding='utf-8') as fl:
    fl.writelines([" ".join(i) + "\n" for i in content])
