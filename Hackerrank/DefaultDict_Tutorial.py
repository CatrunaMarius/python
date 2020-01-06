

#Formatul de intrare

#Prima linie conține numere întregi, n și m separate de un spațiu.
#Următoarele n linii conțin cuvintele aparținând grupului A.
#Următoarele linii m conțin cuvintele aparținând grupului B.

#Format de iesire

#Ieșiri m linii.
#Linia ith trebuie să conțină pozițiile 1-indexate ale aparițiilor cuvântului ith separate prin spații.

#Sample Input

#5 2
#a
#a
#b
#a
#b
#a
#b
#Sample Output

#1 2 4
#3 5

from collections import defaultdict
#metoda 1
n, m = map(int, input().split())

d = defaultdict(list)
for i in range(n):
        d[input()].append(i + 1)


for i in range(m):
        print (*d.get(input(), [-1]))

#metoda 2
#n, m = map(int, input().split())
#d = defaultdict(lambda: -1)

#for i in range(1, n+1): 
#    word = input()
#    d[word] = d[word] + ' ' + str(i) if word in d else str(i)

#for _ in range(m):
#    print(d[input()]) 

#metoda 3
#d, n = defaultdict(list), list(map(int, input().split()))

#for i in range(n[0]):
#    d[input()].append(i + 1)

#for i in range(n[1]):
#    print(' '.join(map(str, d[input()])) or -1)

#metoda 4
#inputs = input().split()
#group_A = defaultdict(list)
#group_B = defaultdict(list)

#n = inputs[0]
#m = inputs[1]

#for index_1 in range(1, int(n)+1):
#    value = input().strip()
#    group_A[value].append(str(index_1))

#for index_2 in range(1, int(m)+1):
#    value = input().strip()
#    group_B[value].append(str(index_2))
    
#collection = list(group_B.keys())
#collection.sort()

#for each in collection:
#    if each in group_A:
#        print(' '.join(group_A[each]))
#    else:
#        print(-1)

