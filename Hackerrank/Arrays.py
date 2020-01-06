

Arrays

Un tablou NumPy este o grilă de valori. Sunt similare cu listele, cu excepția faptului că fiecare element al unui tablou trebuie să fie de același tip.

import numpy

a = numpy.array([1,2,3,4,5])
print a[1]          #2

b = numpy.array([1,2,3,4,5],float)
print b[1]          #2.0

În exemplul de mai sus, numpy.array () este utilizat pentru a converti o listă într-un tablou NumPy. Al doilea argument (float) poate fi utilizat pentru a seta tipul de elemente de matrice.

Sarcină

#Vi se oferă o listă de numere separată de spațiu.
#Sarcina dvs. este de a imprima un tablou NumPy inversat cu float-ul de tip element.

#Formatul de intrare

#O singură linie de intrare care conține numere separate în spațiu.

#Format de iesire

#Imprimați tabloul invers NumPy cu float tip.

#Sample Input

#1 2 3 4 -8 -10
#Sample Output

#[-10.  -8.   4.   3.   2.   1.]

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    #revrser array first, convert to float array with numpy
    return numpy.array(arr[::-1],float)
    
     #metoda 2
    return numpy.flipud(numpy.array(arr, float))
    #metoda 3
    return numpy.array(arr, float)[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)