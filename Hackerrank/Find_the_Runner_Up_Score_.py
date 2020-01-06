

#Având în vedere foaia de participare a participanților pentru Ziua Sportului Universitar, vi se cere să găsiți scorul de alergător.
# Vi se acordă n scoruri. Stocați-le într-o listă și găsiți scorul de al doilea.

#Format de intrare

#Prima linie conține n. A doua linie conține un tablou A [] de n numere întregi separate fiecare de un spațiu.

#Sample Input 0

#5
#2 3 6 6 5
#Sample Output 0

#5


#Explicație 0

#Lista dată este [2,3,6,6,5]. Scorul maxim este 6, al doilea maxim este de 5. Prin urmare, vom tipări 5 ca punctaj al doilea.

#i = int(input())
#lis = list(map(int,input().strip().split()))[:i]
#z = max(lis)
#while max(lis) == z:
#    lis.remove(max(lis))

#print (max(lis))
#metoda 2
n = int(input())
arr = list(map(int, input().split()))
print(arr)
l = max(arr)
for i in range(n):
    if largest == max(arr):
       arr.remove(max(arr))
#print(arr)

print(max(arr))