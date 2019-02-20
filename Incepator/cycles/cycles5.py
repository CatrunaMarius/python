#Convert a number from the decimal number system to any nuber system with base up to 9
#Conversia unui număr de la sistemul de numere zecimale la orice sistem numeric cu baza de până la 9
num=int(input("introdu numarul pe care vrei sa-l transformin din baza 10"))
base=int(input("Base(2-9): "))
if not(2<=base<=99):
       quit()
newNum= ''

while num >0:
    newNum =str(num% base)+newNum
    num //=base
print(newNum)

#exemplu 53 in baza zece convertit in baza 2
#53=1*2^5+1*2^4+1*2^2+1*2^0
#2^0=1
#2^1=2
#2^2=4
#2^3=8
#2^4=16
#2^5=32
#2^6=64>53 daca este mai mare decat numarul nostru ne oprim aici
#2^5|2^4|2^3|2^2|2^1|2^0
#1  |1  |0  |1  |0  |1
#unde este unu inseama ca 2^5 ai intrat in 53 decat o data,aic vom scadea din 53 -(2^5)=>53-32=21;2^4 a intrat in 21 o sigura data(21-16=5)
#modivul pentru care avem 0 la 2^3 este ca 2^3 (8) este > decat 5
#deci 53 in baza 10 convertit in baza 2 este 110101
#