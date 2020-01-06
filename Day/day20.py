
#Având în vedere foaia de participare a participanților pentru Ziua Sportului Universitar, vi se cere să găsiți punctajul de alergare. Vi se acordă scoruri. Stocați-le într-o listă și găsiți scorul de al doilea.

#Dacă următoarea șir este dată ca intrare pentru program:

#5
#2 3 6 6 5
#Apoi, rezultatul programului ar trebui să fie:

#5
#sugestii
#Faceți scorurile unice și apoi găsiți al doilea cel mai bun număr

n= int(input())
arr = map(int, input().split())
arr = list(set(arr))
arr.sort()
print(arr[-2])

##program 2
##Vi se oferă un string S și lățimea W. Sarcina dvs. este să înfășurați string într-un paragraf de lățime.

##Dacă următoarea string este dată ca intrare pentru program:

##ABCDEFGHIJKLIMNOQRSTUVWXYZ
##4
##Apoi, rezultatul programului ar trebui să fie:

##ABCD
##EFGH
##IJKL
##NU SUNT
##QRST
##UVWX
##YZ
##sugestii
##Utilizați funcția de înfășurare a modulului de învelire text

import textwrap

def wrap(string, max_width):
    string = textwrap.wrap(string,max_width)
    string = "\n".join(string)
    return string

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)

##program 3

##Vi se oferă un număr întreg, N. Sarcina dvs. este de a imprima un alfabet rangoli de dimensiunea N. (Rangoli este o formă de artă populară indiană bazată pe crearea de tipare.)

##Mai jos sunt prezentate diferite dimensiuni de rangoli ale alfabetului:

### dimensiunea 3

##---- c ----
##--c-b-C--
##c-b-a-b-c
##--c-b-C--
##---- c ----

### dimensiunea 5

##-------- e --------
##------ e-d-e ------
##---- e-d-c-d-e ----
##--e-d-c-b-c-d-E--
##e-d-c-b-a-b-c-d-e
##--e-d-c-b-c-d-E--
##---- e-d-c-d-e ----
##------ e-d-e ------
##-------- e --------
##sugestii
##Primiți mai întâi jumătatea Rangoli în modul dat și salvați fiecare linie într-o listă. Apoi imprimați lista în ordine inversă pentru a obține restul.

import string
def print_rangoli(size):
    n= size
    alph = string.ascii_lowercase
    width = 4*n-3

    ans =[]
    for i in range(n):
        left = '-'.join(alph[n-i-1:n])
        mid = left[-1:0:-1] + left
        final = mid.center(width,'-')
        ans.append(final)
    if len(ans)>1:
        for i in ans[n-2::-1]:
            ans.append(i)
    ans ='\n'.join(ans)
    print(ans)

n= int(input())
print_rangoli(n)

#Problema 4
#Vi se oferă o dată. Sarcina ta este să găsești care este ziua la acea dată.

#Intrare

#O singură linie de intrare care conține spațiul, luna, ziua și anul, separat în format MM DD AAAA.

#08 05 2015
#producție

#Afișează ziua corectă cu majuscule.

#MIERCURI
#sugestii
#Utilizați funcția în timpul săptămânii din modulul calender

import calendar
month , day ,year= map(int, input().split())
dayId = calendar.weekday(year,month,day)
print(calendar.day_name[dayId].upper())

#problema 5
#Dat fiind 2 seturi de numere întregi, M și N, imprimați diferența lor simetrică în ordine crescătoare. Termenul diferență simetrică indică acele valori care există fie în M, fie în N, dar nu există în ambele.

#Intrare

#Prima linie de intrare conține un număr întreg, M. A doua linie conține M numere întregi separate de spațiu. A treia linie conține un număr întreg, N. A patra linie conține N întregi separate de spațiu.

#4
#2 4 5 9
#4
#2 4 11 12
#producție

#Afișează diferențele simetrice întregi în ordine crescătoare, una pe fiecare linie.

#5
#9
#11
#12
#sugestii
#Folosiți „^” pentru a face operațiunea de diferență simetrică.

n= int(input())
set1 = set(map(int, input().split()))

m = int(input())
set2 = set(map(int,input().split()))

ans = list(set1 ^ set2)
ans.sort()
for i in ans:
    print(i)
