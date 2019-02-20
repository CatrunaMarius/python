#The sum and product of the digits of a number

a= abs(int(input()))

suma =0
mult=1

while a>0:
    digit =a%10
    suma +=digit
    mult *=digit
    a=a//10
print("Sum: ", suma)
print("Product:", mult)
