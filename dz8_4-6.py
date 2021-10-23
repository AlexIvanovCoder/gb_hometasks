class MyTypeError(Exception):
    pass


class Warehouse:
    '''keeps tech objects and its properties'''
    tech_base = {}

    def add_to_wh(self, objects):
        '''add objects to warehouse'''
        for i in objects:
            self.tech_base[i.__class__.__name__] = vars(i)
        return self.tech_base


class Tech():
    '''general class for all the tech objects'''
    '''пробовал создать отдельный проверяющий метод 
    @staticmethod
    def validate_if_number(quant):
        print(quant)
        try:
            if quant.isdecimal() == False:
                raise MyTypeError(
                    f"{quant} is invalid because it is not numerical. Only numbers required. None is added")
        except MyTypeError as err:
            print(err)
            return None
        else:
            return quant
    
    и сделать 
    def __init__(self):
        self.quantity = validate_if_number(input(f'Введите количество товаров {self.__class__.__name__}:'))
     
    , но его не находит __init__.
    #а если убираю @staticmethod, то начинает "ругаться" на несоответствие количества объявленных и поданных аргументов
    
    Поэтому проверку вложил в init (что неправильно).
    Буду признателен за помощь, как встроить отдельный метод в init.
'''

    def __init__(self):
        quant = input(f'Введите количество товаров {self.__class__.__name__}:')
        try:
            if quant.isdecimal() == False:
                raise MyTypeError(
                    f"{quant} is invalid because it is not numerical. Only numbers required. None is added")
        except MyTypeError as err:
            print(err)
            quant = None
        else:
            self.quantity = quant
        self.department = ''

    def assign_department(self, department):
        self.department = department

    # class Tech' decendants


class Printer(Tech):
    def __init__(self, color):
        self.color = color
        super().__init__()


class Copier(Tech):
    def __init__(self, with_wi_fi):
        self.with_wi_fi = with_wi_fi
        super().__init__()


class Scanner(Tech):
    def __init__(self, resolution):
        self.resolution = resolution
        super().__init__()


pr = Printer('red')
pr.assign_department('purchase')
print(vars(pr))

cp = Copier(1)
cp.assign_department('marketing')
print(vars(cp))

sc = Scanner(180)
sc.assign_department('sales')
print(vars(sc))

wh = Warehouse()
objects = (pr, cp, sc)
tb = wh.add_to_wh(objects)
print(tb)
