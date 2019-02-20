#A function that fills a list with numbers

from random import randint

def fill_list(lst, qty, low, high):
    for i in range(qty):
        lst.append(randint(low, high))

minimum = int(input("Min: "))
maximum = int(input("Max: "))
n = int(input("Quantity: "))
a = []

fill_list(a,n, minimum, maximum)

print(a)