#In the matrix, find the row and column with the maximum sums of elements

from random import  random #randit() iti trebuie initializati parametri pt a functiona

matrix = []

for i in range(5):
    row =[]
    for j in range(5):
        row.append(int(random()*10))
    matrix.append(row)

for row in matrix:
    print(row)

maxRow =0
idRow= 0
i=0
for row in matrix:
    if sum(row)>maxRow:
        maxRow = sum(row)
        idRow = i
    i += 1
print(idRow, '-', maxRow)

maxCol =0
idCol =0
for i in range(5):
    colsum =0
    for j in range(5):
        colsum += matrix[j][i]
    if colsum>maxCol:
        maxCol = colsum
        idCol = i

print(idCol, '-',maxCol)
