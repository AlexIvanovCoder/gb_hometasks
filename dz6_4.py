class Car:
    is_police = False

    def __init__(self, color, name, speed):
        self.color = color
        self.name = name
        self.speed = speed

    def go(self, speed=30):
        self.speed = speed

        return f"Машина поехала. " + self.show_speed()

    def stop(self):
        self.speed = 0
        return f"Машина остановилась. " + self.show_speed()

    def turn(self, direction):
        if direction == "left":
            a = "налево"
        elif direction == "right":
            a = f"направо"
        return f'Машина повернула {a}. ' + self.show_speed()

    def show_speed(self):
        return f"Скорость = {self.speed}"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Скорость = {self.speed}. Превышение!"
        else:
            return f"Скорость = {self.speed}"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Скорость = {self.speed}. Превышение!"
        else:
            return f"Скорость = {self.speed}"


class PoliceCar(Car):
    is_police = True


car = Car("Red", "VW", 50)
print(vars(car))
print(car.go(60))
print(car.turn("left"))
print(car.stop())
print(car.show_speed())

town_car = TownCar("White", "Town", 70)
print(vars(town_car))
print(town_car.go(70))
print(town_car.turn("left"))
print(town_car.stop())

sport_car = SportCar("White", "Sport", 70)
print(vars(sport_car))
print(sport_car.go(60))
print(sport_car.turn("left"))
print(sport_car.stop())

police_car = PoliceCar("White", "Police", 50)
print(vars(police_car))
print(police_car.go())
print(police_car.turn("left"))
print(police_car.stop())

# как можно
"""
Вопрос:
Как можно сделать, чтобы в метод go по умолчанию подавалось значение атрибута speed, которое установлено при инициализациии
экземпляра класса (напр., для PoliceCar = 50), а не заданное в самом методе (30).
А то сейчас получается, что 30 затирает исходное значение. 

Т.е. чтобы я мог запустить print(car.go()) без параметра и он выдавал значение атрибута speed не 30, а то, которое было установлено при инициализации.
Напр., для класса Police car = 50. 
"""
