#dose the point belong to a circle with it's a center at the origin?
import math
#The coorfinates of a point that is either inside the circle or not
print("Point: ")
x=float(input("x= "))
y=float(input("y= "))

#The radius of a circle with the center at origin.
print("Radius of circle: ")
r=float(input("r= "))

#It is necessary to calculate the length of the segment from the origin to a given point. If this segment is not larger than the radius of the circle, then the point will belong to the circle.
#this segment is a hypotenuse of a right triangle; one leg of which is egual to the distance X, the second to the distance Y. The hypotenuse is found by the Pythagorea theorem.
hyp =math.sqrt(x**2+y**2)

#If hypotenuse is no larger than radius...
if hyp<=r:
    print("Point belongs to the circle.")
#Otherwise...
else:
    print("Point doesn't belong to the circle.")