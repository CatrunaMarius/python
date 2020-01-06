
#Dat fiind 2 seturi de numere întregi, M și N, imprimați diferența lor simetrică în ordine crescătoare. 
#Termenul diferență simetrică indică acele valori care există fie în M, fie în N, dar nu există în ambele.

#Formatul de intrare

#Prima linie de intrare conține un număr întreg, M.
#A doua linie conține M numere întregi separate de spațiu.
#A treia linie conține un număr întreg, N.
#A patra linie conține N întregi separate de spațiu.

#Sample Input

#4
#2 4 5 9
#4
#2 4 11 12
#Sample Output

#5
#9
#11
#12



M,N = [set(input().split()) for _ in range(4)][1::2]
#print("\n".join(sorted(M.union(N)-M.intersection(N),key=int)))
print ('\n'.join(sorted(N^M, key=int)))

#metoda 2
a,b=(int(input()),input().split())
c,d=(int(input()),input().split())
x=set(b)
y=set(d)
p=y.difference(x)
q=x.difference(y)
r=p.union(q)
print ('\n'.join(sorted(r, key=int)))