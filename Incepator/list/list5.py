#Replacinf list items

array = [10, -15, 3, 8, 0, 9, -6]
print(array)

for i in range(len(array)):
    if array[i] >0:
        array[i]=1
    elif array[i]<0:
        array[i]=-1

print(array)
