#Read the data from a file to a dictionary
products = {}

for i in open("goods.txt"):
    row = i.split()
    row[1] = float(row[1])
    row[2] = int(row[2])
    products[row[0]] = row[1:]
print(products)
