#Get a random integer and float number in given ranges
#From the random module, we iport the random() function , which generates a random float number, and the randint() function, which generates a random integer.
from random import random ,randint

#We request the lower and upper limits of the range, within these limits a random integer will be generated.
print("Range of intefers: ")
imin = int(input())
imax = int(input())

#the randint() function generates a random number n that is not less than imin an not more than imax.
n=randint(imin,imax)
print("%d" % n )

#we requwst the lower and upper limits of the range, within these limits a random float will be generated.
print("Range of floats: ")
fmin= float(input())
fmax=float(input())

#There random() function generates a float number from zero to one.The 1 is not in the range.
n=random()
#Multiply the number by the length of the range. From example if fmax =5.6, fmax =3.2, then we get a random number from 0 to 2.4.
n=n*(fmax-fmin)
#Shift the lower limit of the number by the value of fmin. Thus, the random number will bi in range from 3.2 to 5.6.
n=n+fmin

print("%.3f" %n)