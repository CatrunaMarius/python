#suprafața totală a cilindrului
#importați constantul pi din modulul matematic.
from math import pi

# înălțime cilindru
h=float(input('h= '))

#raza bazei cilindrului
r=float(input('r= '))

#Un cilindru are două baze.
#Aria fiecăruia este pi * R * R.
circles =2*(pi*r**2)

#suprafața laterală a unui cilindru este de 2 * pi * R * H.
side=2*pi*r*h
#suprafața totală
area=circles+side

print('A=', round(area,2))