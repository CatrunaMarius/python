
#În această provocare, sarcina este depanarea codului existent pentru a executa cu succes toate fișierele de test furnizate.

#Python acceptă un concept util de valori ale argumentului implicit. Pentru fiecare argument de cuvinte cheie al unei funcții, putem atribui o valoare implicită care va fi utilizată ca valoare a argumentului menționat dacă funcția este apelată fără aceasta. De exemplu, luați în considerare următoarea funcție de incrementare:

#    def increment_by(n, increment=1):
#    return n + increment
#The functions works like this:

#increment_by(5, 2)
#7
#increment_by(4)
#5

#Debug the given function print_from_stream using the default value of one of its arguments.

#The function has the following signature:

#def print_from_stream(n, stream)

#Această funcție ar trebui să imprime primele n valori returnate prin metoda get_next () a obiectului stream oferit ca argument. Fiecare dintre aceste valori trebuie tipărită într-o linie separată.

#Ori de câte ori funcția este apelată fără argumentul fluxului, ar trebui să utilizeze o instanță a clasei EvenStream definită în butoanele de cod de mai jos ca valoare a fluxului.

#Funcția dvs. va fi testată în mai multe cazuri prin codul șablonului blocat.

#Formatul de intrare

#Intrarea este citită de șablonul de cod blocat furnizat. În prima linie, există un singur număr întreg q care indică numărul de interogări. Fiecare dintre următoarele linii q conține un stream_name urmat de un număr întreg și corespunde unui singur test pentru funcția dvs.

#Format de iesire

#Ieșirea este produsă de șablonul de cod furnizat și blocat. Pentru fiecare dintre interogări (stream_name, n), dacă stream_name este chiar atunci se apelează print_f__stream (n). Altfel, dacă stream_name este ciudat, atunci se numește print_from_stream (n, OddStream ()).

#Sample Input 0

#3
#odd 2
#even 3
#odd 5
#Sample Output 0

