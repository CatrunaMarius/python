#Find the equation of the line (y=kx+b) passing through two known points
#To find the equation of a straight line 
#(y =kx+b) that passes through 
#two know points, it is necessary to solve the system of equations 
#{y1 =kx1 +b and y2 = kx2 +b},
#where x1,y1, x2,y2 are known variables, kand b are coefficients to be found.
#from this system of equations derive the coefficients b and k:
#the second eguation is converted to the form 
#b=y2-kx2.
#After it the value of b is substituted into
# the first eguation and get  
#k=(y1-y2)/(x1-x2).
#At the end k and b are substituted into the
#eguation y=kx+b and get
#the eqation of a particular line.

print("A(x1; y1): ")
x1=float(input("\tx1= "))
y1=float(input("\ty1= "))

print("B(x2; y2): ")
x2=float(input("\tx2= "))
y2=float(input("\ty2= "))

print("Equation:")
k=(y1-y2)/(x1-x2)
b=y2-k*x2
print("\ty=%.2f*x+%.2f" % (k,b))