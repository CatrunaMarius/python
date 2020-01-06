
#Scrieți un program care poate face o hartă () pentru a face o listă ale cărei elemente sunt pătrate de numere cuprinse între 1 și 20 (ambele incluse).

#sugestii:
#Folosiți harta () pentru a genera o listă. Utilizați lambda pentru a defini funcții anonime.

squareNumbers = map(lambda x: x**2, range(1,21))
print(list(squareNumbers))

#metoda 2
def sqr(x):
    return x*x

squaredNumbers = list(map(sqr,range(1,21)))
print(squaredNumbers)

#Problema 2
#Definiți o clasă numită american care are o metodă statică numită printNationality.

#sugestii:
#Utilizați decoratorul @staticmethod pentru a defini metoda statică a clasei.
# Există, de asemenea, alte două metode. Pentru a ști mai multe, accesați acest link.

class American(object):
    @staticmethod
    def PrintNationality():
        print("America")
anAmerican =American()
anAmerican.PrintNationality()
American.PrintNationality()

#metoda 2
class American():
    @staticmethod
    def printNationality():
        print("I am American")

american = American()
american.printNationality()
American.printNationality()

#Problema 3
#Definiți o clasă numită americană și subclasa sa NewYorker.

#sugestii:
#Utilizați clasa Subclase (ParentClass) pentru a defini o subclasă. *

class America(object):
    pass
class NewYorker(America):
    pass

anAmerican =America()
aNewYorker =NewYorker()
print(anAmerican)
print(aNewYorker)

