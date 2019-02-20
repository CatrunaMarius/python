#the sums of the items in the rows and columns of a matrix

from random import randint


m = 7
n = 5
matrix = []
row_sums = [0] * n
col_sums = [0] * m

for i in range(n):
    row =[]
    for j in range(m):
        row.append(randint(0,3))
    matrix.append(row)

for i in range(n):
    for j in range(m):
        row_sums[i] += matrix[i][j]
        col_sums[j] += matrix[i][j]

for i in range(n):
    print(matrix[i],"|",row_sums[i])

print('-' *m*4)
print(col_sums)
