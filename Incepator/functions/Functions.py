#The function returns the average of two arguments

def average(n1, n2):
    m=(n1+n2)/2
    return m
a=int(input("A = "))
b =int(input("B = "))

avrg = average(a, b)
print(round(avrg,2))