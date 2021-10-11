with open("test_dz5_1.py", 'a', encoding='utf-8') as f:
    while 1 == 1:
        a = input("Введите текст: ")
        if a != '':
            f.writelines(a + '\n')
        else:
            f.writelines('\n')
            break
