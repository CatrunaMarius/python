
#Definiți o funcție care poate imprima un dicționar în care tastele sunt numere cuprinse între 1 și 20 (ambele incluse) și valorile sunt pătrate de taste.
#Utilizați dict [cheie] = modelul valorii pentru a introduce intrarea într-un dicționar. 
#Utilizați operatorul ** pentru a obține puterea unui număr.

def printDict():
    d=dict()
    for i in range(1,20):
        d[i]=i**2
    print(d)
printDict()

#Metoda 2
def printDict():
    dict={i:i**2 for i in range(1,21)}
    print(dict)
printDict()

#Problema 2
#Definiți o funcție care poate genera un dicționar 
#în care tastele sunt numere cuprinse între 1 și 20 (ambele incluse)
# și valorile sunt pătrate de taste.
# Funcția ar trebui să imprime doar tastele.
#Utilizați dict [key] = pattern pattern pentru a intra într-un dicționar.
#Utilizați ** operator pentru a obține puterea unui număr.
#Utilizați intervalul () pentru bucle.Useze tastele () pentru a repeta cheile din dicționar.
# De asemenea, putem folosi item () pentru a obține perechi cheie / valoare.

def printDict():
    d=dict()
    for i in range (1,21):
        d[i]=i**2
    for k in d.keys():
        print(k)
printDict()

#metoda 2
def printDict():
    dict = {i:i**2 for i in range(1,21)}
    print(dict.keys())
printDict()

#Problema 3
#Definiți o funcție care poate genera și
# tipări o listă în care valorile sunt pătrate de numere cuprinse 
# între 1 și 20 (ambele incluse).

def printList():
    l=list()
    for i in range(1,21):
        l.append(i)
    print(l)
printList()

#metoda 2

def printList():
    l =[i**2 for i in range (1,21)]
    print(l)
printList()

#Program 4
#Definiți o funcție care poate genera o listă în care 
#valorile sunt pătrate de numere cuprinse între 1 și 20 (ambele incluse). 
#Apoi funcția trebuie să imprime primele 5 elemente din listă.
#hints
#Utilizați operatorul ** pentru a obține puterea unui număr.
#Utilizați un interval () pentru loops.
#Use list.append () pentru a adăuga valori într-o listă.
# Utilizați [n1: n2] pentru a împărți o listă
def printList():
    l=list()
    for i in range(1,21):
        l.append(i**2)
    print(l[:5])
printDict()

#metoda 2
def printList():
    l=[i**2 for i in range(1,21)]
    for i in range(5):
        print(l[1])
printList()

#program 5
#Definiți o funcție care poate genera o listă în care 
#valorile sunt pătrate de numere cuprinse între 1 și 20 (ambele incluse). 
#Apoi funcția trebuie să imprime ultimele 5 elemente din listă.
#Hints
#Use ** operator to get power of a number.Use range() for loops.
#Use list.append() to add values into a list.
#Use [n1:n2] to slice a list

def printList():
    l=list()
    for i in range(1,21):
        l.append(i**2)
    print(l[-5:])
printList()

#metoda 2
def printList():
    l=[i**2 for i in range(1,21)]
    for i in range(19,14,-1):
        print(l[i])
printList()

#Problema 6
#Definiți o funcție care poate genera o listă în care valorile sunt pătrate de numere cuprinse între 1 și 20 (ambele incluse). 
#Apoi funcția trebuie să imprime toate valorile, cu excepția primelor 5 elemente din listă.
#
#Sugestii: Folosiți ** operator pentru a obține puterea unui număr. 
#Utilizați un interval () pentru loops.
#Use list.append () pentru a adăuga valori într-o listă.
# Utilizați [n1: n2] pentru a tăia o listă
def printList():
    l=list()
    for i in range(1,21):
        l.append(i**2)
    print(l[5:])
printList()

#metoda 2
def printList():
    l=[i**2 for i in range(1,21)]
    for i in range(5,20):
        print(l[i])
printList()

#Problema 7
#Definiți o funcție care poate genera
# și tipări un tuple în care valoarea este pătrat de numere cuprinse
#  între 1 și 20 (ambele incluse).
#hints
#Folosiți ** operator pentru a obține puterea unui număr.
#Utilizați un interval () pentru loops.
#Use list.append () pentru a adăuga valori într-o listă.

def printTuple():
    l=list()
    for i in range(1,21):
        l.append(i**2)
    print(tuple(l))
printTuple()

#metoda 2
def printTupple():
    l=[i**2 for i in range(1,21)]
    print(tuple(l))
printTupple()
