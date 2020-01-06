

#Cu un tuple dat (1,2,3,4,5,6,7,8,9,10), scrieți un program pentru a imprima valorile primei jumătăți într-o linie și valorile ultimei jumătăți într-o linie.
#hints
#Utilizați notarea [n1: n2] pentru a obține o felie dintr-un tuple.
tp= (1,2,3,4,5,6,7,8,9,10)
tp1 = tp[:5]
tp2 = tp[5:]
print(tp1)
print(tp2)

#metoda 2
tp1 = (1,2,3,4,5,6,7,8,9,10)
for i in range(0,5):
    print(tp1[i],end=' ')
print()
for i in range(5,10):
    print(tp1[i],end=' ')

#metoda 3
tpl = (1,2,3,4,5,6,7,8,9,10)
l1, l2 =[],[]

for i in range(0,5):
    l1.append(tpl[i])
for i in range(5,10):
    l2.append(tpl[i])
print(l1)
print(l2)

#metoda 4
tup =(1,2,3,4,5,6,7,8,9,10)
l = int(len(tup)/2) 
print(tup[:l],tup[l:]) 

#Problema 2
#Scrieți un program pentru a genera și
# tipări un alt tuple ale cărui valori sunt numere uniforme
#  în tupla dată (1,2,3,4,5,6,7,8,9,10).
#hints
#Folosiți „pentru” pentru a itera tuple. 
#Folosiți tuple () pentru a genera o tuple dintr-o listă.

#tp = (1,2,3,4,5,6,7,8,9,10)
#l=list()
#for i in tp:
#    if i%2 ==0:
#        l.append(tp[i])
#tp2 =tuple(l)
#print(tp2)

#metoda 2
tpl = (1,2,3,4,5,6,7,8,9,10)
tpl1 = tuple(i for i in tpl if i%2 ==0)
print(tpl1)

#metoda 3
tpl = (1,2,3,4,5,6,7,8,9,10)
tpl1 = tuple(filter(lambda x: x%2==0, tpl))
print(tpl1)

#Problema 3
#Scrieți un program care acceptă un șir ca intrare pentru a imprima „Da” dacă șirul este „da” sau „DA” sau „Da”, altfel imprimați „Nu”.
#hints
#Utilizați dacă declarația pentru a judeca starea.

s= input()
if s== "yes" or s=="YES" or s=="Yes":
    print("Yes")
else:
    print("No")

#metoda 2
s= input()
if s.lower() =='yes':
    print("Yes")
else:
    print("No")


#Problema 4
#Scrieți un program care poate face o hartă ()
# pentru a realiza o listă ale cărei elemente sunt pătrate de elemente în 
# [1,2,3,4,5,6,7,8,9,10].
#
#sugestii:
#Utilizați harta () pentru a genera o listă.
# Utilizați lambda pentru a defini funcții anonime.


l = [1,2,3,4,5,6,7,8,9,10]
squaredNambers = map(lambda x:x**2,l)
print(list(squaredNambers)) 

#Problema 5
#Scrieți un program care poate face o hartă () și filtra ()
# pentru a face o listă ale cărei elemente sunt pătrate cu 
# număr egal în [1,2,3,4,5,6,7,8,9,10].

#sugestii:
#Utilizați harta () pentru a genera o listă.Utilizați filtrul () 
#pentru a filtra elemente dintr-o listă. 
#Utilizați lambda pentru a defini funcții anonime.

l = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x:x**2, filter(lambda x:x%2==0,l))
print(list(evenNumbers))

#metoda2
def even(x):
    return x%2==0

def squer(x):
    return x*x

l =[1,2,3,4,5,6,7,8,9,10]
l =map(squer,filter(even,l))
print(list(l)) 

#Problema 6
#Scrieți un program care poate filtra () pentru a realiza
# o listă ale cărei elemente sunt chiar un număr între 1 și 20
#  (ambele incluse).

#sugestii:
#Utilizați filter () pentru a filtra elemente dintr-o listă.
# Utilizați lambda pentru a defini funcții anonime.

evenNumbers = filter(lambda x: x%2==0, range(1,21))
print(list(evenNumbers)) 

#metoda 2
def event(x):
    return x%2==0
evenNumbers = filter(event, range(1,21))
print(list(evenNumbers))
