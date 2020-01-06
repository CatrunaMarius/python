
#A valid postal code P have to fullfil both below requirements:

#1.P must be a number in the range  from 100000  to 999999  inclusive.
# 2.P must not contain more than one alternating repetitive digit pair.
#Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

#For example:
#    121426 # Here, 1 is an alternating repetitive digit.
#    523563 # Here, NO digit is an alternating repetitive digit.
#    552523 # Here, both 2 and 5 are alternating repetitive digits.

#Sarcina dvs. este să oferiți două expresii obișnuite regex_integer_in_range și regex_alternating_repetitive_digit_pair. Unde:

#regex_integer_in_range ar trebui să se potrivească numai cu numere întregi cuprinse între 100000 și 999999 inclusiv

#regex_alternating_repetitive_digit_pair ar trebui să găsească perechi de cifre repetitive alternante într-un șir dat.

#Ambele expresii obișnuite vor fi utilizate de șablonul de cod furnizat pentru a verifica dacă șirul de intrare este un cod poștal valid folosind următoarea expresie:

#(bool(re.match(regex_integer_in_range, P)) 
#and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#Formatul de intrare

#Codul stub blocat în editor citeste un singur șir care notează P de la stdin și folosește expresia furnizată și expresiile dvs. obișnuite pentru a valida dacă P este un cod poștal valid.

#Format de iesire

#Nu sunteți responsabil pentru imprimarea nimicului în stdout. Blocat cod ciot în editorul face asta.

#Output Format

#You are not responsible for printing anything to stdout. Locked stub code in the editor does that.

#Sample Input 0

#110000
#Sample Output 0

#False


#Explicație 0

#1 1 0000: (0, 0) și (0, 0) sunt două perechi alternantă cifre. Prin urmare, este un cod poștal nevalid.

#Notă:
#Un punctaj 0 din va fi acordat pentru utilizarea condițiilor „dacă” din codul dvs.
#Trebuie să treci toate testele pentru a obține un scor pozitiv.

regex_integer_in_range = r"[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#metoda 2

import re
s=input()
print (bool(re.match(r'^[1-9][\d]{5}$',s) and len(re.findall(r'(\d)(?=\d\1)',s))<2 ))

#metoda 3
import re

print(bool(re.match(
    r'^'
    r'(?!.*(.).\1.*(.).\2)'
    r'(?!.*(.)(.)\3\4)'
    r'[1-9]\d{5}'
    r'$', input()
)))

#metoda 4
s = input()
print(s.isdigit() and 100000 <= int(s) <= 999999 and 
      sum([s[i] == s[i+2] for i in range(0, 4)]) < 2)