#Which rows and columns of the matrix contains the element?

from random import random

n=6
m=5
matrix=[]
for i in range(n):
    row=[]
    for j in range(m):
        row.append(int(random()*40)+10)
    matrix.append(row)

for row in matrix:
    print(row)

item = int(input("Number range(10,50): "))

print("Rows (index):", end=" ")
for i in range(n):
    if item in matrix[i]:
        print(i, end=" ")
print()

print("Columns (index):", end=" ")
for j in range(m):
    for i in range(n):
        if matrix[i][j] == item:
            print(j, end=" ")
            break
print()