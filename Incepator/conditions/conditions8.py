#Determine whether a year is a leap year
#A year is enteref, converted to an integer
year=int(input())

#A year is a leap year if it divided by 4. However, centuries are not leap years, although they are divided by 4.
#But centuries that are divided into 400 are still leap years.
#If the remainder of the division by 4 is not zero, then the year is not divided by 4, and therefore it is an usual.

if year %4 !=0:
    print("usual year")

#Exclude century.
#if a year is a century, is it divided by 400?
elif year %100 ==0:
    if year % 400==0:
        #in that case, the leap year
        print("leap year")


    #If the century is not divisible by 400,
    else:
        #the year is an usual.
        print("usual year")

#In all other cases, the year is a leap.
else:
    print("leap years")