#the digits are represented as symbils.Find the difference and sum
n1='3'
n2 ='8'

#the ord() function returns the caracter number in the symbol table.
a=ord(n1)
b=ord(n2)

#Symbols of digits follow one another in the table.Therefore, difference of their codes will be tha same as the difference of digits.
diff=a-b

#If we subtract the code of zero from the code of digit, we get the number corresponding to the digit character.
a=a-ord('0')
b=b-ord('0')
#After that you can simply find the sum of the numbers.
sum=a+b
print("%s-%s=%d" %(n1,n2,diff))
print("%s+%s=%d" %(n1,n2,sum))