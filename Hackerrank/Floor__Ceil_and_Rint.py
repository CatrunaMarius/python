
#floor/podea
#Podeaua de instrumente returnează podeaua elementului de intrare.
#Etajul lui x este cel mai mare număr întreg i unde i <= x.

#import numpy

#my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
#print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

#ceil/tencui
#Plafonul instrumentului returnează plafonul elementului de intrare.
#Plafonul lui x este cel mai mic număr întreg i unde i> = x.

#import numpy

#my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
#print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]

#rint/rintați
#Instrumentul rint se apropie de cel mai apropiat număr întreg de element de intrare.


#Sarcină
#Vi se oferă un tablou 1-D, A. Sarcina dvs. este de a imprima podeaua, tavanul și rinderea tuturor elementelor din A.

#Formatul de intrare

#O singură linie de intrare care conține elemente separate în spațiu ale tabloului A.

#Format de iesire

#Pe prima linie, imprimați podeaua lui A.
#Pe a doua linie, imprimați tavanul lui A.
#Pe a treia linie, imprimați rintul lui A.

#Sample Input

#1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
#Sample Output

#[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
#[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
#[  1.   2.   3.   4.   6.   7.   8.   9.  10.]

import numpy as np

numpy.set_printoptions(sign=' ')
a = np.array(input().split(),float)
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))

#metoda 2
a = np.array(input().split(), float)
print(*(f(a) for f in [np.floor, np.ceil, np.rint]), sep='\n')


