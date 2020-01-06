
#Vi se dă un șir și trebuie să validați dacă este un număr roman valid. Dacă este validă, imprimați True. În caz contrar, imprimați False. Încercați să creați o expresie obișnuită pentru un număr roman valid.

#Formatul de intrare

#O singură linie de intrare conținând un șir de caractere romane.

#Format de iesire

#Ieșiți o singură linie care conține True sau False conform instrucțiunilor de mai sus.

#Sample Input

#CDXXI
#Sample Output

#True

#Sample Input 2
#MMMDCCCLXXXXVIII
#Sample Output 2
#False
#metoda 1
regex_pattern = r"(?:M|MM|MMM)?(?:C|CC|CCC|CD|D|DC|DCC|DCCC|CM)?(?:X|XX|XXX|XL|L|LX|LXX|LXXX|XC)?(?:I|II|III|IV|V|VI|VII|VIII|IX)?$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

#metoda 2
import re

thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'
print (bool(re.match(thousand + hundred+ten+digit +'$', input())))

#metoda 3

x=input()
try:
    if (roman.fromRoman(x)>0 and roman.fromRoman(x)<4000):
        print("True")
    else:
        print("False")
except:
    print("False")