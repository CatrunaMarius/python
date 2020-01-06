

#Haideți să ne cufundăm în subiectul interesant al expresiilor obișnuite! Vi se oferă o anumită intrare și trebuie să verificați dacă sunt numere de telefon valabile.

#Un număr mobil valid este un număr de zece cifre care începe cu un 7,8 sau 9.

#Concept

#Un număr mobil valid este un număr de zece cifre care începe cu un 7,8 sau 9.

#Expresiile regulate sunt un concept cheie în orice limbaj de programare. O explicație rapidă cu exemple Python este disponibilă aici. De asemenea, puteți parcurge link-ul de mai jos pentru a citi mai multe despre expresiile obișnuite din Python.

#https://developers.google.com/edu/python/regular-expressions

#Formatul de intrare

#Prima linie conține un număr întreg N, numărul de intrări.
#Urmează N linii, fiecare conținând unele șiruri.

#Format de iesire

#Pentru fiecare șir listat, imprimați „DA” dacă este un număr mobil valid și „NU” dacă nu este pe linii separate. Nu imprimați ghilimelele.

#Sample Input

#2
#9587456281
#1252478965
#Sample Output

#YES
#NO


import re
N=int(input())
for i in range(N):

 if re.match(r'[789]\d{9}$',input()):   
    print ('YES')  
 else:  
    print ('NO') 

#metoda 2

[print('YES' if re.match(r'[789]\d{9}$',input()) else 'NO') for _ in range(int(input()))]

#metoda 3
n = int(input())
pattern = re.compile(r'^[7-9]\d{9}$')
numbers = [input() for _ in range(n)]

for number in numbers:
    if pattern.match(number):
        print('YES')
    else:
        print('NO')

metoda 4
import re


numbers = int(input("")) #numbers you want to add
ls = []
for i in range(0,numbers):
    x = input("") # mobile numbers
    k = re.sub("\D","",x) # replace all non digit character
    ls.append(k)

for y in range(len(ls)):
    match1 = re.search("7", ls[y][0])
    match2 = re.search("8", ls[y][0])
    match3 = re.search("9", ls[y][0])
    if (match1 or match2 or match3) and len(ls[y]) == 10:
        print ("Yes")
    else:
        print ("No")