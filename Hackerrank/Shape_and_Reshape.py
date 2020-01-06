

#formă

#Instrumentul de formă oferă un tuple de dimensiuni de matrice și poate fi utilizat pentru a modifica dimensiunile unui tablou.

#Using shape to get array dimensions

#import numpy

#my__1D_array = numpy.array([1, 2, 3, 4, 5])
#print my_1D_array.shape     #(5,) -> 5 rows and 0 columns

#my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
#print my_2D_array.shape     #(3, 2) -> 3 rows and 2 columns 
#(b). Using shape to change array dimensions

#import numpy

#change_array = numpy.array([1,2,3,4,5,6])
#change_array.shape = (3, 2)
#print change_array      

##Output
#[[1 2]
#[3 4]
#[5 6]]


#remodela

#Instrumentul de remodelare oferă o nouă formă unui tablou fără a-și schimba datele. Creează un nou tablou și nu modifică singur tabloul original.

#import numpy

#my_array = numpy.array([1,2,3,4,5,6])
#print numpy.reshape(my_array,(3,2))

##Output
#[[1 2]
#[3 4]
#[5 6]]

#Sarcină

#Vi se oferă o listă separată în spațiu de nouă întregi. Sarcina dvs. este de a converti această listă într-un tablou NumPy 3X3.

#Formatul de intrare

#O singură linie de intrare care conține 9 întregi separate de spațiu.

#Format de iesire

#Tipăriți matricea NumPy 3X3.

#Sample Input

#1 2 3 4 5 6 7 8 9
#Sample Output

#[[1 2 3]
# [4 5 6]
# [7 8 9]]

import numpy
i = input().split()
arr = numpy.array(i,int)
arr.shape =(3,3)

print(arr)


#metoda 2
import numpy as np
print(np.array(input().split(),int).reshape(3,3))
#metoda 3
print( numpy.reshape(numpy.array(input().split(),int),(3,3)))

#metoda 4
a=np.array(list(map(int,input().split())))
a.shape=(3,3)
print(a)

#metoda 5
def main():
    a = input().split(' ')
    a = numpy.array(a, int)
    print(numpy.reshape(a, (3, 3)))


if __name__ == "__main__":
    main()

#metoda 6
array = numpy.array([int(i) for i in input().split()])
print(numpy.reshape(array, (3,3)))

#metoda 7
print (numpy.fromstring(input(), dtype=int, sep=" ").reshape(3,3))