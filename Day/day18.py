
#Utilizând comprehension listei, vă rugăm să scrieți un program pentru a imprima lista după ce eliminați numerele 0, 4, 5 din [12,24,35,70,88,120,155].

#sugestii
#Utilizați comprehension listei pentru a șterge o mulțime de elemente dintr-o listă. Utilizați enumerarea () pentru a obține (index, valoare).


l =[12,24,35,70,88,120,155]
li = [l[i] for i in range(len(l)) if i not in (0,4,5)]
print(li)

#Problema 2
#Folosind comprehension listei, vă rugăm să scrieți un program pentru a imprima lista după eliminarea valorii 24 din [12,24,35,24,88,120,155].

#sugestii
#Folosiți metoda de eliminare a listei pentru a șterge o valoare.

l =[12,24,35,24,88,120,155]
li=[x for x in l if x!=24]
print(li)

#metoda 2 fara comprehension
l=[12,24,35,24,88,120,155]
li=set(l)
li.remove(24)
print(list(li))

#problema 3

#Cu două liste date [1,3,6,78,35,55] și [12,24,35,24,88,120,155], scrieți un program pentru a realiza o listă ale cărei elemente sunt intersecția listelor date mai sus.

#sugestii
#Folosiți setul () și „& =” pentru a efectua operațiunea de intersecție.

l1 = set([1,3,6,78,35,55])
l2 = set([12,24,35,24,88,120,155])
l1 &= l2
l=list(l1)
print(l)

#metoda 2
l1 = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]
set1= set(l1)
set2= set(l2)
intersection = set1 & set2
print(intersection)

#metoda 3
l1 =set([1,3,6,78,35,55])
l2 =set([12,24,35,24,88,120,155])
intersection = set.intersection(l1,l2)
print(intersection)

#problema 4
#Cu o listă dată [12,24,35,24,88,120,155,88,120,155], scrieți un program pentru a imprima această listă după ce eliminați toate valorile duplicate cu comanda originală rezervată.

#sugestii
#Utilizați setul () pentru a stoca un număr de valori fără duplicat.

l =[12,24,35,24,88,120,155,88,120,155]
print(list(set(l)))

#metoda 2
def removeDuplicate(l):
    newl =[]
    seen = set()
    for item in l:
        if item not in seen:
            seen.add(item)
            newl.append(item)
    return newl

l = [12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(l))

#metoda 3
l = [12,24,35,24,88,120,155,88,120,155]
for i in l:
    if l.count(i)>1:
       l.remove(i)
print(l)

#metoda 4
def removeDuplicat(l):
    seen = {}
    for item in  l:
        if item not in seen:
            seen[item] = True
            yield item

l = [12,24,35,24,88,120,155,88,120,155]
ans = list(removeDuplicat(l))
print(ans)

#programul 5
#Definiți o clasă Person și cele două clase child ale acesteia: masculin și feminin. Toate clasele au o metodă „getGender” care poate imprima „Bărbat” pentru clasa masculină și „feminin” pentru clasa feminină.

#sugestii
#Utilizați Subclasa (Parentclass) pentru a defini o clasă pentru copii.

class Person(object):
    def getGender(self):
        return "Unknown"
class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
       return "Female"

aMale = Male()
aFemale = Female()
print(aMale.getGender())
print(aFemale.getGender())





