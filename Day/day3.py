
#Un site web solicită utilizatorilor să introducă numele de utilizator și parola pentru a se înregistra.
#Scrieți un program pentru a verifica validitatea introducerii de parole de către utilizatori.
# Următoarele sunt criteriile pentru verificarea parolei:
#   Cel puțin o literă între [az] Cel puțin 1 număr între [0-9] 
#   Cel puțin 1 scrisoare între [AZ]
#   Cel puțin 1 caracter din [$ # @] 
#   Lungimea minimă a parolei tranzacției : 6 
#   Durata maximă a parolei de tranzacție: 12
# Programul dvs. ar trebui să accepte o secvență de parole separate prin virgulă și le va verifica în conformitate cu criteriile de mai sus.
# Parolele care corespund criteriilor vor fi tipărite, fiecare separat de virgulă.
# Exemplu Dacă următoarele parole sunt date ca date de intrare în program:
#ABd1234@1,a F1#,2w3E*,2We3345
#output
#ABd1234@1
#hints 
#În cazul în care datele de intrare sunt furnizate la întrebare, ar trebui să presupunem că este o intrare de consolă.

import re
value = []
items = [x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))

#metoda 2
def is_low(x):
    for i in x:
        if "a"<=i and i<='z':
            return True
    return False

def is_up(x):
    for i in x:
        if 'A'<=i and i<='Z':
            return True
    return False

def is_num(x):
    for i in x:
        if '0'<=i and i<='9':
            return True
    return False
def is_other(x):
    for i in x:
        if i=='$' or i=='#' or i=='@':
            return True
    return False

s = input().split(',')
l=[]
for i in s :
    length = len(i)
    if 6<=length and length<=12 and is_low(i) and is_up(i) and is_num(i) and is_other(i):
        l.append(i)
print(",".join(l))

#metoda 3

def check(x):
    cnt=(6<=len(x) and len(x)<=12)
    for i in x:
        if i.isupper():
            cnt+=1
            break
    for i in x:
        if i.islower():
            cnt+=1
            break
    for i in x:
        if i.isnumeric():
           cnt+=1
           break
    for i in x:
        if i=='@' or i=='#' or i=='$':
            cnt+=1
            break
    return cnt ==5

s= input().split(',')
l= filter(check, s)
print(",".join(l))

#metoda 4
import re

s = input().split()
l =[]
for i in s :
    cnt =0
    cnt+=(6<=len(i) and len(i)<=12)
    cnt+=bool(re.search("[a-z]",i))
    cnt+=bool(re.search('[A-Z]',i))
    cnt+=bool(re.search("[0-9]",i))
    cnt+=bool(re.search('[@#$]',i))
    if cnt ==5:
        l.append(i)
print(",".join(l))

#Vi se cere să scrieți un program pentru a sorta (numele, vârsta, scorul) tupluri crescând ordinea în care numele este șir, vârsta și punctajul sunt numere. Tuplurile sunt in
#troduse prin consolă. Criteriile de sortare sunt:

#1: Sortare în funcție de nume
#2: apoi sortați în funcție de vârstă
#3: apoi sortați după scor
#Prioritatea este că numele> vârsta> punctajul.

#Dacă sunt introduse următoarele programe drept intrare pentru program:
#Tom,19,80
#John,20,90
#Jony,17,91
#Jony,17,93
#Json,21,85
#output:
#[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
#Hints:
#În cazul în care datele de intrare sunt furnizate la întrebare, ar trebui să presupunem că este o intrare de consolă.
# Folosim elementgetter pentru a activa mai multe taste de sortare.

from operator import itemgetter

l=[]
while True:
    s=input()
    if not s:
        break
    l.append(tuple(s.split(',')))
print(sorted(l,key=itemgetter(0,1,2)))

#metoda 2
l=[]
while True:
    s=input().split(',')
    if not s[0]:
        break
    l.append(tuple(s))
l.sort(key= lambda x:(x[0],x[1],x[2]))
print(l)
