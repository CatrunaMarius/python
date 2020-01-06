
#Când utilizatorii postează o actualizare pe rețelele de socializare, cum ar fi o adresă URL, o imagine, o actualizare de stare etc., alți utilizatori din rețeaua lor pot vedea această nouă postare în fluxul lor de știri. Utilizatorii pot vedea de asemenea exact când a fost publicată postarea, adică câte ore, minute sau secunde în urmă.

#Deoarece uneori postările sunt publicate și vizualizate în diferite zone de timp, acest lucru poate fi confuz. Vi se oferă două mărci de timp ale unei astfel de postări pe care un utilizator le poate vedea pe newsfeed-ul său în următorul format:

#Ziua dd Luni aaaa hh: mm: ss + xxxx

#Aici + xxxx reprezintă fusul orar. Sarcina dvs. este de a imprima diferența absolută (în câteva secunde) între ele.

#Formatul de intrare

#Prima linie conține T, numărul de probe.
#Fiecare cutie de testare conține 2 linii, reprezentând timpul t1 și timpul t2.

#Sample Input 0

#2
#Sun 10 May 2015 13:54:36 -0700
#Sun 10 May 2015 13:54:36 -0000
#Sat 02 May 2015 19:54:36 +0530
#Fri 01 May 2015 13:54:36 -0000
#Sample Output 0

#25200
#88200

#metoda de a rezolva problema de pe hackerrank
#import math
#import os
#import random
#import re
#import sys
#import datetime
## Complete the time_delta function below.
#def time_delta(t1, t2):
    
#    t1=datetime.datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z' )
#    t2=datetime.datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z' )
#    return str(int((abs(t1-t2)).total_seconds()))

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

#    t = int(input())

#    for t_itr in range(t):
#        t1 = input()

#        t2 = input()

#        delta = time_delta(t1, t2)

#        fptr.write(delta + '\n')

#    fptr.close()


#metoda 1
from datetime import datetime as dt

fmt = '%a %d %b %Y %H:%M:%S %z'
for _ in range(int(input())):
    time1 = dt.strptime(input(), fmt)
    time2 = dt.strptime(input(), fmt)
    print(int(abs((time1 - time2).total_seconds())))

#metoda 2

from datetime import datetime

for _ in range(int(input())):
    t1=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    t2=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    print (int(abs((t1-t2).total_seconds())))