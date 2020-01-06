
#Sample Input

#3 1000
#2 5 4
#3 7 8 9 
#5 5 7 8 9 10 
#Sample Output

#206

from itertools import *


K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))

#explicatii N = (list(map(int, input().split()))[1:] for _ in range(K))
#N = []
#for _ in range(k):
#    # Get input and split into list
#    l = input().split()

#    # Turn list  of strings into list of integers
#    l = list(map(int, l))

#    # Remove index [0] using a slice
#    l = l[1:]
		
#    # Build list of lists
#    N.append(l)    

#metoda 2
from itertools import product
K, M = input().split()
List = []
Temp = []
for i in range(int(K)):
    List.append([i**2 for i in list(map(int,input().split()))][1:])

Max = 0
for i in list(product(*List)):
    if sum(i)%int(M) > Max:
        Max = sum(i)%int(M)

print(Max)