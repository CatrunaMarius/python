#output the items that are larger than the arithmetic meam of the array

from random import randint

n=10
a=[]
sum=0

for i in range(n):
    a.append(randint(0,9))
    print(a[i], end=' ')
    sum += a[i]
print()

average =sum/n
print("the average: %.2f" %average)

for i in a:
    if i> average:
        print(i, end=' ')
print()

