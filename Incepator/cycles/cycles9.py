#output of the N items of the series 1 -0.5,0.25,-0.125
n=input("Number of items: ")
n=int(n)

item=1

while n>0:
    print(item, end=' ')
    item = item / -2
    n-= 1
print()
