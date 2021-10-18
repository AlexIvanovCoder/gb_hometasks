class Clothes:
    def __init__(self, name):
        self.name = name

    @property
    def count_material_cost(self):
        pass

class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    def count_material_cost(self):
        return self.v / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    def count_material_cost(self):
        return 2 * self.h + 0.3

ct = Coat('Coat', 5)
print(vars(ct))
print(ct.count_material_cost())

st = Suit('Suit', 1)
print(vars(st))
print(st.count_material_cost())

print(ct.count_material_cost() + st.count_material_cost())
