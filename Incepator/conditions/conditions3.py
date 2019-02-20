#Checking the divisibility of one integer by another
#The check of divisibility mekes sens only for integers. Therefore, we convert the string returned by the input() function to an integer type using the int() function.
a=int(input("introdu numarul pe care trebuie sa il imparti: "))
b=int(input("introdu numarul la care il inparti: "))

#The % operator returns the rramainder of the division.If it is zero, i.e there is no remainder, then the first number is devided completely into the second.
if a %b==0:
    print("yes")

#in all other cases there is the remainder, and it is no zero. Hence, the firt number is not divided completely into the second. 
else:
    print("no")

    #displey the value of the remainder
    print("The remainder is ", a%b )