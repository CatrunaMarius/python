#Exchange values of the principal and secondary diagonals of a square matrix

from random import randint

n =5
matrix = []
for i in range(n):
    row=[]
    for j in range(n):
        row.append(randint(1, 99))
        print("%4d" % row[j], end=' ')
    matrix.append(row)
    print()
print()

for i in range(n):
    b = matrix[i][i]
    matrix[i][i] = matrix[i][n-1-i]
    matrix[i][n-1-i] = b

for i in matrix:
    for j in i:
        print("%4d" % j, end=' ')
    print()
