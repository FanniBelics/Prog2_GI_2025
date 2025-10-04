from functools import total_ordering

@total_ordering
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