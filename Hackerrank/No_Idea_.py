
#Există o serie de numere întregi. 
#Există, de asemenea, 2 seturi disjuncte, A și B, fiecare conținând numere întregi. 
#Îți plac toate numerele întregi din setul A și îți place toate numerele întregi din setul B. 
#Fericirea dvs. inițială este 0. Pentru fiecare i număr întreg din tablou, dacă i = A, adăugați 1 la fericirea voastră. 
#Dacă i = B, adaugi -1 la fericirea ta. Altfel, fericirea ta nu se schimbă. Ieșiți fericirea finală la sfârșit.

#Sample Input

#3 2
#1 5 3
#3 1
#5 7
#Sample Output

#1
#metoda 1
#n, m = input().split()
#arr = [int(x) for x in input().split()]
#A = set([int(y) for y in input().split()])
#B = set([int(z) for z in input().split()])
#count = [0 + 1 if x in A else 0-1 if x in B else 0 + 0 for x in arr]
#print(sum(count))

#metoda 2
#n,m=map(int,input().split())
#l=input().split(' ')
#A=set(input().split(' '))
#B=set(input().split(' '))
#happiness=0

#for i in l:
#    if i in A:
#        happiness+=1
#    if i in B:
#        happiness-=1
#print(happiness)

#metoda 3
#_, n, a, b = [input().strip().split() for i in range(4)]
#a, b = set(a), set(b)
#print(sum([(i in a) - (i in b) for i in n]))  

#metoda 4
def read_ints(): return map(int, input().split())
_, nums, A, B = read_ints(), list(read_ints()), set(read_ints()), set(read_ints())
print(sum((i in A) - (i in B) for i in nums))