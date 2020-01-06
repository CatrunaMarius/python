

#Există un rând orizontal de cuburi. Lungimea fiecărui cub este dată. Trebuie să creați o nouă grămadă verticală de cuburi. Noua grămadă ar trebui să urmeze aceste indicații: dacă cubei este deasupra cubejului, atunci sideLengthj> = sideLengthi.

#Atunci când stivați cuburile, puteți ridica de fiecare dată doar cel mai din stânga sau cel din dreapta. Imprimați „Da” dacă este posibil să stivați cuburile. În caz contrar, imprimați „Nu”. Nu imprimați ghilimelele.

#Formatul de intrare

#Prima linie conține un singur număr întreg T, numărul de cazuri de testare.
#Pentru fiecare caz de test, există 2 linii.
#Prima linie a fiecărui caz de test conține n, numărul de cuburi.
#A doua linie conține n numere întregi separate de spațiu, indicând lungimile laterale ale fiecărui cub în ordinea respectivă.

#Sample Input

#2
#6
#4 3 2 1 3 4
#3
#1 3 2
#Sample Output

#Yes
#No

#metoda 1 pt incepatori
print("=== metoda 1 ===")
for t in range(int(input())):
    l = int(input())
    lst = list(map(int, input().split()))
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    print("Yes" if i == l - 1 else "No")

#metoda 2 pt incepatori
print("=== metoda 2 ===")
for t in range(int(input())):
    input()
    lst = [int(i) for i in input().split()]
    min_list = lst.index(min(lst))
    left = lst[:min_list]
    right = lst[min_list+1:]
    if left == sorted(left,reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")

#metoda 3
print("=== metoda 3 ===")
from collections import *
for _ in (range(int(input()))):
    input()
    side_lengths = deque(map(int, input().strip().split()))
    result = "Yes"
    if max(side_lengths) not in (side_lengths[0], side_lengths[-1]):
        result = "No"
    print(result)

#metoda 4
print("=== metoda 4 ===")
from collections import *
for i in range(int(input())):
    n = int(input())
    d = deque()
    d.extend(map(int,input().strip().split()))
    t = 'Yes'
    while True:
        if d == deque([]):
            break
        elif max(d) == d[0] or max(d) == d[-1]:
            d.remove(max(d))
        else:
            t = 'No'
            break
    print(t)


#metoda 5
print("=== metoda 5 ===")
for _ in range(int(input())): 
    m, l = int(input()), [int(x) for x in input().split()]
    left = True
    valid = True
    
    for x in range(1,m):
        if left:
            if l[x] > l[x-1]:
                left = False
        else:
            if l[x] < l[x-1]:
                valid = False
    
    print("Yes" if valid else "No")