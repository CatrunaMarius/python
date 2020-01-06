
#Vi se oferă o foaie de calcul care conține o listă de N sportivi și detaliile acestora (cum ar fi vârsta, înălțimea, greutatea și așa mai departe).
# Vi se cere să sortați datele pe baza atributului Kth și să imprimați tabelul rezultat. 
# Urmați exemplul dat mai jos pentru o mai bună înțelegere.

#Rețineți că K este indexat de la 0 la M-1, unde M este numărul de atribute.

#Notă: Dacă două atribute sunt aceleași pentru rânduri diferite, de exemplu, dacă doi athete au aceeași vârstă, imprimați rândul care a apărut primul în intrare.

#Formatul de intrare

#Prima linie conține N și M separate de un spațiu.
#Următoarele N linii fiecare M conțin elemente.
#Ultima linie conține K.

#Format de iesire

#Tipăriți cele N linii ale tabelului sortat. Fiecare linie trebuie să conțină elemente separate de spațiu. Verificați eșantionul de mai jos pentru claritate.

#Sample Input 0

#5 3
#10 2 5
#7 1 0
#9 9 9
#1 23 12
#6 5 9
#1
#Sample Output 0

#7 1 0
#10 2 5
#6 5 9
#9 9 9
#1 23 12
#xplicație 0

#Detaliile sunt sortate pe baza celui de-al doilea atribut, deoarece K este indexat cu zero.

def athlete(arr, q):
    arr1 = sorted(arr,key=lambda x: x[q])
    for i in arr1:
        print(*i)

nm = input().split()

n = int(nm[0])

m = int(nm[1])

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

athlete(arr,k) 

#metoda 2
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    data = []
    for i in range(n):
        data.append(arr[i][k])

data = sorted(data)

for j in range(n):
    for i in range(n):
        if data[j] == arr[i][k]:
            print(*arr[i])

#metoda 3
n,m =map(int,input().split())
rows=[input()for _ in range(n)]
k = int(input())

for row in sorted(rows, key= lambda row: int(row.split()[k])):
    print(row)

#metoda 4
from operator import itemgetter
n,m = map(int, input().split())
lst = [[int(i)for i in input().split()] for _ in range(n)]
for i in sorted(lst, key=itemgetter(int(input()))):
    print(*i)