
#Sarcină

# Raghu este proprietarul unui magazin de încălțăminte. Magazinul său are numărul X de pantofi.
#Are o listă care conține dimensiunea fiecărui pantof pe care îl are în magazinul său.
#Există un număr de N de clienți care sunt dispuși să plătească o sumă de bani doar dacă primesc pantoful de mărimea dorită.

#Sarcina ta este să calculezi câți bani câștiga Raghu.

#Formatul de intrare

#Prima linie conține X, numărul de încălțăminte.
#A doua linie conține lista separată de spațiu a tuturor mărimilor de pantofi din magazin.
#A treia linie conține N, numărul de clienți.
#Următoarele N linii conțin valorile spațiale separate de _shoe_size_ dorite de client și xi, prețul pantofului.

#Sample Input

#10
#2 3 4 5 6 8 7 6 5 18
#6
#6 55
#6 45
#6 55
#4 40
#18 60
#10 50
#Sample Output

#200
print("=== metoda 1 ===")
from collections import *
numShoes = int(input())
sizeShoes = Counter(map(int, input().split()))
numCos = int(input())
income = 0

for i in range(numCos):
    size,price = map(int, input().split())
    if sizeShoes[size]:
        income += price
        sizeShoes[size] -= 1
print(income)

#metoda 2
print("=== metoda 2 ===")
_, stock = input(), Counter(list(map(int,input().split())))
money = 0
for size, cost in [map(int, input().split()) 
                      for _ in range(int(input()))]:
    if stock[size]>0:
        stock[size]-=1
        money+=cost
print(money)

#metoda 3
print("=== metoda 3 ===")
n = int(input())
s = Counter(map(int,input().split()))
x = int(input())
total = []
for i in range(x):
    a,b = map(int,input().split())
    if s[a] > 0:
        total.append(b)
        s.subtract(Counter([a]))
print (sum(total))



#metoda 4
print("=== metoda 4 ===")
# imports
from collections import Counter

# get the inputs
x = int(input())
shoes = list(map(int, input().split()))
n = int(input())
requirements = []
for _ in range(n):
    item_required = list(map(int, input().split()))
    requirements.append(item_required)

# counter
counts = Counter(shoes)
money_earned = 0

# check whether item available and update the counter
for item in requirements:
    if(counts[item[0]] != 0):
        counts[item[0]] -= 1
        money_earned += item[1]

# print result
print(money_earned)

#metoda 5
print("=== metoda 5 ===") 
n=int(input())
size=list(map(int,input().split()))
n2=int(input())
p=[]
for _ in range(n2):
       p.append(list(map(int,input().split())))
i=0 
count=0
while(i<n2):
    if p[i][0] in size:
        count+=p[i][1]
        size.remove(p[i][0])
    i+=1
print(count)    

#metoda 6
print("=== metoda 6 ===")
_ = int(input())
l = list(map(int,input().split()))
tp = 0
for _ in range(int(input())):
    s,p=map(int,input().split())
    if s in l:
        tp += p
        l.pop(l.index(s))    
print(tp)