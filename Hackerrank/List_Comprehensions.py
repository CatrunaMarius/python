

#Haideți să aflăm despre înțelegerile listelor! Vi se oferă trei întregi x, y și z reprezentând dimensiunile unui cuboid împreună cu un număr întreg. Trebuie să imprimați o listă a tuturor coordonatelor posibile date de (i, j, k) pe o grilă 3D în care suma i + j + k nu este egală cu. Aici, 0 <= i <= X; 0 <= j <= y; 0 <= k <= z
#Format de intrare

#Patru numere întregi x, y, z și n fiecare pe patru linii separate, respectiv.

#Constrângerile

#Tipăriți lista în ordine lexicografică în creștere.

#Sample Input 0

#1
#1
#1
#2
#Sample Output 0

#[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

#Sample Input 1

#2
#2
#2
#2
#Sample Output 1

#[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
#creaza o lista pt x,y,z
xlist = range(int(input())+1)#creaza un range (0,3) 
ylist = range(int(input())+1)#creaza un range (0,3) 
zlist = range(int(input())+1)#creaza un range (0,3) 
print(xlist,ylist,zlist,sep= '\n')
n = int(input())
#for z in zlist:
     #print(z)
#for x in xlist aceasta creaza o lista pt x 
c= [[x,y,z] for x in xlist for y in ylist for z in zlist if x+y+y !=n]
print(c)
