#hackerrank.com
n = int(input())
#n%2 == 0 , 0 arata inceputul numaru impar
if n%2 == 0:
   

    if n in range(2,6):
        print("not weird")
    if n in range(6,21):
        print("Weird")
    if n>20:
        print("Not Weird")
else:
    print("weird")