#1
#3
#0
#2
#4
#1
#3
#5
#7
#9
'''#sample input 1
#100
#odd 10
#even 7
#odd 4
#odd 10
#even 2
#odd 5
#odd 1
#even 9
#even 1
#odd 1
#even 1
#odd 1
#odd 10
#even 7
#even 4
#odd 5
#odd 2
#even 10
#even 10
#odd 4
#even 5
#odd 6
#even 6
#odd 10
#odd 7
#even 7
#odd 9
#odd 7
#odd 8
#even 1
#odd 9
#even 1
#odd 9
#even 10
#odd 2
#odd 6
#even 8
#odd 2
#even 2
#even 2
#odd 7
#odd 7
#odd 9
#even 6
#even 10
#odd 1
#even 10
#even 3
#even 6
#even 9
#even 4
#odd 2
#even 1
#even 1
#odd 6
#odd 2
#odd 6
#odd 9
#odd 1
#even 4
#odd 2
#odd 8
#odd 2
#odd 10
#even 9
#odd 5
#odd 2
#even 8
#odd 9
#odd 7
#odd 6
#even 7
#odd 9
#odd 3
#even 9
#even 8
#odd 7
#even 3
#odd 7
#even 9
#odd 6
#odd 6
#odd 7
#even 4
#even 3
#odd 7
#odd 8
#even 8
#even 6
#odd 3
#even 10
#odd 2
#even 10
#even 2
#even 7
#even 5
#even 2
#even 8
#even 4
#odd 7

#sample output 1
#1
#3
#5
#7
#9
#11
#13
#15
#17
#19
#0
#2
#4
#6
#8
#10
#12
#1
#3
#5
#7
#1
#3
#5
#7
#9
#11
#13
#15
#17
#19
#0
#2
#1
#3
#5
#7
#9
#1
#0
#2
#4
#6
#8
#10
#12
#14
#16
#0
#1
#0
#1
#1
#3
#5
#7
#9
#11
#13
#15
#17
#19
#0
#2
#4
#6
#8
#10
#12
#0
#2
#4
#6
#1
#3
#5
#7
#9
#1
#3
#0
#2
#4
#6
#8
#10
#12
#14
#16
#18
#0
#2
#4
#6
#8
#10
#12
#14
#16
#18
#1
#3
#5
#7
#0
#2
#4
#6
#8
#1
#3
#5
#7
#9
#11
#0
#2
#4
#6
#8
#10
#1
#3
#5
#7
#9
#11
#13
#15
#17
#19
#1
#3
#5
#7
#9
#11
#13
#0
#2
#4
#6
#8
#10
#12
#1
#3
#5
#7
#9
#11
#13
#15
#17
#1
#3
#5
#7
#9
#11
#13
#1
#3
#5
#7
#9
#11
#13
#15
#0
#1
#3
#5
#7
#9
#11
#13
#15
#17
#0
#1
#3
#5
#7
#9
#11
#13
#15
#17
#0
#2
#4
#6
#8
#10
#12
#14
#16
#18
#1
#3
#1
#3
#5
#7
#9
#11
#0
#2
#4
#6
#8
#10
#12
#14
#1
#3
#0
#2
#0
#2
#1
#3
#5
#7
#9
#11
#13
#1
#3
#5
#7
#9
#11
#13
#1
#3
#5
#7
#9
#11
#13
#15
#17
#0
#2
#4
#6
#8
#10
#0
#2
#4
#6
#8
#10
#12
#14
#16
#18
#1
#0
#2
#4
#6
#8
#10
#12
#14
#16
#18
#0
#2
#4
#0
#2
#4
#6
#8
#10
#0
#2
#4
#6
#8
#10
#12
#14
#16
#0
#2
#4
#6
#1
#3
#0
#0
#1
#3
#5
#7
#9
#11
#1
#3
#1
#3
#5
#7
#9
#11
#1
#3
#5
#7
#9
#11
#13
#15
#17
#1
#0
#2
#4
#6
#1
#3
#1
#3
#5
#7
#9
#11
#13
#15
#1
#3
#1
#3
#5
#7
#9
#11
#13
#15
#17
#19
#0
#2
#4
#6
#8
#10
#12
#14
#16
#1
#3
#5
#7
#9
#1
#3
#0
#2
#4
#6
#8
#10
#12
#14
#1
#3
#5
#7
#9
#11
#13
#15
#17
#1
#3
#5
#7
#9
#11
#13
#1
#3
#5
#7
#9
#11
#0
#2
#4
#6
#8
#10
#12
#1
#3
#5
#7
#9
#11
#13
#15
#17
#1
#3
#5
#0
#2
#4
#6
#8
#10
#12
#14
#16
#0
#2
#4
#6
#8
#10
#12
#14
#1
#3
#5
#7
#9
#11
#13
#0
#2
#4
#1
#3
#5
#7
#9
#11
#13
#0
#2
#4
#6
#8
#10
#12
#14
#16
#1
#3
#5
#7
#9
#11
#1
#3
#5
#7
#9
#11
#1
#3
#5
#7
#9
#11
#13
#0
#2
#4
#6
#0
#2
#4
#1
#3
#5
#7
#9
#11
#13
#1
#3
#5
#7
#9
#11
#13
#15
#0
#2
#4
#6
#8
#10
#12
#14
#0
#2
#4
#6
#8
#10
#1
#3
#5
#0
#2
#4
#6
#8
#10
#12
#14
#16
#18
#1
#3
#0
#2
#4
#6
#8
#10
#12
#14
#16
#18
#0
#2
#0
#2
#4
#6
#8
#10
#12
#0
#2
#4
#6
#8
#0
#2
#0
#2
#4
#6
#8
#10
#12
#14
#0
#2
#4
#6
#1
#3
#5
#7
#9
#11
#13
'''
#Explicație 0

#În eșantion există 3 întrebări.

#În prima interogare, funcția print_from_stream (2, OddStream ()) este exectuată, ceea ce duce la imprimarea valorilor 1 și 2 în linii separate ca primele două numere impare ne negative.

#În cea de-a doua interogare, funcția print_from_stream (3) este exectuată, ceea ce duce la imprimarea valorilor 2,4 și 6 în linii separate ca primele trei numere uniforme negative.

#În cea de-a treia interogare, funcția print_from_stream (5, OddStream ()) este exectuată, ceea ce duce la imprimarea valorilor 1,3,5,7 și 9 în linii separate ca primele cinci numere impare ne-negative.

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())



queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())

