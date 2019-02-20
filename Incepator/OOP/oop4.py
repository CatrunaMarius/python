#Reloading of the operator of addition
class Animal:
    def __init__(self, species):
        self.species = species

    def __add__(self, another):
        hybrid = Animal.__hybrid_name(
            self.species, another.species)
        return Animal(hybrid)

    @staticmethod
    def __hybrid_name(first, second):
        ln = len(first)
        s1 = first[:(ln//2+1)]
        ln = len(second)
        s2 = second[(ln//2):]
        return s1 +s2

a1 = Animal("cat")
a2 = Animal("dog")
a3 = a1+a2
print(a3.species)

b1 = Animal("lion")
b2 = Animal("monkey")
b3 =b1 +b2
print(b3.species)

ab = a3 +b3
print(ab.species)

ba = b3 +a3
print(ba.species)
