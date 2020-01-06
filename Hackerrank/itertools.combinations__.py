#Sample Input

#HACK 2
#Sample Output

#A
#C
#H
#K
#AC
#AH
#AK
#CH
#CK
#HK

from itertools import *

s,k = input().split()

for l in range(1,int(k)+1):
    for c in combinations (sorted(s),l):
        print(''.join(c))

#metoda 2 
#s, k = input().split()

#[print("".join(i)) for x in range(1, int(k)+1) for i in combinations(sorted(s), x)]

#metoda 3
#s, k = input().split()
#for size in range(int(k)):
#    print(*map(''.join, combinations(sorted(s),size +1)),sep = '\n') 

#metoda 4
#s = input().split()
#string, number = sorted(s[0]), int(s[1])
#for i in range(1, number + 1):
    #print(*list(map(''.join, combinations(string, i))), sep='\n')



#metoda 5
#s,k = map(str, input().split())

#for i in range(1,int(k)+1):
#    l = list()
#    if i > 1:
#        print()
#    for j in combinations(sorted(s),i):
#        l.append("".join(j))
#    print(*l, sep="\n",end="")