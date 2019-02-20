#in which quadrant is the point?
#                y|
#                 |
#                 |
#        II       |         I
#                 |                     
#                 |                      x  
#---------------------------------------->
#                 |
#                 |
#     III         |        IV
#                 |
#                 |
#                 

print("The coordinates of a point: ")  
x= float(input("x= "))
y=float(input("y= "))

if x>0 and y>0:
    print("The I quadrant")
elif x<0 and y>0:
    print("The II quadrant")
elif x<0 and y<0:
    print("The III quadrant")
elif x>0 and y<0:
    print("the IV quadrant")
elif x ==0 and y==0:
    print("The point is at origin")
elif x==0:
    print("The point is on the x-axis")
elif y==0:
    print("The point is on the y-axis")
#Note. The sequence of checks is not important, except for the folloeing:
#the check of the equality of both coordinates to zero must precede the checking for yhe eguality to zero of only one coordinate