#problema 1
#Scrieți un program care acceptă o secvență de cuvinte separate de spațiu alb ca intrare 
#și tipărește cuvintele după ce eliminați toate cuvintele duplicate și le sortați alfanumeric. 
#Să presupunem că următorul input este furnizat programului:
#hello world and practice makes perfect and hello world again 
#output 
#again and hello makes perfect practice world

#Hinte
#În cazul în care datele de intrare sunt furnizate la întrebare,
# ar trebui să presupunem că este o intrare de consolă.
# Folosim un container setat pentru a elimina automat datele duplicate
#  și apoi utilizăm sortate () pentru a sorta datele.

s = input().split()

for i in s:
    if s.count(i)>1:
         s.remove(i)
       
s.sort()
print(" ".join(s))

#metoda 2 comprehension
s = input().split()
[s.remove(i) for i in s if s.count(i)>1]
s.sort()
print(" ".join(s))

#metoda 3
s=sorted(list(set(input().split())))
print(" ".join(s))

#problema 2
#Scrieți un program care acceptă o secvență de numere binare de 4 cifre separate de virgulă
# ca intrare a acestuia și apoi verificați dacă sunt divizibile cu 5 sau nu. 
#Numerele divizibile cu 5 trebuie să fie tipărite într-o secvență separată prin virgulă. 
#Exemplu: 0100,0011,1010,1001
#output 1010
#hints
#În cazul în care datele de intrare sunt furnizate la întrebare, 
#ar trebui să presupunem că este o intrare de consolă.

def cheack(x):               #convertește binar în număr întreg și returnează zero dacă este divizibil cu 5
    total,pw =0,1
    reversed(x)
    for i in x:
        total+=pw*(ord(i)- 48)#
        pw*=2
    return total % 5
data = input().split(",")
lst = []

for i in data:
    if cheack(i)==0:        #dacă este găsit zero înseamnă divizibil cu zero și adăugat la listă
        lst.append(i)
print(",".join(lst)) 

#metoda 2
def check(x): 
    return int(x,2)%5==0
data = input().split(',')

data = list(filter(check,data))
print(",".join(data))

#metoda 3
data = input().split(',')
data = list(filter(lambda i:int(i,2)%5==0,data))
print(",".join(data)) 


#problema 3
#Scrieți un program, care va găsi toate aceste numere între 1000 și 3000 (ambele incluse) astfel încât fiecare cifră a numărului să fie un număr egal. 
#Numerele obținute ar trebui să fie tipărite într-o secvență separată de virgule pe o singură linie.

l=[]

for i in range(1000,3001):
    flag =1
    for j in str(i):
        if ord(j)%2 !=0:
            flag=0
    if flag ==1:
        l.append(str(i))
print(",".join(l))

#metoda 2

def check(element):
    return all(ord(i)%2 ==0 for i in element)
l = [str(i) for i in range(1000,3001)]
l = list(filter(check,l))
print(",".join(l))

#metoda 3
l= [str(i) for i in range(1000,3001)]
l= list(filter(lambda i: all(ord(j)%2 ==0 for j in i),l))
print(",".join(l))

values =[]
for i in range(1000,3001):
    s= str(i)
    if int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0 :
         values.append(s)
print(",".join(values))         
       
#Problema 4
#Scrieți un program care acceptă o propoziție și calculați numărul de litere și cifre. 
#Să presupunem că următorul input este furnizat programului:
#  hello world! 123      
#  output
#   LETTERS 10
#   DIGITS 3
#hints
#În cazul în care datele de intrare sunt furnizate la întrebare, 
#ar trebui să presupunem că este o intrare de consolă.

s  = input()
letter,digit = 0,0

for i in s:
    if ('a'<= i and i<='z') or ('A'<=i and i<='Z'):
        letter+=1
    if '0'<=i and i <= '9':
        digit+=1
print("LETTERS {0}\nDIGITS {1}".format(letter,digit))

#metoda 2     

s = input()
letter, digit = 0,0

