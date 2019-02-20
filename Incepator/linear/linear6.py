#Length of circumference and area of circle
#The math module contains the pow() 
#function and the constant pi.
import math

r=input("Radius = ")

#the string is converted to a float number.
r= float(r)

#The length of circumference is 2*pi*R
ln=2*math.pi *r

#The area of the circle is PI*R*R

area= math.pi*math.pow(r,2)
#Note: in Python, you can raise 
#to a power using the ** operator.
#Then:
#area =math.pi*r**2

print("Length =%.2f" % ln)
print("Area = %.2f" % area)

