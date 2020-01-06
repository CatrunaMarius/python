

#re.findall ()
#Expresia re.findall () returnează toate potrivirile care nu se suprapun din tipare într-un șir ca listă de șiruri.

#Code

#import re
#re.findall(r'\w','http://www.hackerrank.com/')
#['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

#re.finditer ()
#Expresia re.finditer () returnează un iterator care produce instanțe MatchObject peste toate meciurile care nu se suprapun pentru modelul re din șir.

#Code

#import re
#re.finditer(r'\w','http://www.hackerrank.com/')
#<callable-iterator object at 0x0266C790>
#map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
#['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

#Sarcină
#Vi se oferă un șir S. Este format din caractere, spații și simboluri alfanumerice (+, -).
#Sarcina dvs. este să găsiți toate subcărțile din S care conțin 2 sau mai multe vocale.
#De asemenea, aceste substraturi trebuie să fie cuprinse între 2 consoane și trebuie să conțină numai vocale.

#Notă :
#Vocalele sunt definite ca: AEIOU și aeiou.
#Consonantele sunt definite ca: QWRTYPSDFGHJKLZXCVBNM și qwrtypsdfghjklzxcvbnm.

#Formatul de intrare

#O singură linie de intrare conținând șirul S.

#Format de iesire

#Imprimați subteranele potrivite în ordinea lor de apariție pe linii separate.
#Dacă nu se găsește nicio potrivire, imprimați -1.

#Sample Input

#rabcdeefgyYhFjkIoomnpOeorteeeeet
#Sample Output

#ee
#Ioo
#Oeo
#eeeee

#Explicaţie

#ee este situat între consoana d și f.
#Ioo este situat între consoana k și m.
#Oeo este situat între consoana p și r.
#eeeee este situat între consoana t și t.

import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(),  re.I)
print('\n'.join(m or ['-1']))

#metoda 2
import re
s = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
print('\n'.join(a or ['-1']))

#metoda 3
import re

string=input()

pattern=re.compile(r'[^AEIOUaeiou][AEIOUaeiou]{2,}[^AEIOUaeiou]')

matches=pattern.findall(string)

if not matches:
    print ("-1")

for i in range(len(matches)):
    print (matches[i][1:-1])


#metoda 4
import re 
S = str(input(""))
l = re.findall(r'([aeiouAEIOU]{2,})',S) 
if len(l) > 0:
    if (list(map(lambda x: x.group(), re.finditer(r'([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm.])',S[-1]))))!=[]:
        for i in l: 
            print(i)           
    else:
        for j in range(len(l)-1): 
            print(l[j])     
else: 
    print(-1)
