
#Vă rugăm să scrieți un program care să scoată un număr parator între 0 și 10 inclusiv, 
#folosind modulul aleatoriu și înțelegerea listei.
#Sugestii Utilizați random.choice () la un element aleator dintr-o listă

import random

print(random.choice([i for i in range(11) if i%2==0]))

#metoda 2
resp = [i for i in range(0,11,2)]
print(random.choice(resp))

#Problema 2
#Vă rugăm să scrieți un program care să scoată un număr aleatoriu, 
#care poate fi divizibil cu 5 și 7, între 10 și 150 inclusiv, 
#folosind modulul aleatoriu și înțelegerea listei.

#sugestii
#Utilizați random.choice () la un element aleator dintr-o listă.

import random
print(random.choice([i for i in range(10,151) if i%5==0 and i%7==0]))

#metoda 2
resp = [i for i in range(10,151) if i %35 ==0]
print(random.choice(resp))

#Problema 3
#Vă rugăm să scrieți un program pentru a genera o listă cu 5 numere aleatorii între 100 și 200 inclusiv.

#sugestii
#Utilizați random.sample () pentru a genera o listă de valori aleatorii.

import random
print(random.sample(range(100,201),5))

#Problema 4
#Vă rugăm să scrieți un program pentru a genera aleatoriu o listă cu 5 numere uniforme între 100 și 200 inclusiv.

#sugestii
#Utilizați random.sample () pentru a genera o listă de valori aleatorii.

import random
print(random.sample([i for i in range(100,201) if i%2==0],5))

#metoda 2
import random
resp = random.sample(range(100,201,2),5)
print(resp)

#Problema 5
#Vă rugăm să scrieți un program pentru a genera aleatoriu o listă cu 5 numere,
# care sunt divizibile cu 5 și 7, între 1 și 1000 inclusiv.

#sugestii
#Utilizați random.sample () pentru a genera o listă de valori aleatorii.

import random
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0],5))

#metoda 2
l = [i for i in range(1,1001) if i%35==0]
resp= random.sample(l,5)
print(resp)

