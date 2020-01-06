#Vă rugăm să scrieți un program pentru a imprima aleatoriu un număr întreg între 7 și 15 inclusiv.

#sugestii
#Utilizați random.randrange () la un număr întreg aleator dintr-un interval dat.

import random
print(random.randrange(7,16))

#Problema 2
#Vă rugăm să scrieți un program pentru a comprima și decomprima șirul "salut lume! Salut lume! Salut lume! Salut lume!".

#sugestii
#Folosiți zlib.compress () și zlib.decompress () pentru a comprima și decomprima un șir.

import zlib
s='hello world!hello world!hello world!hello world!'
t = zlib.compress(s.encode("utf-8"))
print(t)
print(zlib.decompress(t))

#metoda 2
s= b'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))

#problema 3
#Vă rugăm să scrieți un program pentru a imprima de fiecare data cand ruleaza  „1 + 1” de 100 de ori.

#sugestii
#Utilizați funcția timeit () pentru a măsura timpul de rulare.

from timeit import Timer
t =Timer("for i in range(100):1+1")
print(t.timeit())

#problema 4
#Vă rugăm să scrieți un program pentru a amesteca și tipări lista [3,6,7,8].

#sugestii
#Utilizați funcția shuffle () pentru a amesteca o listă.

from random import shuffle
l = [3,6,7,8]
shuffle(l)
print(l)

#metoda 2
import random
l = [3,6,7,8]
seed =7
random.Random(seed).shuffle(l)
print(l)

#problema 5
#Vă rugăm să scrieți un program pentru a genera toate propozițiile în care subiectul este în [„Eu”, „Tu”] și verbul este în [„Joacă”, „Iubire”], iar obiectul este în [„Hockey”, „Fotbal”].

#sugestii
#Folosiți nota [index] pentru a obține un element dintr-o listă.

subjects =["I", "You"]
verbs =["Play","Love"]
objects = ["Hockey", "Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence ="%s %s %s." %(subjects[i],verbs[i],objects[i])
            print(sentence)

#metoda 2
subjects= ["I", "You"]
verbs=["Play","Love"]
objects=["Hockey","Football"]

for sub in  subjects:
    for verb in verbs:
        for obj in objects:
            print("{} {} {}".format(sub,verb,obj))
