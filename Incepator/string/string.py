#Calculate the sum of the digits of a random three-digit number
#python2
from random import random
 
n = random(* 900 + 100) 
n = int(n)
print(n)
 
# The number is converted to a string type
s = str(n)
 
# The first [0] character of the string is extracted,
# converted to an integer.
# Similarly, the second [1] and the third [2].
a = int(s[0])
b = int(s[1])
c = int(s[2])
 
print(a+b+c)
 
# The sum of digits is calculated and displayed on the screen.
print(a+b+c)