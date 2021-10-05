# 2
def user_info_in_one_line(**kwargs):
    out_string = ""
    for key, value in kwargs.items():
        out_string += f'{key}: {value} \n'    
    return out_string

print(user_info_in_one_line(name = "Max"
                            , surname = "Power"
                            , birthyear = 2120
                            , city = "Moscow"
                            , e_mail = "max@ru.ru"
                            , phone = "222-22-22" ))