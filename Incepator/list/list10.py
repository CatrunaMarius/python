#Find the longest sequence that is ordered in ascending order

from random import random

n=10
lst = [0] *n
for i in range(n):
    lst[i] =int(random()*50)
print(lst)

max_length =1
current_length = 1
id_end = 0

for i in range(1, n):
    if lst[i]>lst[i-1]:
        current_length +=1
    else:
        if current_length > max_length:
            max_length=current_length
            id_end =i
        current_length =1

print(max_length)
print(lst[id_end - max_length : id_end])


