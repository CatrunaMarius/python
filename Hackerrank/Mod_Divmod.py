
#Sample Input

#177
#10
#Sample Output

#17
#7
#(17, 7)


#metoda 1
#a = int(input())
#b = int(input())
#print(a//b)
#print(a%b)
#print(divmod(a,b))

#metoda 2
#print('{0}\n{1}\n({0}, {1})'.format(*divmod(int(input()), int(input()))))

#metoda 3
a, b = int(input()), int(input())
print("{d[0]}\n{d[1]}\n{d}".format(d=divmod(a, b)))