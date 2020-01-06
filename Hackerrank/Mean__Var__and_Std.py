
#Rău/mean

#Instrumentul mediu calculează media aritmetică de-a lungul axei specificate.

#import numpy

#my_array = numpy.array([ [1, 2], [3, 4] ])

#print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
#print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
#print numpy.mean(my_array, axis = None)     #Output : 2.5
#print numpy.mean(my_array)                  #Output : 2.5


#În mod implicit, axa este None. Prin urmare, calculează media tabloul aplatizat.

#var

#Instrumentul var calculează variația aritmetică de-a lungul axei specificate.

#import numpy

#my_array = numpy.array([ [1, 2], [3, 4] ])

#print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
#print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
#print numpy.var(my_array, axis = None)      #Output : 1.25
#print numpy.var(my_array)                   #Output : 1.25


#În mod implicit, axa este None. Prin urmare, calculează variația tabloului aplatizat.

#std

#Instrumentul std calculează abaterea standard aritmetică de-a lungul axei specificate.

#import numpy

#my_array = numpy.array([ [1, 2], [3, 4] ])

#print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
#print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
#print numpy.std(my_array, axis = None)      #Output : 1.11803398875
#print numpy.std(my_array)                   #Output : 1.11803398875


#În mod implicit, axa este None. Prin urmare, calculează abaterea standard a tablei aplatizate.

#Sarcină

#Vi se oferă o gamă 2-D de dimensiune NxM.
#Sarcina ta este să găsești:

#Media de-a lungul axei 1
#Var de-a lungul axei 0
#Std de-a lungul axei Nici unul
#Formatul de intrare

#Prima linie conține valorile spațiale separate de N și M.
#Următoarele N linii conțin M numere întregi separate de spațiu.

#Format de iesire

#În primul rând, imprimați media.
#În al doilea rând, tipăriți varianta.
#În al treilea rând, imprimați std.

#Sample Input

#2 2
#1 2
#3 4
#Sample Output

#[ 1.5  3.5]
#[ 1.  1.]
#1.11803398875

import numpy as np
np.set_printoptions(legacy = '1.13')
n,m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)],int)
print(np.mean(arr, axis =1),np.var(arr, axis =0) ,np.std(arr,axis=None),sep='\n')

#metoda 2
n,m = map(int, input().split())
b = []
for i in range(n):
    a = list(map(int, input().split()))
    b.append(a)

b = np.array(b)

np.set_printoptions(legacy='1.13')
print(np.mean(b, axis = 1))
print(np.var(b, axis = 0))
print(np.std(b))