for i in s:
    letter+=i.isalpha()
    digit+=i.isnumeric()

print("LETTERS %d\nDIGITS %d"%(letter,digit))    
 
#metoda 3
s = input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("LETTERS",d["LETTERS"])
print("DIGITS", d["DIGITS"])

         
#Problema 5  
#   Scrieți un program care acceptă o propoziție și calculați numărul de litere mari și minuscule.
#    Să presupunem că următorul input este furnizat programului: 
#   Hello world!
#   Output
#   UPPER CASE 1
#   LOWER CASE 9
#Hints
#În cazul în care datele de intrare sunt furnizate la întrebare, ar trebui să presupunem că este o intrare de consolă.

s= input()
d={"UPPER CASE":0,"LOWER CASE":0 } 

for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print("UPPER CASE",d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])

#metod 2

s = input()
upper,lower =0,0

for i in s:
    if 'a'<=i and i<='z':
        lower+=1
    if 'A'<=i and i<="Z":
        upper+=1
print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))

#metoda 3
s = input()
upper,lower = 0,0

for i in s:
    lower +=i.islower()
    upper +=i.isupper()
print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))

#metoda 4

s = input() 
upper= sum(1 for i in s if i.isupper())
lower= sum(1 for i in s if i.islower())

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))

#metoda 5
s = input()
upper = 0
lower = 0
for i in s:
    if i.isupper()==True:
        upper+= 1
    if i.islower()==True:
        lower+=1
print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))

#problema 6
#Scrieți un program care calculează valoarea unui + aa + aaa + aaaa cu o cifră dată ca valoare a. 
#Să presupunem că următorul input este furnizat programului: 
#9 
#output: 
#11106

#Hint
#În cazul în care datele de intrare sunt furnizate la întrebare, ar trebui să presupunem că este o intrare de consolă.

a = input()
n1 = int("%s" % a)
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" % (a,a,a))
n4 = int("%s%s%s%s" %(a,a,a,a))

print(n1+n2+n3+n4)

#metoda 2
a = input()
total,tmp =0,str()

for i in range(4):
    tmp+=a
    total+=int(tmp)
print(total)

#metoda 3
a= input()
total= int(a) + int(2*a)+int(3*a)+int(4*a)
print(total)

#Problema 7
#Utilizați o listă de înțelegere pentru a pătra fiecare număr impar dintr-o listă. 
#Lista este introdusă de o secvență de numere separate prin virgulă.
# Să presupunem că următorul input este furnizat programului:
#1,2,3,4,5,6,7,8,9
#output:
#1,9,25,49,81
#În cazul în care datele de intrare sunt furnizate la întrebare, ar trebui să presupunem că este o intrare de consolă.

l =[str(int(i)**2)for i in input().split(',') if int(i)%2]
print(",".join(l))

#problema 8
#Scrieți un program care calculează suma netă a unui cont bancar bazat pe un jurnal de tranzacții de la intrarea consolei.
# Formatul jurnalului de tranzacții este prezentat după cum urmează:
#D 100
#W 200
#D înseamnă depozit în timp ce W înseamnă retragere.
#D 300
#D 300
#W 200
#D 100
#output
#500
#Hints
#În cazul în care datele de intrare sunt furnizate la întrebare,
# ar trebui să presupunem că este o intrare de consolă.
import sys
netAmount =0
while True:
    s=input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation =="W":
        netAmount-=amount
    else:
        pass
    print(netAmount)

#metoda 2
print("metoda 2")
total =0
while True:
    s=input().split(" ")
    if not s:
        break
    cm,num =str,s

    if cm =="D":
        total+=int(num)
    if cm =="W":
        total-=int(num) 
print(total) 
#metoda 3
l=[]
while True:
    x=input()
    if len(x)==0:
        break
    l.append(x)

balance = 0
for item in l:
    if "D" in item:
        balance +=int(item.strip('D '))
    if "W" in item:
        balance -= int(item.strip("W "))
print(balance)
