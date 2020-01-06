
#Transpune

#Putem genera transpunerea unui tablou folosind instrumentul numpy.transpose.
#Nu va afecta tabloul original, dar va crea un nou tablou.

#import numpy

#my_array = numpy.array([[1,2,3],
#                        [4,5,6]])
#print numpy.transpose(my_array)

##Output
#[[1 4]
# [2 5]
# [3 6]]

#Aplatiza

#Instrumentul aplatizează creează o copie a tabloului de intrare aplatizat la o dimensiune.

#import numpy

#my_array = numpy.array([[1,2,3],
#                        [4,5,6]])
#print my_array.flatten()

##Output
#[1 2 3 4 5 6]


#Sarcină

#Vi se oferă o matrice întreagă NxM cu elemente separate de spațiu (N = rânduri și M = coloane).
#Sarcina dvs. este de a imprima rezultatele transpuse și aplatizarea.

#Formatul de intrare

#Prima linie conține valorile spațiale separate de N și M.
#Următoarele N linii conțin elemente separate în spațiu ale coloanelor M.

#Format de iesire

#Mai întâi, imprimați tabloul de transpunere și apoi imprimați aplatizarea.

#Sample Input

#2 2
#1 2
#3 4
#Sample Output

#[[1 3]
# [2 4]]
#[1 2 3 4]
import numpy as np
n, m = map(int, input().split())
#print(n)
myArr = np.array([input().split() for _ in range(n)],int)
#print(myArr)

print(myArr.transpose())
print(myArr.flatten())

#metoda 2
n , m = input().split();
a = [];
for i in range(int(n)):
    my_array = input().split();
    a.append(my_array);
lis1 = numpy.array(a,int);
print(numpy.transpose(lis1))
print(lis1.flatten())