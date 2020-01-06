
#sum

#Instrumentul sumă returnează suma elementelor matricei pe o axă dată.

#import numpy

#my_array = numpy.array([ [1, 2], [3, 4] ])

#print numpy.sum(my_array, axis = 0)         #Output : [4 6]
#print numpy.sum(my_array, axis = 1)         #Output : [3 7]
#print numpy.sum(my_array, axis = None)      #Output : 10
#print numpy.sum(my_array)                   #Output : 10

#În mod implicit, valoarea axei este None. Prin urmare, execută o sumă peste toate dimensiunile tabloului de intrare.

#prod

#Instrumentul prod returnează produsul elementelor matricei pe o axă dată.

#import numpy

#my_array = numpy.array([ [1, 2], [3, 4] ])

#print numpy.prod(my_array, axis = 0)            #Output : [3 8]
#print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
#print numpy.prod(my_array, axis = None)         #Output : 24
#print numpy.prod(my_array)                      #Output : 24


#În mod implicit, valoarea axei este None. Prin urmare, execută produsul peste toate dimensiunile tabloului de intrare.

#Sarcină

#Vi se oferă un tablou 2-D cu dimensiunile NxM.
#Sarcina dvs. este să efectuați instrumentul de sumă peste axa 0 și apoi să găsiți produsul rezultatului respectiv.

#Formatul de intrare

#Prima linie de intrare conține valori separate de spațiu de N și M.
#Următoarele N linii conțin M numere întregi separate de spațiu.

#Format de iesire

#Calculați suma de-a lungul axei 0. Apoi, imprimați produsul sumei respective.

#Sample Input

#2 2
#1 2
#3 4
#Sample Output

#24

#Sample Input 1
#2 2
#1 2
#3 2

#Sample Output
#16
#Explanation

#The sum along axis 0 = [4 6]
#The product of this sum = 24

import numpy as np

n,m = map(int, input().split())

arr = np.array([input().split() for _ in range(n)],int)
print(arr)
print(np.prod(np.sum(arr, axis =0),axis =None))    

#metoda 2
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(np.prod(numpy.sum(arr,axis=0)))

#metoda 3
print(np.prod(np.sum(np.array([input().split() for _ in range(int(input().split()[0])) ],int),axis=0)))

#metoda 4
n,m = map(int,input().split())
ar = np.array([input().split() for i in range(n)], int)
print(np.prod((np.sum(ar,axis=0))))

#metoda 5
import numpy
def compute():
    dim = input().split()
    for i in range(len(dim)):
        dim[i] = int(dim[i])

    arr = []
    for i in range(dim[0]):
        ele = numpy.array(input().split() , int)
        arr.append(ele)
    arr = numpy.array(arr)

    print(numpy.prod(numpy.sum(arr , axis = 0)))
compute()