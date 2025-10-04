from functools import total_ordering

@total_ordering
class Person:
    __id: str
    _name: str
    _age: int
    _smoking: bool

    AGE_LIMIT = 18

    num_of_people = 0
    example_names = ["Attila", "Beáta", "Cintia"]

    def __init__(self, id, name, age, smoking):
        self.__id = id
        self._name = name
        self._age = age
        self._smoking = smoking

        Person.num_of_people += 1

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, givenName: str):
        self._name = givenName

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int):
        if(type(age) != int):
            raise TypeError("age must be an integer")

        if(age <= 0 or age > 120):
            raise ValueError("age must be between 0 and 120")

        self._age = age

    def __str__(self):
        return '[id = {0}] : name = {1}, age = {2}, smoking = {3}'.format(self.__id, self._name, self._age, self._smoking)

    def __repr__(self):
        return "id = {0} name = {1}, age = {2}, smoking = {3}.".format(self.__id, self._name, self._age, self._smoking)

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __le__(self, other):
        return self.id <= other.id

    def __hash__(self):
        return hash(self.id)

    @staticmethod
    def is_adult(self):
        return self._age >= Person.AGE_LIMIT