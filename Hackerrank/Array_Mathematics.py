
#Funcțiile matematice de bază operează în baza elementelor. Sunt disponibile atât ca supraîncărcări ale operatorului, cât și ca funcții în modulul NumPy.
#import numpy

#a = numpy.array([1,2,3,4], float)
#b = numpy.array([5,6,7,8], float)

#print a + b                     #[  6.   8.  10.  12.]
#print numpy.add(a, b)           #[  6.   8.  10.  12.]

#print a - b                     #[-4. -4. -4. -4.]
#print numpy.subtract(a, b)      #[-4. -4. -4. -4.]

#print a * b                     #[  5.  12.  21.  32.]
#print numpy.multiply(a, b)      #[  5.  12.  21.  32.]

#print a / b                     #[ 0.2         0.33333333  0.42857143  0.5       ]
#print numpy.divide(a, b)        #[ 0.2         0.33333333  0.42857143  0.5       ]

#print a % b                     #[ 1.  2.  3.  4.]
#print numpy.mod(a, b)           #[ 1.  2.  3.  4.]

#print a**b                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
#print numpy.power(a, b)         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04
#Sarcină

#Vi se oferă două tablouri întregi, A și B de dimensiuni NxM.
#Sarcina dvs. este să efectuați următoarele operații:

#Adăugați (A + B)
#Restă (A- B)
#Înmulțiți (A * B)
#Divizia întreagă (A / B)
#Mod (A% B)
#Putere (A ** B)
#Formatul de intrare

#Prima linie conține două întregi separate de spațiu, N și M.
#Următoarele N linii conțin M numere întregi separate de spațiu ale tabloului A.
#Următoarele N linii conțin M numere întregi separate de spațiu ale tabloului B.

#Format de iesire

#Tipăriți rezultatul fiecărei operații în comanda dată în Task.

import numpy as np

n, m =map(int, input().split())
a,b= (np.array([input().split()for _ in range(n)], dtype=int ) for _ in range(2))

print(a+b, b-a, a*b, a//b, a%b, a**b, sep='\n')

#metoda 2
N, M = list(map(int, input().split()))

a1 = np.array([input().split() for _ in range(N)], int)
a2 = np.array([input().split() for _ in range(N)], int)

print(*[eval('a1'+i+'a2') for i in ['+','-','*','//','%','**']], sep='\n')

#metoda 3
N, M = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(N)], int)
B = np.array([list(map(int, input().split())) for _ in range(N)], int)
print(np.add(A,B), np.subtract(A,B), np.multiply(A,B,), np.floor_divide(A,B), np.mod(A,B), np.power(A,B), sep = "\n")

#metoda 4
N, M = map(int, input().split())

operations = ['add', 'subtract', 'multiply', 'divide', 'mod', 'power']

a, b = [np.array([input().split() for _ in range(N)], int) for _ in range(2)]

for op in operations:
    print (eval('np.' + op + '(a, b)'))