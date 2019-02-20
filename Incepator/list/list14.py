#binary search.Find a number in a ordered array

from random import random

n=20
array = []

for i in range(n):
    array.append(int(random()*100))
array.sort()
print(array)

number = int(input())

low =0
high = n-1
while low <= high:
    mid = (low +high) //2
    if number <array[mid]:
        high =mid-1
    elif number >array[mid]:
        low =mid +1
    else:
        print("ID=", mid)
        break
else:
    print("no the number")
