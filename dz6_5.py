class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки канцелярией {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}')


stationery = Stationery('Rolex')
pen = Pen('Parker')
pencil = Pencil('Murzilka')
handle = Handle('Black_color')

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
