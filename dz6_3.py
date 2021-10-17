class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


ivan = Position("Ivan", "Ivanov", "Doctor", {"wage": 50, "bonus": 2})
print(vars(ivan))
print(ivan.get_full_name())
print(ivan.get_total_income())
