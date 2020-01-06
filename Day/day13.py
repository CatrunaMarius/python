
#Scrieți un program pentru a calcula:

#f (n) = f (n-1) +100 când n> 0
#și f (0) = 1
#cu o intrare n dată de consolă (n> 0).

#Exemplu: Dacă următorul n este dat ca intrare pentru program:

#5
#Apoi, rezultatul programului ar trebui să fie:

#500
#În cazul în care datele de intrare sunt furnizate la întrebare, ar trebui să presupunem că este o intrare de consolă.

#sugestii
#Putem defini funcția recursivă în Python.

def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100

n= int(input())
print(f(n))

#problema 2
#Secvența Fibonacci este calculată pe baza formulei următoare:

#f (n) = 0 dacă n = 0
#f (n) = 1 dacă n = 1
#f (n) = f (n-1) + f (n-2) dacă n> 1
#Vă rugăm să scrieți un program pentru a calcula valoarea f (n) cu o intrare n dată de către consolă.

#Exemplu: Dacă următorul n este dat ca intrare pentru program:

#7
#Apoi, rezultatul programului ar trebui să fie:

#13
#În cazul în care datele de intrare sunt furnizate la întrebare, ar trebui să presupunem că este o intrare de consolă.

#sugestii
#Putem defini funcția recursivă în Python.

def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)

n= int(input())
print(f(n))

#metoda 2
def f(n):
    if n<2:
        return n
    return f(n-1)+f(n-2)

n= int(input())
print(f(n))

#problema 3
#Secvența Fibonacci este calculată pe baza formulei următoare:

#f (n) = 0 dacă n = 0
#f (n) = 1 dacă n = 1
#f (n) = f (n-1) + f (n-2) dacă n> 1
#Vă rugăm să scrieți un program pentru a calcula valoarea f (n) cu o intrare n dată de către consolă.

#Exemplu: Dacă următorul n este dat ca intrare pentru program:

#7
#Apoi, rezultatul programului ar trebui să fie:

#0,1,1,2,3,5,8,13
#În cazul în care datele de intrare sunt furnizate la întrebare, ar trebui să presupunem că este o intrare de consolă.

#sugestii
#Putem defini funcția recursivă în Python. Utilizați înțelegerea listei pentru a genera o listă dintr-o listă existentă. Utilizați string.join () pentru a vă alătura unei liste de șiruri.

#metoda 1.0
def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return f(n-1)+f(n-2)
#metoda 1.1
def f(n):
    if n<2:
        return n
    return f(n-1)+f(n-2)

n= int(input())
values = [str(f(x)) for x in range(0,n+1)]
print(",".join(values))

#metoda 3
def f(n):
    if n<2:
        fibo[n]=n
        return fibo[n]
    fibo[n]=f(n-1)+f(n-2)
    return fibo[n]

n= int(input())
fibo = [0]*(n+1)# initializeaza lungimea listei (n+1)
f(n)            # cheama din nou si seteaza valoare lui fibo[0-n]
fibo=[str(i) for i in fibo]#conveteste intigerul dat in string
ans=",".join(fibo)
print(ans)

#Problema 4
#Vă rugăm să scrieți un program folosind generator pentru a imprima numerele uniforme între 0 și n în formă separată de virgulă, în timp ce n este introdus de consolă.

#Exemplu: Dacă următorul n este dat ca intrare pentru program:

#10
#Apoi, rezultatul programului ar trebui să fie:

#0,2,4,6,8,10
#În cazul în care datele de intrare sunt furnizate la întrebare, ar trebui să presupunem că este o intrare de consolă.

#sugestii
#Utilizați randamentul pentru a produce următoarea valoare în generator.

def EventGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1

n=int(input())
values =[]
for i in EventGenerator(n):
    values.append(str(i))
print(",".join(values))

#Problema 5
#Vă rugăm să scrieți un program folosind generator pentru a imprima numerele care pot fi divizibile cu 5 și 7 între 0 și n sub formă separată de virgulă, în timp ce n este introdus de consolă.

#Exemplu: Dacă următorul n este dat ca intrare pentru program:

#100
#Apoi, rezultatul programului ar trebui să fie:

#0,35,70
#În cazul în care datele de intrare sunt furnizate la întrebare, ar trebui să presupunem că este o intrare de consolă.

#sugestii
#Utilizați randamentul pentru a produce următoarea valoare în generator.

def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n = int(input())
values = []
for i in NumGenerator(n):
    values.append(str(i))
print(",".join(values))

#metoda 2
def generate(n):
    for i in range(n+1):
        if i %35 ==0:   #7*5 =35 dacă un număr este divizibil cu a & b, atunci acesta este, de asemenea, divizibil cu a * b
            yield i

n= int(input())
resp=[str(i) for i in generate(n)]
print(",".join(resp))

 
