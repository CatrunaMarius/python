
#Sarcină

#Vi se oferă un polinom P al unei singure indeterminate (sau variabile), x.
#Vi se oferă și valorile x și k. Sarcina dvs. este de a verifica dacă P (x) = k.

#Constrângerile
#Toți coeficienții polinomului P sunt numere întregi.
#x și y sunt de asemenea numere întregi.

#Formatul de intrare

#Prima linie conține valorile spațiale separate de x și k.
#A doua linie conține polinomul P.

#Format de iesire

#Print True dacă P (x) = k. În caz contrar, imprimați False.

#Sample Input

#1 4
#x**3 + x**2 + x + 1
#Sample Output

#True

x, k = map(int, input().split())

print(eval(input())== k)