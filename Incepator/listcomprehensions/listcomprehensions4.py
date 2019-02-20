#Unpacking a matrix into an one-level list
a = [[1, 2, 3], [6, 5, 4],[7, 8, 9]]
b = [item for row in a for item in row]
print(b)
