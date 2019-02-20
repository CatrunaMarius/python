class Person:
    def __init__(self,person_name, person_surname):
        self.name = person_name
        self.surname =person_surname

    def about(self):
        return self.name + ' ' +self.surname

men = []

for i in range(5):
    one = input("Entre persone: ")
    one = one.split()
    men.append(Person(one[0], one[1]))

    for i in men:
        print(i.about())

