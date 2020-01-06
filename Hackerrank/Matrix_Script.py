
#Neo are un script matricial complex. Scriptul matricial este o grilă N x M de șiruri. Este format din caractere, spații și simboluri alfanumerice (!, @, #, $,%, &).

#Pentru a decoda scriptul, Neo trebuie să citească fiecare coloană și să selecteze doar caracterele alfanumerice și să le conecteze. Neo citește coloana de sus în jos și începe să citească din coloana din stânga.

#Dacă există simboluri sau spații între două caractere alfanumerice ale scriptului decodat, atunci Neo le înlocuiește cu un singur spațiu '' pentru o mai bună lizibilitate.

#Neo consideră că nu este necesar de a utiliza „dacă“ condițiile de decodare.

#Caracterele alfanumerice constau din: [A-Z, a-z și 0-9].

#Formatul de intrare

#Prima linie conține numere întregi N (rânduri) și, respectiv, M (coloane) separate de spațiu.
#Următoarele N linii conțin elementele de rând ale scriptului matricei.

#Format de iesire

#Print script matrice decodificat.

#Sample Input 0

#7 3
#Tsi
#h%x
#i #
#sM 
#$a 
##t%
#ir!
#Sample Output 0

#This is Matrix#  %!

#Explanation 0

#The decoded script is:

#This$#is% Matrix#  %!
#Neo replaces the symbols or spaces between two alphanumeric characters with a single space   ' ' for better readability.

#So, the final decoded script is:

#This is Matrix#  %!

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

print(re.sub(r'(\w)(\W)+(\w)',
          r'\1 \3',
          ''.join([u for t in zip(*matrix) for u in t])))

#metoda 2
import re

n, m = map(int, input().split())
a, b = [], ""
for _ in range(n):
    a.append(input())

for z in zip(*a):
    b += "".join(z)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))

#metoda 3
import re
n, m = map(int, input().split())
arr = ''.join([''.join(t) for t in zip(*[input() for _ in range(n)])])
print(re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', arr))

