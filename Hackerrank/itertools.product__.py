
#Input Format

#The first line contains the space separated elements of list .
#The second line contains the space separated elements of list .

#Both lists have no duplicate integer elements.
#Output the space separated tuples of the cartesian product.

#Sample Input

# 1 2
# 3 4
#Sample Output

# (1, 3) (1, 4) (2, 3) (2, 4)

from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))

#metoda 2
import itertools

A = [int(x) for x in input().split()]
B = [int(y) for y in input().split()]

print(*itertools.product(A, B))