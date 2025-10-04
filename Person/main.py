from person import Person

def main():
    print("Hello World")
    p1 = Person("p1", "Antal", 45, False)
    p2 = Person("p2", "Barbara", 20, True)
    p3 = Person("p1", "Csaba", 26, True)

    print(p1)

    print(p1 == p2)
    print(p1 == p3)

    print(p1.__gt__(p2))
    print(p1>p2)
    print(p1>p3)

    print(p1.__hash__())



if __name__=="__main__":
    main()