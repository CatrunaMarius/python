
#filing an array with random numbers
from random import randint
#n=10
n=int(input("introdu un nr pt cat de lung sa fie array-ul: "))
array = []

for i in range(n):
    array.append(randint(1,99))

for i in array:
    print(i, end=' ')
print()