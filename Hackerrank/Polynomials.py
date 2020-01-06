
#poli/poly

#Instrumentul poli returnează coeficienții unui polinom cu secvența dată de rădăcini.

#print numpy.poly([-1, 1, 1, 10])        #Output : [  1 -11   9  11 -10]


#rădăcini/roots

#Instrumentul rădăcini returnează rădăcinile unui polinom cu coeficienții dat.

#print numpy.roots([1, 0, -1])           #Output : [-1.  1.]

#polyint

#Instrumentul Polyint returnează un antiderivativ (integrală nedeterminată) al unui polinom.

#print numpy.polyint([1, 1, 1])          #Output : [ 0.33333333  0.5         1.          0.        ]



#polyder

#Instrumentul polder returnează derivatul din ordinea specificată a unui polinom.
#print numpy.polyder([1, 1, 1, 1])       #Output : [3 2 1]

#polyval

#Instrumentul polivalent evaluează polinomul la o valoare specifică.

#print numpy.polyval([1, -2, 0, 2], 4)   #Output : 34

#polyfit

#Instrumentul polyfit se potrivește unui polinom al unei ordini specificate unui set de date folosind o abordare cu cel puțin pătrate.

#print numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2)
##Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]

#Funcțiile polyadd, polysub, polimul și polidiv gestionează, de asemenea, adunarea, scăderea, înmulțirea și împărțirea corespunzătoare a coeficienților, respectiv.

#Sarcină

#Vi se dau coeficienții unui polinom P.
#Sarcina dvs. este de a găsi valoarea lui P în punctul x.

#Formatul de intrare

#Prima linie conține valoarea spațiului separat de coeficienții din P.
#A doua linie conține valoarea lui x.

#Format de iesire

#Tipăriți valoarea dorită.

#Sample Input

#1.1 2 3
#0
#Sample Output

#3.0

import numpy as np

p =np.array(input().split(),float)

x= float(input())
print(np.polyval(p,x))

#metoda 2
#p=list(map(float, input().split()))
#m = float(input())
#print(np.polyval(p, m))

##metoda 3
#print(np.polyval(list(map(float,input().split())),float(input()))) 

#metoda 4
#PC=[float(x) for x in input().split()]
#print(PC)
#value=float(input())
#print(np.polyval(PC,value))

