#Is a number print or complex?

import math

n=int(input())

if n<2:
    print("A number must be more 1")
    
elif n==2:
    print("It's prim number")
    

i=2

limit =int(math.sqrt(n))

while i <= limit:
    if n % i ==0:
        print("It's composite number")
       # quit()
        break
    i += 1
   # else: print("it's prime number")
    break
      