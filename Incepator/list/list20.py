#The sum of the elements of the diagonals of a matrix

from random import random

n=5
matrix=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(random()*10))
    matrix.append(row)

for row in matrix:
    print(row)

sumMain =0
sumSecondary =0
for i in range(n):
    sumMain += matrix[i][i]
    sumSecondary =+ matrix[i][n-i-1]

print(sumMain)
print(sumSecondary)
