
#Task

#You are given a string S.
#Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
#Sample Input

#HACK 2
#Sample Output

#AC
#AH
#AK
#CA
#CH
#CK
#HA
#HC
#HK
#KA
#KC
#KH

from itertools import permutations

s,k = input().split()
print(*[''.join(i) for i in permutations(sorted(s), int(k) )], sep = '\n')

#metoda 2
a, b = input().split()
[print(''.join(i)) for i in permutations(sorted(a), int(b))]

#metoda 3
a, b = input().split()
for c in permutations(sorted(a), int(b)):
    print(''.join(c))
