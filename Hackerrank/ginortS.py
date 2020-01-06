
#Ți-a fost dat un șir.
#S conține doar caractere alfanumerice.
# Sarcina dvs. este de a sorta șirul S în felul următor:

#Toate literele minuscule sortate sunt înainte de litere mari.
#Toate literele majuscule sortate sunt înaintea cifrelor.
#Toate cifrele impare sortate sunt înainte de cifrele sortate.
#Formatul de intrare

#O singură linie de intrare conține șirul S.
#Format de iesire

#Ieșiți șirul sortat S.

#Sample Input

#Sorting1234
#Sample Output

#ginortS1324
#metoda 1
print("=== Metoda 1 ===")
print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

#metoda 2
print("=== Metoda 2 ===")
print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

#metoda 3
print("=== Metoda 3 ===")
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')

#metoda 4
print("=== Metoda 4 ===")
import string
print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')

#metoda 5
print("=== Metoda 5 ===")
def getKey(x):
    if x.islower():
        return(1,x)
    elif x.isupper():
        return(2,x)
    elif x.isdigit() :
        if int(x)%2==1:
            return(3,x)
        else :
            return(4,x)

print(*sorted(input(),key=getKey),sep='')

#metoda 6
print("=== Metoda 6 ===")
from string import ascii_lowercase, ascii_uppercase 
sortkey = ascii_lowercase + ascii_uppercase + "1357902468"
x = input()
print(*map(lambda y: y * x.count(y), sortkey), sep='')

#metoda 7
print("=== Metoda 7 ===")
import re

patterns = [ r'[a-z]', r'[A-Z]' , r'[13579]'  ,r'[02468]']
data = input()
t = [  r for pattern in patterns for r in sorted(re.findall( pattern, data ))  ]
print("".join(t))