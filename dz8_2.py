class MyTypeError(Exception):
    pass


in_data = input("Enter a number: ")
try:
    in_data = int(in_data)
    if in_data == 0:
        raise MyTypeError("Only positive") #сгенерили ошибку
except(MyTypeError) as err: #поймали ошибку
    print(err)
else:
    print(100/in_data)
finally:  # что делать в любом случае
    print('The end')