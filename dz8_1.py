# dz8_1
'''
@staticmethod можно также как и @classmethod использовать без инициализации класса
'''


class Date:
    @classmethod
    def convert_date_to_int(cls, dt):
        return list(map(int, dt.split('-')))

    @staticmethod
    def validate_date(dt):
        dt_num = Date.convert_date_to_int(dt)

        if 1 > dt_num[0] or dt_num[0] > 31 \
                or 1 > dt_num[1] or dt_num[1] > 12 \
                or 1 > dt_num[2] or dt_num[2] > 2021:
            raise ValueError('Date is not valid')
        else:
            return dt_num


print(Date.validate_date(input('Введите дату в формате "дд-мм-гггг": ')))
