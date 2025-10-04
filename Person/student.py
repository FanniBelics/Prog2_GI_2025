from person import Person


class Student(Person):
    neptun: str

    def __init__(self, id, name, age, smoking, neptun):
        super().__init__(id, name, age, smoking)
        self.neptun = neptun

    def __str__(self):
        return super().__str__() + " neptun = {0}".format(self.neptun)