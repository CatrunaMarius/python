#How to create a dictionary from two list?

a = [1, 2, 3, 4, 5]
b = ['a','b', 'c', 'd', 'e' ]

c = {}
for i in range(len(a)):
    c[b[i]] = a[i]
#or just
#c = dict(zip(b,a))

print(c)