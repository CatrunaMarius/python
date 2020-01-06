
#Compania ABCXYZ are până la 100 de angajați.
#Compania decide să creeze un număr de identificare unic (UID) pentru fiecare dintre angajații săi.
#Compania v-a atribuit sarcina de validare a tuturor UID-urilor generate aleatoriu.

#Un UID valid trebuie să respecte regulile de mai jos:

#Acesta trebuie să conțină cel puțin 2 caractere mari cu alfabet englezesc.
#Acesta trebuie să conțină cel puțin 3 cifre (0 - 9).
#Acesta trebuie să conțină numai caractere alfanumerice (a - z, A-Z și 0 - 9).
#Niciun personaj nu trebuie să repete.
#Trebuie să existe exact 10 caractere într-un UID valid.
#Formatul de intrare

#Prima linie conține un număr întreg T, numărul de cazuri de testare.
#Următoarele linii T conțin UID-ul unui angajat.

#Format de iesire

#Pentru fiecare caz de test, imprimați „Valid” dacă UID este valid. În caz contrar, imprimați „Invalid”, pe linii separate. Nu imprimați ghilimelele.

#Sample Input

#2
#B1CD102354
#B1CDEF2354
#Sample Output

#Invalid
#Valid
#Explanation

#B1CD102354: 1 is repeating → Invalid
#B1CDEF2354: Valid

import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')

#metoda 2
import re

def valid(s):
    if len(s) != 10:
        return 'Invalid'
    else:
        if  not re.search(r'.*[A-Z].*[A-Z].*', s):
            return 'Invalid' 
        if not re.search(r'.*\d.*\d.*\d.*', s):
            return 'Invalid' 
        if not re.search(r'[a-zA-Z\d]{10}', s):
            return 'Invalid'
        if re.search(r'(.).*\1', s):
            return 'Invalid'
        return 'Valid'

for _ in range(int(input())):
    s = input()
    print(valid(s))

#metoda 3
from collections import Counter
import string

def valid_string(s):
    strings = string.ascii_letters + string.digits + ',' + '&'

    if len(s)!=10:
        return False
    
    d_strings = Counter(s)
    
    cnt_A_Z = 0
    cnt_digits = 0

    for key, value in d_strings.items():
        if key not in strings or value != 1:
            return False
        
        if key in string.digits:
            cnt_digits += 1

        if key in string.ascii_uppercase:
            cnt_A_Z += 1

    if cnt_digits < 3 or cnt_A_Z < 2:
        return False
    
    return True

#metoda 4
import re
for _ in range(int(input())):
    s = input()
    print('Valid' if all([re.search(r, s) for r in [r'[A-Za-z0-9]{10}',r'([A-Z].*){2}',r'([0-9].*){3}']]) and not re.search(r'.*(.).*\1', s) else 'Invalid')

#metoda 5
import re

MATCH_UPPER = re.compile(r'[A-Z]')
MATCH_DIGIT = re.compile(r'\d')
MATCH_ALPHANUMERIC = re.compile(r'^[a-zA-Z0-9]+$')
MATCH_REPEAT_CHARACTERS = re.compile(r'^.*(.).*(\1).*$')
MATCH_LENGTH_10 = re.compile(r'^.{10}$')


def is_valid(uid):
    validators = [
        # it must contain at least 2 uppercase characters
        contains_match(MATCH_UPPER, count=2, op='>='),

        # it must contain at least 3 digits
        contains_match(MATCH_DIGIT, count=3, op='>='),

        # it should only contain alphanumeric characters
        contains_match(MATCH_ALPHANUMERIC),

        # no character should repeat
        contains_match(MATCH_REPEAT_CHARACTERS, count=0),

        # there must be exactly 10 characters
        contains_match(MATCH_LENGTH_10)
    ]
    return all(validator(uid) for validator in validators)


def contains_match(regex, count=1, op='=='):
    op_def = {
        '>=': lambda a, b: a >= b,
        '==': lambda a, b: a == b,
    }

    def validator(uid):
        op_compare = op_def[op]
        return op_compare(len(regex.findall(uid)), count)

    return validator


def main():
    from fileinput import input

    # get input
    uids = [line.rstrip() for line in input()]
    n = int(uids.pop(0))

    # for each uid ... print (In)Valid
    for i in range(n):
        uid = uids[i]
        print('Valid' if is_valid(uid) else 'Invalid')


if __name__ == '__main__':
    main()