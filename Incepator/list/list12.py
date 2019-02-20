#Bubble sort

from random import randint

n = 7
a = []

for i in range(n):
    a.append(randint(1,20))
print(a)

for i in range(n-1):
    for j in range(n-i-1):
        if a [j]> a[j+1]:
            b=a[j]
            a[j] = a[j+1]
            a[j+1] = b
print(a)