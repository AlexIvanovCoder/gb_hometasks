class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_count(self, mass_1cm, fatness):
        return self._length * self._width * mass_1cm * fatness / 1000


mkad = Road(5, 2)

mkad_weight = mkad.mass_count(2, 2)
print(mkad_weight)
