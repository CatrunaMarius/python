#calculați durata anului pe planete
#importați constantul pi din modulul matematic
from math import pi
r=input("Radius of the orbit(milion km): ")
v=input("Orbital speed(km/s): ")

#sirurile de caractere sunt convertite in numerele float.
r=float(r)
v=float(v)

# transforma milioane de kilometri în kilometri
r=r*1000000

#An, exprimat în secunde. lungimea circumferinței este fund (2 * pi * R), 
#adică orbita, și este împărțită la viteză.
year =2*pi*r/v

#pentru a transforma secunde în zile,
# trebuie să împărțiți cu 60 și să obțineți minutele,
# apoi împărțiți 60 și obțineți orele,
# apoi împărțiți cu 24 și obțineți ziua.
year=year/(60*60*24)
print(round(year))
