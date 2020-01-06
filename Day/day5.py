#Scrieți un program pentru a calcula frecvența cuvintelor de la intrare.
#Ieșirea ar trebui să iasă după sortarea cheii alfanumerice.

#Să presupunem că următorul input este furnizat programului:
#New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
#output:
#2:2
#3.:1
#3?:1
#New:1
#Python:5
#Read:1
#and:1
#between:1
#choosing:1
#or:2
#to:1
#hints:
#    În cazul în care datele de intrare sunt furnizate la întrebare, 
#    ar trebui să presupunem că este o intrare de consolă.
#metoda 1 scrisa in python 2 transformata in python 3
freq ={} 
line= input()
for word in line.split():
    freq[word] = freq.get(word,0)+1 
words=freq.keys()

for w in words:
    print("%s:%d" %(w,freq[w]))

#metoda 2
ss=input().split()
word=sorted(set(ss))

for i in word:
    print("{0}:{1}".format(i,ss.count(i)))

#mrtioda 3
s=input().split()
dict = {}
for i in s:
    i=dict.setdefault(i,s.count(i))

dict= sorted(dict.items())
for i in dict:
    print("%s:%d" %(i[0],i[1]))

    #metoda 4
s= input().split()
dict = {i:s.count(i) for i in s}
dict = sorted(dict.items())

for i in dict:
    print("%s:%d"%(i[0],i[1]))

#metoda 5
from collections import Counter

s = input().split()
s = Counter(s)
s = sorted(s.items())

for i in s:
    print("%s:%d"%(i[0],i[1]))

#metoda 6
from pprint import pprint
p=input().split()
pprint({i:p.count(i) for i in p})

#Problema 2
#Scrieți o metodă care poate calcula valoarea pătrată a numărului
#Hint
#Folosind operatorul ** care poate fi scris ca n ** p unde înseamnă n ^ p

def square(num):
    return num**2
print(square(2))
print(square(3))

#metoda 2
n=int(input())
print(n**2)


#Problema 3
#Python are multe funcții încorporate și, dacă nu știi cum să-l folosești, 
#poți citi documente online sau găsești câteva cărți.
# Dar Python are o funcție de document încorporată pentru fiecare funcție încorporată.

#Vă rugăm să scrieți un program pentru a imprima unele documente funcționale integrate Python,
# cum ar fi abs (), int (), raw_input ()

#Și adăugați document pentru propria funcție
#hints
#The built-in document method is __doc__

print (abs.__doc__)
print(int.__doc__)
print(input().__doc__)

def square(num):
    '''Return the square value of the input number.
    
    The input number must be integer.
    '''
    return num **2

print(square(2))
print(square.__doc__)

#metoda 2
print(str.__doc__)
print(sorted.__doc__)

def pow(n,p):
      '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''
      return n**p

print(pow(3,4))
print(pow.__doc__)


#Definiți o clasă, care au un parametru de clasă și au același parametru de instanță
#hint
#Definiți un parametru de instanță, trebuie să îl adăugați în metoda __init__.
# Puteți iniția un obiect cu parametru construct sau să setați valoarea mai târziu

class Person:
    name="Person"

    def __init__(self, name = None):
        self.name =name
jeffrey = Person("Jeffrey")
print("s% name is %s" %(Person.name, jeffrey.name))

nico =Person()
nico.name ="Nico"
print("%s name is %s" %(Person.name, nico.name)) 

#metoda 2

class Car:
    name = "Car"
    
    def __init__(self,name = None):
        self.name =name
honda=Car("Honda")
print("%s name is %s" %(Car.name, honda.name))

toyota=Car()
toyota.name="Toyota"
print("%s name is %s"%(Car.name, toyota.name))
