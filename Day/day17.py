
#Vă rugăm să scrieți un program pentru a imprima lista după ce eliminați numerele uniforme în [5,6,77,45,22,12,24].
# Sugestii Utilizați comprehension listei pentru a șterge o mulțime de elemente dintr-o listă.

l = [5,6,77,45,22,12,24]
l = [x for x in l if x%2!=0]
print(l)

#metoda 2
def isEven(n):
    return n%2!=0
l=[5,6,77,45,22,12,24]
lst =list(filter(isEven,l))
print(lst)

#metoda 3
l = [5,6,77,45,22,12,24]
lst = list(filter(lambda n:n%2!=0,l))
print(lst)

#problema 2
#Folosind comprehension listei, vă rugăm să scrieți un program pentru a imprima lista după eliminarea numerelor divizibile cu 5 și 7 în [12,24,35,70,88,120,155].

#sugestii
#Utilizați înțelegerea listei pentru a șterge o mulțime de elemente dintr-o listă.

l =[12,24,35,70,88,120,155]
li =[x for x in l if x%5!=0 and x%7!=0]
print(li)

#metoda 2
l =[12,24,35,70,88,120,155]
li = [x for x in l if x%35!=0]
print(li)

#problema 3
#Utilizând înțelegerea listei, vă rugăm să scrieți un program pentru a tipări lista după ce eliminați numerele 0, 2, 4, 6 din [12,24,35,70,88,120,155].

#sugestii
#Utilizați înțelegerea listei pentru a șterge o mulțime de elemente dintr-o listă. Utilizați enumerarea () pentru a obține (index, valoare) tuple.

l = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(l) if i%2!=0]
print(li)

#metoda 2
l = [12,24,35,70,88,120,155]
li =[l[i] for i in range(len(l)) if i%2 != 0]
print(li)

#problema 4
#Utilizând comprehension listei, vă rugăm să scrieți un program pentru a imprima lista după ce eliminați numerele 2 - 4 din [12,24,35,70,88,120,155].

#sugestii
#Utilizați comprehension listei pentru a șterge o mulțime de elemente dintr-o listă. Utilizați enumerarea () pentru a obține (index, valoare) tuple.

l = [12,24,35,70,88,120,155]
li= [ x for (i,x) in enumerate(l) if i<3 or 4<i]
print(li)

#metoda 2
l =[12,24,35,70,88,120,155]
li= [l[i] for i in range(len(l)) if i<3 or 4<i]
print(li)

#problema 5
#Utilizând comprehension listei, vă rugăm să scrieți un program pentru a genera un tablou 3D 3 * 5 * 8 al cărui element este 0.

#sugestii
#Utilizați comprehension listei pentru a crea un tablou.

array =[[[0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)
