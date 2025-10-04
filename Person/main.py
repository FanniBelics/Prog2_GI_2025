
class Person:
    id: str
    name: str
    age: int
    smoking: bool

    def __init__(self, id, name, age, smoking):
        self.id = id
        self.name = name
        self.age = age
        self.smoking = smoking

    def __str__(self):
        return '[id = {0}] : name = {1}, age = {2}, smoking = {3}'.format(self.id, self.name, self.age, self.smoking)

    def __repr__(self):
        return "{id = {0} name = {1}, age = {2}, smoking = {3}}.".format(self.id, self.name, self.age, self.smoking)

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __le__(self, other):
        return self.id <= other.id

    def __hash__(self):
        return hash(self.id)


def main():
    print("Hello World")
    p1 = Person("p1", "Antal", 45, False)
    p2 = Person("p2", "Barbara", 20, True)
    p3 = Person("p1", "Csaba", 26, True)

    print(p1)

    print(p1 == p2)
    print(p1 == p3)

    print(p1 > p2)

    print(p1.__hash__())



if __name__=="__main__":
    main()