#Sample Input

#3
#4
#5
#Sample Output

#81
#1

#metoda 1
#a,b,m = int(input()), int(input()), int(input())
#print(pow(a,b))
#print(pow(a,b,m))

#metoda 2
a,b,m = [int(input()) for _ in '123']
print(pow(a,b),pow(a,b,m),sep='\n')

#metoda 3
a,b,m=[int(input())for _ in range(3)]
print(pow(a,b),pow(a,b,m),sep='\n')