

#Vi se oferă un z complex. Sarcina ta este să o transformi în coordonate polare.

#Formatul de intrare

#O singură linie care conține numărul complex z. Notă: funcția complexă () poate fi utilizată în python pentru a converti intrarea ca număr complex.

#Constrângerile

#Numărul dat este un număr complex valid

#Format de iesire

#Ieșire două linii:
#Prima linie trebuie să conțină valoarea r.
#A doua linie ar trebui să conțină valoarea lui s.

#Sample Input

#  1+2j
#Sample Output

# 2.23606797749979 
# 1.1071487177940904
import cmath

#metoda 1
#r = complex(input().strip())

#print(cmath.polar(r)[0])
#print(cmath.polar(r)[1])

#metoda 2
#[print(round(i,20)) for i in cmath.polar(complex(input()))]

#metoda 3
from cmath import phase
print((lambda x: '%.3f\n%.3f' % (abs(x), phase(x)))(complex(input())))