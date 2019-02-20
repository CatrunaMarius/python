#How many odd and even numbers is the list?
from random import random
a=[]
for i in range(7):
    n=int(random()*100)
    a.append(n)

print(a)

even=0
odd=0

for i in a:
    if i % 2 ==0:
        even +=1
    else:
        odd +=1

print("Even: ", even)
print("Odd: ", odd)

#[69, 63, 42, 11, 35, 21, 58]
#Even:  2 / 58/2 and 42/2
#Odd:  5