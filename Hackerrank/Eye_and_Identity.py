
#identitate

#Instrumentul de identitate returnează un tablou de identitate.
# O matrice de identitate este o matrice pătrată cu toate elementele diagonale principale ca 1 și restul ca 0. 
# Tipul implicit de elemente este float.

#import numpy
#print numpy.identity(3) #3 is for  dimension 3 X 3

##Output
#[[ 1.  0.  0.]
# [ 0.  1.  0.]
# [ 0.  0.  1.]]

#ochi
#import numpy
#print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.

##Output
#[[ 0.  1.  0.  0.  0.  0.  0.]
# [ 0.  0.  1.  0.  0.  0.  0.]
# [ 0.  0.  0.  1.  0.  0.  0.]
# [ 0.  0.  0.  0.  1.  0.  0.]
# [ 0.  0.  0.  0.  0.  1.  0.]
# [ 0.  0.  0.  0.  0.  0.  1.]
# [ 0.  0.  0.  0.  0.  0.  0.]
# [ 0.  0.  0.  0.  0.  0.  0.]]

#print numpy.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.

#Instrumentul pentru ochi returnează un tablou 2-D cu 1-uri ca diagonală și 0-uri în altă parte. 
#Diagonala poate fi principală, superioară sau inferioară, în funcție de parametrul opțional k. 
#O k pozitivă este pentru diagonala superioară, o negativă k este cea inferioară, iar 0 k (implicit) este pentru diagonala principală.


#Sarcină

#Sarcina dvs. este de a imprima un tablou de dimensiuni NxM cu elementele sale diagonale principale ca 1 și 0 peste tot.

#Formatul de intrare

#O singură linie care conține valorile spațiale separate de N și M.
#N denumește rândurile.
#M indică coloanele.

#Format de iesire

#Tipăriți matricea NxM dorită.
#Sample Input

#3 3
#Sample Output

#[[ 1.  0.  0.]
# [ 0.  1.  0.]
# [ 0.  0.  1.]]

import numpy as np

n, m= map(int,input().split())

print(str(np.identity(n)).replace('1',' 1').replace('0', ' 0'))

#metoda 2
np.set_printoptions(sign=' ')
print(np.eye(*map(int, input().split())))

#metoda 3
np.set_printoptions(sign=' ')
n, m= map(int,input().split())
print(np.eye(n,m))
