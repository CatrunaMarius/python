#Definiți o funcție care poate calcula suma a două numere.

#sugestii:
#Definiți ca argumente o funcție cu două numere.
# Puteți calcula suma în funcție și returnați valoarea.

def sumFunction(number1, number2):
    return number1+number2
print(sumFunction(1,2))

#metoda 2
sum= lambda n1,n2:n1+n2
print(sum(1,2))

#Problema 2
#Definiți o funcție care poate converti un număr întreg într-un string și să îl imprimați în consolă.

#sugestii:
#Folosiți str () pentru a converti un număr în șir.

def printValue(n):
    print(str(n))
printValue(3)

#metoda 2
conv = lambda x : str(x)
n=conv(10)
print(n)
print(type(n))

#metoda 3
n=10
s=str(n)
print(s)
print(type(s), type(n),sep='\n')

#Problema 3
#Definiți o funcție care poate primi două numere întregi sub formă de string și calculați suma lor și apoi imprimați-o în consolă.

#sugestii:
#Utilizați int () pentru a converti un șir în număr întreg.

def printValue(s1,s2):
    print(int(s2)+int(s2))
printValue("3","4")

#metoda 2
sum= lambda s1,s2:int(s1)+int(s2)
print(sum("10","45"))

#Problema 4
#Definiți o funcție care poate accepta două șiruri ca intrare și concatenează-le și apoi imprimă-o în consolă.

#sugestii:
#Folosiți + semn pentru a concatena șirurile.

def printValue(s1,s2):
    print(s1+s2)
printValue("3","4")

#metoda 2
sum=lambda s1,s2:s1+s2
print(sum("10","45"))

#problema 5
#Definiți o funcție care poate accepta două șiruri ca intrare și imprima șirul cu lungimea maximă în consolă.
# Dacă două șiruri au aceeași lungime, atunci funcția ar trebui să imprime toate șirurile linie cu linie.
#hints
#Utilizați funcția len () pentru a obține lungimea unei șiruri.
def printValue(s1,s2):
    len1=len(s1)
    len2=len(s2)
    if len1>len2:
        print(s1)
    if len1<len2:
        print(s2)
    else:
        print(s1)
        print(s2)

printValue("one", "three")

#metoda 2
def printVal(s1,s2):
    len1 =len(s1)
    len2 =len(s2)
    if len1<len2:
        print(s2)
    elif len1>len2:
        print(s1)
    else:
        print(s1)
        print(s2)
s1,s2=input().split()
printVal(s1,s2)
