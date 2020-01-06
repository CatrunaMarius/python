

#grup()
#O expresie de grup () returnează unul sau mai multe subgrupuri ale meciului.
#import re
#m = re.match (r '(\ w +) @ (\ w +) \. (\ w +)', 'username@hackerrank.com')
#m.group (0) # Întregul meci
#'Username@hackerrank.com'
#m.group (1) # Primul subgrupa cu paranteze.
#'nume de utilizator'
#m.group (2) # Al doilea subgrup de paranteză.
#'Hackerrank'
#m.group (3) # Al treilea subgrupa cu paranteze.
#'Com'
#m.group (1,2,3) # Argumente multiple ne oferă un tuple.
#(„nume de utilizator”, „hackerrank”, „com”)

#grupuri ()
#O expresie grupuri () returnează un tuple care conține toate subgrupurile meciului.
#import re
#m = re.match (r '(\ w +) @ (\ w +) \. (\ w +)', 'username@hackerrank.com')
#m.grupuri ()
#(„nume de utilizator”, „hackerrank”, „com”)

#groupdict ()
#O expresie groupdict () returnează un dicționar care conține toate subgrupurile numite ale meciului, introduse cu cheie de numele subgrupului.
#m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
#m.groupdict()
#{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}

#Sarcină

#Vi se dă un șir de șiruri
#Sarcina ta este să găsești prima apariție a unui caracter alfanumeric în S (citit de la stânga la dreapta) care are repetări consecutive.

#Formatul de intrare

#O singură linie de intrare care conține șirul S.

#Format de iesire

#Tipăriți prima apariție a caracterului care se repetă. Dacă nu există caractere care se repetă, imprimați -1.

#Sample Input

#..12345678910111213141516171820212223
#Sample Output

#1

#Explicaţie

#.. este primul caracter care se repetă, dar nu este alfanumeric.
#1 este primul (de la stânga la dreapta) care repetă caracterul alfanumeric al șirului din substratul 111.

import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)

#metoda 2

m = re.findall(r"([A-Za-z0-9])\1+",input())
print(m[1])