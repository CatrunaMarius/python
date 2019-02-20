#finding the minimum and maximum elements of an array

from random import randint

#n=7
n=int(input("Introdu un nr pt array: "))
a=[0] * n

for i in range(n):
    a[i] =randint(0, 100)
    print(a[i], end=' ')
print()

maximum =-1
minimum =101

for i in a:
    if i>maximum:
       maximum=i
    if i<minimum:
       minimum =i
#or use functions of Python
#maximum= max(a)
#minimum= min(a)

print("Maximum: ", maximum)
print("Minimum: ", minimum)