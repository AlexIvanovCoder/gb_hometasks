class MyTypeError(Exception):  # в класс-исключение мы ничего не вводим
    pass


class Lst:
    def __init__(self):
        self.lst = []

    def fill_lst_with_nums(self):
        while 1 == 1:
            elt = input('Введите число: ')
            if elt == 'stop':
                return self.lst
            try:
                if elt.isdecimal() == False:
                    raise MyTypeError(
                        f"{elt} is invalid because it is not numerical. Only numbers required")  # сгенерили ошибку
            except MyTypeError as err:  # поймали ошибку
                print(err)

            else:
                self.lst.append(int(elt))

mcl = Lst()
print(mcl.fill_lst_with_nums())
