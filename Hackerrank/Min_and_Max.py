
#min

#Instrumentul min returnează valoarea minimă de-a lungul unei axe date.

#import numpy

#my_array = numpy.array([[2, 5], 
#                        [3, 7],
#                        [1, 3],
#                        [4, 0]])

#print numpy.min(my_array, axis = 0)         #Output : [1 0]
#print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
#print numpy.min(my_array, axis = None)      #Output : 0
#print numpy.min(my_array)                   #Output : 0

#În mod implicit, valoarea axei este None. Prin urmare, găsește minimul pentru toate dimensiunile tabloului de intrare.

#max

#Instrumentul maxim returnează valoarea maximă de-a lungul unei axe date.

#import numpy

#my_array = numpy.array([[2, 5], 
#                        [3, 7],
#                        [1, 3],
#                        [4, 0]])

#print numpy.max(my_array, axis = 0)         #Output : [4 7]
#print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
#print numpy.max(my_array, axis = None)      #Output : 7
#print numpy.max(my_array)                   #Output : 7


#În mod implicit, valoarea axei este None. Prin urmare, găsește maximul pentru toate dimensiunile tabloului de intrare.

#Sarcină

#Vi se oferă un tablou 2-D cu dimensiunile NxM.
#Sarcina dvs. este să efectuați funcția min peste axa 1 și apoi să găsiți maxima.

#Formatul de intrare

#Prima linie de intrare conține valorile spațiale separate de N și M.
#Următoarele N linii conțin M numere întregi separate de spațiu.

#Format de iesire

#Calculați minul de-a lungul axei 1 și apoi imprimați maximul rezultatului respectiv.
import numpy as np
n,m = map(int,input().split())
arr= np.array([input().split() for _ in range(n)],int)

print(np.max(np.min(arr,axis = 1)))