#Problema 1
#Scrieți un program care va găsi toate aceste numere care sunt divizibile cu 7,
# dar care nu sunt un multiplu de 5, între 2000 și 3200 (ambele incluse).
# Numerele obținute ar trebui să fie tipărite într-o secvență separată de virgule pe o singură linie.

for i in range(2000,3201):
    if i%7==0 and i%5!=0:
       print(i, end=',')

#Problema 2
#Scrieți un program care poate calcula factorialul unui numar dat. 
#Rezultatele ar trebui să fie tipărite într-o secvență separată de virgule pe o singură linie.
#Supunem că următorul input este furnizat programului: 8 Apoi, ieșirea ar trebui să fie: 40320

#for loop
n=int(input())
fact =1
for i in range(1,n+1):
    fact = fact*i
print(fact)

#while loop
n = int(input())
fact=1
i=1
while i <=n:
    fact = fact*i
    i= i + 1
print(fact)

#Problema 3
#Cu un număr integral dat n, scrieți un program pentru a genera un dicționar care conține (i, i x i) 
#astfel încât să fie un număr integral între 1 și n (ambele incluse). 
#apoi programul ar trebui să imprime dicționarul.Supuneți programului următoarea intrare: 8

#Apoi, ieșirea ar trebui să fie:

n =int(input())
r={}
for i in range(1,n+1):
    r[i] = i*i
print(r)

#comprehension 
n=int(input())
print({i : i*i for i in range(1,n+1)})

#Problema 4
#Scrieți un program care acceptă o secvență de numere separate de virgulă de pe consolă și 
#generează o listă și un tuple care conține fiecare număr.
#Supunem că următorul input este furnizat programului:
#34,67,55,33,12,98
#output
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

l=input().split(',')
t=tuple(l)
print(l, t,sep='\n')

#Problema 5
#Definiți o clasă care are cel puțin două metode:

#getString: pentru a obține un șir de la intrarea consolei
#printString: pentru a imprima șirul cu majuscule.
#De asemenea, vă rugăm să includeți funcția de testare simplă pentru a testa metodele clasei.

class myclass():
    #def __init__(self):
    #    pass

    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())
xx=myclass()
xx.getString()
xx.printString()

#Problema 6
#Q = Rădăcina pătrată a [(2 * C * D) / H]
#Următoarele sunt valorile fixe ale lui C și H:
#C este 50. H este 30.
#D este variabila ale cărei valori trebuie introduse în programul dvs. 
#într-o secvență separată de virgulă. De exemplu, 
#să presupunem că urmează programului următoarea secvență de intrare separată de virgule:
#100,150,180
#output
#18,22,24
from math import *


#comprehension
c,h = 50, 30

def calc(d):
    return sqrt((2*c*d)/h)

d= input().split(",")
d=[str(round(calc(int(i)))) for i in d]
print(",".join(d))

#metoda 3
c,h=50,30

def calc(d):
    return sqrt((2*c*d)/h)
print(",".join([str(int(calc(int(i)))) for i in input().split(",")]))

#metoda 4
c,h =50,30
def calc(d):
    d = int(d)
    return str(int(sqrt((2*c*d)/h)))

d=input().split(',')
d=list(map(calc,d))
print(",".join(d))

#Problema 7
#Scrieți un program care are 2 cifre, X, Y ca intrare și generează un tablou bidimensional.
# Valoarea elementului din primul rând și j-a coloană a tabloului ar trebui să fie i * j. Notă: i = 0,1 .., X-1; j = 0,1, ¡Y-1.
#  Să presupunem că sunt date următoarele intrări programului: 3,5 Apoi, rezultatul programului ar trebui să fie:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

x,y = map(int, input().split(','))
l=[]

for i in range(x):
    temp = []
    for j in range(y):
        temp.append(i*j)
    l.append(temp)
print(l)

x,y=map(int, input().split(","))
l=[[i*j for j in range(y)]for i in range(x)]
print(l)

#Problema 8
#Scrieți un program care acceptă o secvență de cuvinte separată de virgulă ca intrare și
# tipărește cuvintele într-o secvență separată de virgule după sortarea lor în ordine alfabetică.

#Să presupunem că următorul input este furnizat programului:
# without,hello,bag,world
#output: bag,hello,without,world

l= input().split(',')
l.sort()
print(l) 

#Scrieți un program care acceptă secvența de linii ca intrare și tipărește liniile după ce toate caracterele propoziției sunt majusculate

#Să presupunem că următorul input este furnizat programului:
#Hello world
#Practice makes perfect

#Output
#HELLO WORLD
#PRACTICE MAKES PERFECT

l=[]

while True:
    s=input()
    if len(s)==0:
        break;
    l.append(s.upper())

for line in l:
    print(line)

