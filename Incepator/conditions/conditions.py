#Is the number negative or positive?
#user entre a number
a=input()

#converting it to a floating point number
a=float(a)

#If the number is greater then zero,
if a>0:
    #then output 1.
    print(1)
#If the number is less than zero,
elif a<0:
    #then output -1.
    print(-1)
#in all other cases
else:
    #output 0.
    print(0)

 #Note. "all other case" is when the number si zero i.e it is no more and no less than zero.
