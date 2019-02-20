#Solve the quadratic equation
#The sqrt() function retrieves the square root
from math import sqrt

#The quadratic equation has the form a*x*x*b*x+c=0. When the coefficients a,b,c are known, we are deaking with a specific quadratic eguation.
#The roots of the equation are the values of the variable x for which a particular eguation becomes true.

#What eguation should be solved?
a=float(input("a= ")) 
b=float(input("b= "))
c=float(input("c= "))

#Calculating the discriminant
d=b*b-4*a*c

#if it is greater than zere, then the equation has tow roots.
if d>0:
    x1=(-b+sqrt(d))/(2*a)
    x2=(-b+sqrt(d))/(2*a)
    print("x1 =%.2f; x2 =%.2f" %(x1,x2))
#if thediscriminant is less than zero, then the equation has one root.
elif d ==0:
    x1=-b/(2*a)
    print("x1 =%.2f" % x1)

#Otherwise(if the discriminant is less than zero) the equation has no roots.
else:
    print("No roots")