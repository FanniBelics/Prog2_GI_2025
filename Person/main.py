
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


def main():
    print("Hello World")
    p1 = Person("p1", "Antal", 45, False)
    p2 = Person("p2", "Barbara", 20, True)

    print(p1)

    #print(p1 > p2)



if __name__=="__main__":
    main()