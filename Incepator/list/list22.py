#Sorting columns by incresing the items of the first row

from random import randint

m=5
n=3
matrix =[]
for i in range(n):
    row =[]
    for j in range(m):
        row.append(randint(10,99))
    matrix.append(row)

for i in matrix:
    print(i)
print()

k=m-1
while k >0:
    ind =0
    for j in range(1, k+1):
        if matrix[0][j]>matrix[0][ind]:
            ind = j
    for i in range(n):
        b=matrix[i][ind]
        matrix[i][ind] = matrix[i][k]
        matrix[i][k] =b
    k -= 1
for i in matrix:
    print(i)

