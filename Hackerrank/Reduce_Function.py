
#Fiind dată o listă de numere raționale, găsiți produsul lor.

#Concept
#Funcția reduce () aplică o funcție de două argumente cumulativ pe o listă de obiecte succesive de la stânga la dreapta pentru a o reduce la o valoare. Spuneți că aveți o listă, spuneți [1,2,3] și trebuie să găsiți suma acesteia.

#reduce(lambda x, y : x + y,[1,2,3])
#6

#De asemenea, puteți defini o valoare inițială. Dacă este specificată, funcția va asuma valoarea inițială ca valoare dată, apoi va reduce. Este echivalent cu adăugarea valorii inițiale la începutul listei. De exemplu:

#    >>> reduce(lambda x, y : x + y, [1,2,3], -3)
#3

#from fractions import gcd
#reduce(gcd, [2,4,8], 3)
#1

#Formatul de intrare

#Prima linie conține n, numărul de numere raționale.
#Ith din următoarele n linii conțin două numere întregi fiecare, numărătorul (Ni) și numitorul (Di) al numărului rațional ith din listă.

#Format de iesire

#Tipăriți o singură linie care conține numerotatorul și numitorul produsului numerelor din listă în forma sa cea mai simplă, adică numărătorul și numitorul nu au un divizor comun decât 1.

#Sample Input 0

#3
#1 2
#3 4
#10 6
#Sample Output 0

#5 8

from fractions import Fraction
from functools import reduce
import operator

def product(fracs):
    t = reduce(operator.mul , fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)


#metoda 2
def product(fracs):
    t = reduce(lambda x, y : x * y, fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

#metoda 3
def product(fracs):
    t = reduce(lambda fraction1,fraction2:fraction1* fraction2,fracs)
    return t.numerator, t.denominator

fracs=[]
for _ in range(int(input())):
     a,b=input().split()
     c=Fraction(int(a),int(b))
     fracs.append(c)

print(*product(fracs))
#metoda 4
from functools import reduce
from fractions import gcd

n = int(input())
rationals = []
for i in range(n):
    rationals.append(list(map(int, input().split())))
s = [list(a) for a in zip(*rationals)]
print(s)
k = [reduce(lambda x, y: x*y, s[i]) for i in range(2)]
c = reduce(gcd, k)
for i in range(2):
    k[i] //= c
print(*k)




#metoda 5
n = int(input())
top = list()
bottom = list()
for i in range(n):
    m = list(map(int, input().split()))
    top.append(m[0])
    bottom.append(m[1])
numerator = reduce(lambda x, y: x * y, top)
denominator = reduce(lambda x, y: x * y, bottom)
g_cd = reduce(gcd, [numerator, denominator])
print(int(numerator / g_cd), int(denominator / g_cd))