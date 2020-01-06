

#start () & end ()
#Aceste expresii returnează indicii de la începutul și sfârșitul subcentrului asortat de grup.

#Code

#import re
#m = re.search(r'\d+','1234')
#m.end()
#4
#m.start()
#0


#Sarcină
#Vi se dă un string S.
#Sarcina dvs. este de a găsi indicii de început și sfârșit de șir k în S.

#Formatul de intrare

#Prima linie conține șirul S.
#A doua linie conține șirul k.

#Format de iesire

#Tipăriți tuple-ul în acest format: (start _index, end _index).
#Dacă nu se găsește nicio potrivire, imprimați (-1, -1).

#Sample Input

#aaadaa
#aa
#Sample Output

#(0, 1)  
#(1, 2)
#(4, 5)
import re

S = input()
k = input()

pattern = re.compile(k)
r = pattern.search(S)
if not r: print ("(-1, -1)")
while r:
    print ("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(S,r.start() + 1)



#metoda 2
s = input()
k = input()
index = 0

if re.search(k, s):
    while index+len(k) < len(s):
        m = re.search(k, s[index:]) #begins search with new index
        
        print("({0}, {1})".format(index+m.start(), index+m.end()-1)) 
        
        index += m.start() + 1 #assign new index by +1 
else:
    print((-1, -1))

#metoda 3
import re
s, k = input(), input()
matches = list(re.finditer(r'(?={})'.format(k), s))
if matches:
    print('\n'.join(str((match.start(),
          match.start() + len(k) - 1)) for match in matches))
else:
    print('(-1, -1)')

#metoda 4


s = input()
k = input()
if k in s:
    print(*[(i.start(), (i.start()+len(k)-1)) for i in re.finditer(r'(?={})'.format(k), s)], sep='\n')
else:
    print('(-1, -1)')

#metoda 5

s = input()
v = input()
for i,x in enumerate(s):
    if re.match(v,s[i:]):
        print((i,i+len(v)-1))
if re.search(v, s)==None:
    print((-1,-1))  