#functiom that calculates the arithmetic mean of list elements
def list_avrg(lst):
    l =len(lst)
    suma = 0
    for i in lst:
        suma +=i 
    return suma / l

print("Input integers: ")
a = input()
a = a.split()
for i in range(len(a)):
    a[i] = int(a[i])

avrg = list_avrg(a)

print("Avrage: ")
print(round(avrg, 2))