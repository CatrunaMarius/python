
#Vă rugăm să scrieți un program care să numere și să imprime numerele fiecărui personaj într-un șir de intrare de către consolă.

#Exemplu: Dacă următorul șir este dat ca intrare în program:

#abcdefgabc
#Apoi, rezultatul programului ar trebui să fie:

#o, 2
#c, 2
#b, 2
#e, 1
#d, 1
#g, 1
#f, 1
#sugestii
#Utilizați dict pentru a stoca perechi de cheie / valoare. Utilizați metoda dict.get () pentru a căuta o cheie cu valoare implicită.

dic = {}
s = input()

for s in s:
    dic[s] = dic.get(s,0)+1
print("\n".join(['%s,%s' %(k,v) for k,v in dic.items()]))

#metoda 2
import string
s = input()
for letter in string.ascii_lowercase:
    cnt=s.count(letter)
    if cnt>0:
        print("{},{}".format(letter, cnt))

#metoda 3
s=input()
for letter in range(ord('a'), ord('z')+1):
    letter = chr(letter)
    cnt = s.count(letter)
    if cnt>0:
        print("{},{}".format(letter,cnt))

#Problema 2
#Vă rugăm să scrieți un program care acceptă un string din consolă și să îl imprimați în ordine inversă.

#Exemplu: Dacă următorul string este dat ca intrare în program: *

#rise to vote sir
#Apoi, rezultatul programului ar trebui să fie:

#ris etov ot esir
#sugestii
#Folosiți lista [:: - 1] pentru a itera o listă într-o ordine inversă.

s=input()
s= s[::-1]
print(s)

#metoda 2
s=input()
s=''.join(reversed(s))
print(s)

#Problema 3
#Vă rugăm să scrieți un program care acceptă un string din consolă și să imprimați caracterele care au chiar și indexuri.

#Exemplu: Dacă următorul șir este dat ca intrare în program:

#H1e2l3l4o5w6o7r8l9d
#Apoi, rezultatul programului ar trebui să fie:

#Helloworld
#sugestii
#Utilizați lista [:: 2] pentru a itera o listă cu pasul 2.
s=input()
s=s[::2]
print(s)

s= "H1e2l3l4o5w6o7r8l9d"
s=[s[i] for i in range(len(s)) if i%2 ==0]
print(''.join(s))

#metoda 2
s="H1e2l3l4o5w6o7r8l9d"
ns=''
for i in range(len(s)):
    if i %2 ==0:
        ns+=s[i]
print(ns)

#Programul 4
#Vă rugăm să scrieți un program care tipărește toate permutările de [1,2,3]

#sugestii
#Utilizați itertools.permutations () pentru a obține permutările listei.

import itertools
print(list(itertools.permutations([1,2,3])))

#Programul 5
#Scrieți un program pentru a rezolva un puzzle clasic chinez antic: Numărăm 35 de capete și 94 de picioare printre puii și iepurii dintr-o fermă. Câți iepuri și câți pui avem?

#sugestii
#Utilizați bucla pentru a itera toate soluțiile posibile.

def solve(numhead, numlegs):
    ns='No solutions!'
    for i in range(numhead+1):
        j=numheads-1
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads=35
numlegs=94
solutions = solve(numheads,numlegs)
print(solutions)

