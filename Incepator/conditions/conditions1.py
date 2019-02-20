#Is the number even or add?
#user entre a number

a=input("introdu un numbar: ")

#convert it to intiger type
a=int(a)

#the % operator returns the residue of the division. Even numbers are completely divisible by 2, i.e. the remainder is 0. Odd numbers have a residue equal to 1.

#if the remainder of the division is zero,
if a%2 ==0:
    #the number is even.
    print("Even")
#Otherwise,
else:
    #the number is odd.
    print("Odd")