#Separate positive numbers from negative
from random import random

a=[]
for i in range(7):
    n =int(random()*20)-10# '20' si '10' arata max si min axei arry. cel care urmeaza dupa * trebuie sa feie >ca cel dupa ) afle vor apare numai numere negative
    a.append(n)

print(a)

neg = []
pos = []

for i in a:
    if i<0:
        neg.append(i)
    elif i >0:
        pos.append(i)

print(neg)
print(pos)