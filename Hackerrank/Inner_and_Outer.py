

#interior/inner

#Instrumentul interior returnează produsul interior al două tablouri.

#import numpy

#A = numpy.array([0, 1])
#B = numpy.array([3, 4])

#print numpy.inner(A, B)     #Output : 4


#exterior/outer

#Instrumentul exterior returnează produsul exterior al două tablouri.

#import numpy

#A = numpy.array([0, 1])
#B = numpy.array([3, 4])

#print numpy.outer(A, B)     #Output : [[0 0]
#                            #          [3 4]]


#Sarcină

#Vi se oferă două tablouri: A și B.
#Sarcina dvs. este de a calcula produsul lor interior și exterior.

#Formatul de intrare

#Prima linie conține elemente separate de spațiu ale tabloului A.
#A doua linie conține elemente separate de spațiu ale tabloului B.

#Format de iesire

#Mai întâi, imprimați produsul interior.
#În al doilea rând, imprimați produsul exterior.

#Sample Input

#0 1
#2 3
#Sample Output

#3
#[[0 0]
# [2 3]]

import numpy as np

a = np.array(input().split(),int)
b = np.array(input().split(),int)

print(np.inner(a,b),np.outer(a,b), sep='\n')

#metoda 2
A,B = [np.array([input().split()],int) for _ in range(2)]
print(np.inner(A,B)[0][0],np.outer(A,B),sep="\n")

#metoda 3
A, B = [np.array(input().split(), int) for _ in range(2)]
print ('\n'.join(str(op(A, B)) for op in (np.inner, np.outer)))