
#Tu și Fredrick sunteți prieteni buni. Ieri, Fredrick a primit N carduri de credit de la ABCD Bank. Vrea să verifice dacă numerele cardului său de credit sunt valabile sau nu. Se întâmplă să fii grozav la regex, așa că îți cere ajutorul!

#Un card de credit valabil de la ABCD Bank are următoarele caracteristici:

#► Trebuie să înceapă cu un 4,5 sau 6.
#► Trebuie să conțină exact 16 cifre.
#► Trebuie să fie format doar din cifre (0-9).
#► Poate avea cifre în grupuri de 4, separate printr-o cratima "-".
#► NU trebuie să folosească niciun alt separator precum '', '_' etc.
#► NU trebuie să aibă 4 sau mai multe cifre repetate consecutive.

#Examples:

#Valid Credit Card Numbers

#4253625879615786
#4424424424442444
#5122-2368-7954-3214
#Invalid Credit Card Numbers

#42536258796157867       #17 digits in card number → Invalid 
#4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
#5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
#44244x4424442444        #Contains non digit characters → Invalid
#0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid


#Formatul de intrare

#Prima linie de intrare conține un număr întreg N.
#Următoarele N linii conțin numere de card de credit.

#Format de iesire

#Tipăriți „Valid” dacă numărul cardului de credit este valid. În caz contrar, imprimați „Invalid”. Nu imprimați ghilimelele.

#Sample Input

#6
#4123456789123456
#5123-4567-8912-3456
#61234-567-8912-3456
#4123356789123456
#5133-3367-8912-3456
#5123 - 3567 - 8912 - 3456
#Sample Output

#Valid
#Valid
#Invalid
#Valid
#Invalid
#Invalid
#Explanation

#4123456789123456 : Valid
#5123-4567-8912-3456 : Valid
#61234-567-8912-3456 : Invalid, because the card number is not divided into equal groups of 4.
#4123356789123456 : Valid
#5133-6733-8912-3456 : Invalid, consecutive digits 3333 is repeating 4 times.
#5123 -- 4567 -- 8912 -- 3456 : Invalid, because space '  ' and - are used as separators.

import re
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for _ in range(int(input().strip())):
    print("Valid" if TESTER.search(input().strip()) else "Invalid")




#metoda 2
import re


for _ in range(int(input())):
    s = input()

    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s) and not re.search(r"([\d])\1\1\1", s.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")

#metoda 3

import re

for _ in range(int(input())):
    n = input().strip()
    try:
        assert re.match(r'(\d{4}-){3}\d{4}$', n) or re.match(r'\d{16}$', n)
        n = re.sub(r'-', '', n)
        assert re.match(r'[456]', n)
        assert not re.search(r'(\d)\1{3,}', n)
    except:
        print('Invalid')
    else:
        print('Valid')