
#punct

#Instrumentul dot returnează produsul punct din două tablouri

#import numpy

#A = numpy.array([ 1, 2 ])
#B = numpy.array([ 3, 4 ])

#print numpy.dot(A, B)       #Output : 11

#cruce

#Instrumentul încrucișat returnează produsul încrucișat din două tablouri.

#import numpy

#A = numpy.array([ 1, 2 ])
#B = numpy.array([ 3, 4 ])

#print numpy.cross(A, B)     #Output : -2

#Sarcină

#Vi se oferă două tablouri A și B. Ambele au dimensiuni de NxM.
#Sarcina dvs. este de a calcula produsul lor matrice.

#Formatul de intrare

#Prima linie conține numărul întreg N.
#Următoarele N linii conțin N numere întregi separate de spațiu ale tabloului A.
#Următoarele N linii conțin N numere întregi separate de spațiu ale tabloului B.

#Format de iesire

#Tipăriți înmulțirea matricială a A și B.

#Sample Input

#2
#1 2
#3 4
#1 2
#3 4
#Sample Output

#[[ 7 10]
# [15 22]]

import numpy as np

#n = int(input())
#a = np.array([input().split() for _ in range(n)],int)
#b = np.array([input().split() for _ in range(n)],int)

#print(np.dot(a,b)) 

#metoda 2
n = int(input())
a,b = (np.array([input().split() for _ in range(n)], int) for _ in range(2))

print(np.dot(a,b))

#metoda 3
#n = int(input())
#arrays = [list(map(int,input().split())) for _ in range(n*2)]
#print(np.matmul(arrays[:n],arrays[n:]))