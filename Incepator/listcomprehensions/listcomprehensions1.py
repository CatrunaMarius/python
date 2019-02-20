#fillind with random numbers
from random import randint
low = int(input("Entre min: "))
high = int(input("Entre max: "))

a= [randint(low, high) for i in range(10)]

print(a)