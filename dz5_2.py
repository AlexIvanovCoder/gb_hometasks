with open("test_dz5_1.py", 'r', encoding='utf-8') as f:
    content = f.read().splitlines()
    for i in content:
        if i != "":
            word_count = len(i.split(" "))
        else:
            word_count = 0  # пустая строка
        print(f'Слов в строке: {i} = {word_count}')
    print(f'Всего строк: {len(content)}')
