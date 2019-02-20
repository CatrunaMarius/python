#Find the maximum digi of a float number
#incearcal di nou
from random import random

num = round(random() * 1000, 3)
print(num)

strNum = str(num)

maxDigit = -1

for i in range(len(strNum)):
    if strNum[i] == '.':
        continue
    elif maxDigit < int(strNum[i]):
        maxDigit = int(strNum[i])

print(maxDigit)