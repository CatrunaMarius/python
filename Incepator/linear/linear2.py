#calcula suma cifrelor de trei cifre aleatoare.
#funcția random () generează un număr fracțional aleatoriu de la 0 la 1

from random import random
'''Când numărul este înmulțit cu 900, 
se obține un număr aleator de la 0 la 899. 
Dacă îi adăugați 100, 
obțineți un număr de la 100 la 999. '''

n =random()*900+100

#partea fracționată este aruncată,
# numărul este afișat.
n=int(n)
print(n)

#Prima cifră (cea mai semnificativă) 
#a numărului este extrasă 
#împărțind-o cu 100.
a=n//100

#ultima cifră a numărului este ștearsă prin împărțirea cu 10 . 
#Apoi găsim restul când împărțim cu 10 extrase ultima cifră, 
#care în numărul inițial era în mijloc.
b=(n//10)%10

#ultima cifră (cea mai mică cifră) a numărului este extrasă 
#prin găsirea restului cu diviziunea cu 10.
c=n%10

#suma cifrelor este calculată și afișată pe ecran
print(a+b+c)