#Fillin a matrix with random numbers

from random import randint

n = 5
m = 10
a = []

for i in range(n):
    b=[]
    for j in range(m):
        b.append(randint(1,99))
    a.append(b)

for i in a:
    for j in i:
        print("%3d" %j, end=' ')
    print()

#or
#for i in range(n):
#    for j in range(m):
#        print("%3d" % a[i][j], endl=' ')
#    print()