

#Un brand multinațional deschis recent a decis să își bazeze logo-ul companiei pe cele mai comune trei caractere din numele companiei. 
#Acum încearcă diverse combinații de nume de firme și logo-uri pe baza acestei condiții.
# Având în vedere un șir de caractere, care este numele companiei cu litere mici, sarcina dvs. este de a găsi cele mai comune trei caractere din șir.

#Tipăriți cele mai comune trei caractere împreună cu numărul de apariții.
#Sortează în ordinea descrescătoare a numărului de apariții.
#Dacă numărul de evenimente este același, sortați caracterele în ordine alfabetică.
#De exemplu, în conformitate cu condițiile descrise mai sus,
#GOOGLE
# ar avea sigla lui cu literele G, O, E.

#Formatul de intrare

#O singură linie de intrare care conține șirul S.

#Format de iesire

#Tipăriți cele mai frecvente trei caractere împreună cu numărul de apariții ale acestora pe o linie separată.
#Sortează ieșirea în ordinea descrescătoare a numărului de apariții.
#Dacă numărul de evenimente este același, sortați caracterele în ordine alfabetică.

#Sample Input 0

#aabbbccde
#Sample Output 0

#b 3
#a 2
#c 2


#metoda 1
print("=== metoda 1 ===")
s = input()
ans =[]
		
for i in set(s):
    ans.append((i,s.count(i)))
					
list.sort(ans, key=lambda x:(x[1],-ord(x[0])), reverse=True)
		
for x in range(3):
    print(ans[x][0], ans[x][1])

#metoda 2
print("=== metoda 2 ===")
from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]

#metoda 3
print("=== metoda 3 ===")
from itertools import groupby
print(*[char+" "+str(num) for num,char in sorted(sorted([(len(list(v)),k) for k, v in groupby(sorted(input()))],key=lambda x: x[1]),key=lambda x: x[0],reverse=True)][:3], sep='\n')

#metoda 4
print("=== metoda 4 ===")
from operator import itemgetter

chars = list(input())
d = [[c,chars.count(c)] for c in set(chars)]
d.sort(key=itemgetter(0))
d.sort(key=itemgetter(1), reverse=True)
for i in d[:3]:
    print("{0} {1}".format(i[0], i[1]))



#metoda 5
print("=== metoda 5 ===")
from itertools import groupby

s = sorted(input())
lst = [(c,len(list(cgen))) for c,cgen in groupby(s)]
list.sort(lst,key = lambda x:((x[1]), -ord(x[0])),reverse = True)
for x in range(3):
        print(lst[x][0], lst[x][1])

#metoda 6
print("=== metoda 6 ===")
from collections import Counter

s = input().strip()
c = Counter(s)
print(type(c))
for element in sorted(c.items(), key=lambda x: (-x[1], x[0]))[:3]:
    print(" ".join(str(e) for e in element), sep=" ")