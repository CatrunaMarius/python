#Determine the maximum integer of three
a=int(input())
b=int(input())
c=int(input())

print("The maximum is ", end="")

#if A is greater than B and greater then C, then it is the maximum.
if b<=a>=c:
    print(b)
    #Otherwise, we chack the number C, that it is greater than both A and B.
elif a<=c>=b:
    print(c)

#Note 1. The last elif can be replaced by a branch without a condition (else).
#Note 2. In conditional expressions, the sign = is necessary for the case when two numbers have the same maximum values.

