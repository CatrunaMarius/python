

#Modulul NumPy vine de asemenea cu o serie de rutine încorporate pentru calculele algebrei liniare. Acestea pot fi găsite în submodulul linalg.

#linalg.det

#Instrumentul linalg.det calculează determinantul unui tablou.

#print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0

#linalg.eig

#Linalg.eig calculează valorile proprii și valorile proprii drepte ale unui tablou pătrat.

#vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
#print vals                                      #Output : [ 3. -1.]
#print vecs                                      #Output : [[ 0.70710678 -0.70710678]
#                                                #          [ 0.70710678  0.70710678]]

#linalg.inv

#The linalg.inv tool computes the (multiplicative) inverse of a matrix.

#print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
#                                                #          [ 0.66666667 -0.33333333]]

#                                                Alte rutine pot fi găsite aici

#Sarcină

#Vi se oferă o matrice pătrată A cu dimensiunile NxN. Sarcina ta este să găsești determinantul. Notă: Rotunjiți răspunsul la 2 locuri după zecimal.

#Formatul de intrare

#Prima linie conține numărul întreg N.
#Următoarele N linii conțin elementele N separate de spațiu ale tabloului A.

#Format de iesire

#Tipăriți determinantul lui A.

#Sample Input

#2
#1.1 1.1
#1.1 1.1
#Sample Output

#0.0
import numpy as np
n=int(input())
a=np.array([input().split() for _ in range(n)],float)
np.set_printoptions(legacy='1.13') #important
print(np.linalg.det(a))

#metoda 2
np.set_printoptions(legacy='1.13') #important
A=[[float(x) for x in input().split(' ')] for i in range(int(input()))]
print(np.linalg.det(A))