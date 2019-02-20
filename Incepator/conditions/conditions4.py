
#Convert Celsius to Fahrenheit or vice versa
#input nC or nF is expected, where n is an integer

t=input()

#the last symbol is retrieved
sign =t[-1]

#whole string except last symbol
t=t[0:-1]
#conversion into integer
t=int(t)

#If the sign denotes Celsius,
if sign =='C' or sign == 'c':
    #conversion to Fahrenheit,
    t=t*(9/5)+32
    #rounding to the integer
    t=round(t)
    print(str(t)+'F')
#if the sign indicates Fahrenheit
elif sign =='F' or sign =="f":
    #conversion to Celsius,
    t=(t-32)*(5/9)
    #rounding to the integer
    t=round(t)
    print(str(t)+'C')