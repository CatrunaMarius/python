
#Găsiți aria și perimetrul unui triunghi cu unghi drept

#modulul matematic care conține diferite 
#funcții matematice este importat.

import math

#funcția input () returnează un string
AB =input("Lungimea of the first leg: ")
AC = input("Length of the second leg: ")

#stringul ar fi transformate în numere real
AB=float(AB)
AC=float(AC)

#găsiți ipotenuza prin teorema lui Pitagora: 
#"suma pătratelor catetelor este egală cu pătratul ipotenuzei".
#Funcția sqrt () a modulului matematic extrage o rădăcină pătrată.
# Operatorul ** ridică un număr la o putere.
BC=math.sqrt(AB**2+AC**2)

#Aria unui triunghi drept este egală cu
# jumătate din suprafața dreptunghiului corespunzător.
S=(AB*AC)/2

#Perimetrul este suma tuturor laturilor.
P=AB+AC+BC

print("Area of the Triangle: %.2f" %S)
print("perimetre of the triangle: %.2f" %P)
