
#Vă rugăm să scrieți afirmații pentru a verifica dacă fiecare număr din listă [2,4,6,8] este egal.

#sugestii
#Utilizați „afirmare expresie” pentru a face afirmație.

li = [2,4,6,8]
for i in li:
    assert i%2==0

#metoda 2
date = [2,4,5,6]
for i in date:
    assert i%2 ==0, "{} is not an even number".format(i) 

    #problema 2
#    Vă rugăm să scrieți un program care acceptă expresia matematică de bază din consolă și să imprimați rezultatul evaluării.

#Exemplu: Dacă următorul n este dat ca intrare pentru program:

#35 + 3
#Apoi, rezultatul programului ar trebui să fie:

#38
#sugestii
#Folosiți eval () pentru a evalua o expresie.

calcul = input()
print(eval(calcul))

#problema 3
#Vă rugăm să scrieți o funcție de căutare binară care caută un articol dintr-o listă sortată.
# Funcția ar trebui să returneze indexul elementului care trebuie căutat în listă.

#sugestii
#Folosiți dacă / elif pentru a face față condițiilor.

import math
def bin_search(li,element):
    bottom=0
    top = len(li)-1
    index =-1
    while top>=bottom and index ==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index =mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid +1
    return index

li = [2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))
#Problema 4
#Vă rugăm să generați un float aleatoriu unde valoarea este între 10 și 100 folosind modulul Python.

#sugestii
#Utilizați random.random () pentru a genera un float aleator în [0,1].

import random
rand_num = random.uniform(10,100)
print(rand_num)

#Problema 5
#Vă rugăm să generați un float aleatoriu unde valoarea este între 5 și 95 folosind modulul Python.

#sugestii
#Utilizați random.random () pentru a genera un float aleator în [0,1].
import random
print(random.uniform(5,95))
