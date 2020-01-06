#Definiți o clasă cu un generator care poate itera numerele, care sunt divizibile cu 7, între un interval 0 și n.

#sugestii:
#Luați în considerare utilizarea clasei, funcției și înțelegerii.

class test:
    def generator(self,n):
        return[i for i in range (n) if i%7==0]
n=int(input())
num= test()
l = num.generator(n)
print(l)

#Problema 2
#Un robot se deplasează într-un avion pornind din punctul inițial (0,0).
# Robotul se poate deplasa în sus, jos, stânga și dreapta, cu pași dat.
#  Urmele mișcării robotului sunt prezentate după cum urmează:

#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2

#Numerele după direcție sunt pași. 
#Vă rugăm să scrieți un program pentru a calcula distanța de la poziția curentă după o secvență de mișcare și punctul inițial.
# Dacă distanța este plutitoare, trebuie doar să imprimați cel mai apropiat număr întreg.
#  Exemplu: Dacă sunt introduse următoarele programe ca intrare în program:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#output 
#2
#hints
#În cazul în care datele de intrare sunt furnizate la întrebare, ar trebui să se presupună că este o intrare de consolă.
#Aici distanța indică distanța euclidiană. Modulul matematic pentru a utiliza funcția sqrt.

import math
pos =[0,0]
while True:
    s=input()
    if not s:
        break
    movement = s.split(' ')
    direction = movement[0]
    steps = int(movement[1])
    if direction =="UP":
        pos[0]+=steps
    elif direction =="DOWN":
        pos[0]-=steps
    elif direction =="LEFT":
        pos[1]-=steps
    elif direction =="RIGHT":
        pos[1]+=steps
    else:
        pass
print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))

#metoda 2

import math

x,y = 0,0
while True:
    s=input().split()
    if not s:
        break
    if s[0]=='UP':
        x+=int(s[1])
    if s[0]=='DOWN':
        x-=int(s[1])
    if s[0]=="LEFT":
        y-=int(s[1])
    if s[0]=="RIGHT":
        y+=int(s[1])
dist = round(math.sqrt(x**2+y**2))
print(dist)

