
#Sarcină

#Vi se oferă o listă separată de spații întregi. Dacă toate numerele întregi sunt pozitive, trebuie să verificați dacă un număr întreg este un număr întreg palindromic.

#Formatul de intrare

#Prima linie conține un număr întreg N. N este numărul total de numere întregi din listă.
#A doua linie conține lista separată de spațiu cu N întregi.


#Print True dacă toate condițiile din declarația problemă sunt îndeplinite. În caz contrar, imprimați False.

#Sample Input 1

#5
#12 9 61 5 14 
#Sample Output 1

#True
#Sample Input 2
#6
#1 2 3 4 5 -9
#Sample Output 1
#False

#_, a =input(), list(map(int,input().split()))
#print(*a)

#metoda

#print ( all([ i > 0 for i in a]) and any( str(j) == str(j)[::-1] for j in a))




#metoda 
_, a =input(), input().split()
print(any([i==i[::-1] for i in a if all(["-" not in n for n in a])]))