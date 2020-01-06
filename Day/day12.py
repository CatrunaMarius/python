
#Presupunând că avem câteva adrese de e-mail în formatul „username@companyname.com”, 
#vă rugăm să scrieți un program pentru a imprima numele companiei unei adrese de e-mail date.
# Atât numele de utilizator, cât și numele companiei sunt compuse numai din litere.

#Exemplu: Dacă este introdusă următoarea adresă de e-mail ca intrare în program:

#john@google.com
#Apoi, rezultatul programului ar trebui să fie:

#Google
#În cazul în care datele de intrare sunt furnizate la întrebare, ar trebui să presupunem că este o intrare de consolă.

#hints
#folosest \w pt a gasi literele

import re 

email = input()
pat2 ="(\w+)@(\w+)\.(com)"
r2 =re.match(pat2,email)
print(r2.group(2))

#metoda 2
email = "john@google.com elise@python.com"
pattern = "\w+@(\w+).com"
ans= re.findall(pattern,email)
print(ans)

##problema 2
##Scrieți un program care acceptă o secvență de cuvinte separate de spațiul alb ca intrare pentru a imprima doar cuvintele compuse din cifre.

##Exemplu: Dacă următoarele date sunt date ca intrare în program:

##2 pisici și 3 câini.
##Apoi, rezultatul programului ar trebui să fie:

##['2', '3']
##În cazul în care datele de intrare sunt furnizate la întrebare, ar trebui să presupunem că este o intrare de consolă.

##sugestii
##Folosiți re.findall () pentru a găsi toate subcategorii folosind regex.

import re
s = input()
print(re.findall('\d+',s))

#metoda 2
email = input()
pattern = "\d+"
ans =re.findall(pattern,email)
print(ans)

#metoda 3
email = input().split()
ans =[]
for words in email:
    if words.isdigit():
        ans.append(words)
print(ans)

#metoda 4
email = input().split()
ans=[word for word in email if word.isdigit()]
print(ans)

#problema 3
#Tipăriți un șir unicode „salut lume”.

#sugestii
#Utilizați formatul u'strings pentru a defini șirul Unicode.

u= u"hello world!"
print(u)

#problema 4
#Scrieți un program pentru a citi un șir ASCII și
# pentru ao converti într-un șir unicod codificat de utf-8.

#sugestii
#Utilizați funcția unicode () / codare () pentru a converti.

s = input()
u = s.encode('utf-8')
print(u)

#problema 5
#Scrieți un comentariu special pentru a indica faptul că un fișier cod sursă Python este în cod unicode.

#sugestii
#Utilizați funcția unicode () pentru a converti.

#Soluţie:

# - * - codare: utf-8 - * -

#problema 6
#Scrieți un program pentru a calcula 1/2 + 2/3 + 3/4 + ... + n / n + 1 cu o intrare n dată de către consolă (n> 0).

#Exemplu: Dacă următorul n este dat ca intrare pentru program:

#5
#Apoi, rezultatul programului ar trebui să fie:

#3,55
#În cazul în care datele de intrare sunt furnizate la întrebare, 
#ar trebui să presupunem că este o intrare de consolă.

#sugestii
#Utilizați float () pentru a converti un număr întreg într-un float. 
#Chiar dacă nu este convertit, acesta nu va cauza o problemă, 
#deoarece implicit python înțelege tipul de date al unei valori

n = int(input())
sum =0.0
for i in range(1,n+1):
    sum+= float(float(i)/float(i+1))
print(sum)

#metoda 2
n=int(input())
sum = 0
for i in range(1,n+1):
    sum+= i/(i+1)
print(round(sum,2))
