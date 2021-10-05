# 6
def int_func(word):
    "слово в верхнем регистре"
    return word[0].upper() + word[1:]

def upper_string(string):
    "строка в верхнем регистре"
    string = [int_func(i) for i in string.split(" ")]
    return " ".join(string)

print(upper_string("i want to break free"))