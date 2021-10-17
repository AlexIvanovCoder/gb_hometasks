with open(r"C:\Users\Dell 7720\Documents\gb\python\lesson5\text_6.txt", 'r', encoding='utf-8') as f:
    content = [i.split(" ") for i in f.read().splitlines()]

    dict_lessons = {}

    for i in content:
        lesson_el = i[0].replace(":", "")
        sum_of_hours = 0
        for j in i[1:]:
            sum_of_hours += int(j.replace("-", "0").replace("(л)", "").replace("(пр)", "").replace("(лаб)", ""))
        dict_lessons[lesson_el] = sum_of_hours

    print(dict_lessons)
