
#O adresă de e-mail validă îndeplinește următoarele criterii:

#Este compus dintr-un nume de utilizator, nume de domeniu și extensie asamblate în acest format: username@domain.extension
#Numele de utilizator începe cu un caracter alfabetic englezesc și 
#toate caracterele ulterioare constau dintr-unul sau mai multe dintre următoarele: caractere alfanumerice, -,., Și _.
#Domeniul și extensia conțin doar caractere alfabetice engleze.
#Extensia are 1, 2 sau 3 caractere.
#Fiind date de intrare n perechi de nume și adrese de e-mail, imprimați fiecare pereche de adrese de e-mail și o adresă de e-mail validă pe o nouă linie.

#Sugestie: încercați să utilizați Email.utils () pentru a finaliza această provocare. De exemplu, acest cod:


#Formatul de intrare

#Prima linie conține un singur număr întreg, n, care indică numărul de adrese de e-mail.
#Fiecare linie i din cele n linii ulterioare conține un nume și o adresă de e-mail ca două valori separate în spațiu după acest format:
#nume <user@email.com>

#Format de iesire

#Tipăriți perechile de adrese de e-mail și nume separate de spațiu care conțin doar adrese de e-mail valide. 
#Fiecare pereche trebuie tipărită pe o nouă linie în următorul format:

#nume <user@email.com>
#Trebuie să imprimați fiecare adresă de e-mail validă în aceeași ordine în care a fost primită ca intrare.

#Sample Input

#2  
#DEXTER <dexter@hotmail.com>
#VIRUS <virus!@variable.:p>
#Sample Output

#DEXTER <dexter@hotmail.com>


#Explicaţie

#dexter@hotmail.com este o adresă de e-mail validă, astfel încât tipărim numele și adresa de e-mail primite ca intrare pe o nouă linie.
#virus! @variable .: p nu este o adresă de e-mail validă, deoarece numele de utilizator conține un punct de exclamare (!),
# iar extensia conține un punct (:). Deoarece acest e-mail nu este valid, nu imprimăm nimic.
import re



n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)

#metoda
print("metoda 2")
import email.utils,re

for _ in range(int(input())):

   t = email.utils.parseaddr(input())


   if bool(re.match('[a-zA-Z](\w|-|\.)*@[a-zA-Z]*\.[a-zA-Z]{0,3}$',t[1])) :
       print( email.utils.formataddr(t))

#metoda 3
print("metoda 3")
import re, sys
[print(e.strip('\n')) for e in sys.stdin if re.search('<[a-z][a-z0-9_.-]+@[a-z]+\.[a-z]{1,3}>', e, re.I)]

#metoda 4
import re


email_pattern = re.compile(r"^[a-zA-Z0-9]+[a-zA-Z0-9-_.]*\@[a-zA-Z]*\.[a-zA-Z]{1,3}$")

for _ in range(int(input())):
        in_str = input()
        if email_pattern.match(in_str.split()[1].strip("<>")):
                print(in_str)