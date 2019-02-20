#Determine the number of digit of an integer
n=int(input())
n=abs(n)

count =1
n//=10
while n>0:
    n//=10
    count +=1
print(count)
