# is there a triangle with given sides?

print("Length of the sides: ")
a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))

#A triangle exists only when the sum of any two it's sides is greater than the third party.
#In the if header, three sides are checked immediately.Each of them should be less than the summ of others.
#Therefore, the logical AND operator is used.
if a+b>c and a+c>b and b+c>a:
    print("the tiangle exists")

#if at least one side turns out to be more than the sum of the others, then a triangle cannot be constructrd from the given segments.
else:
    print("The triangle doesn't exists")
#Note. There is a notion of a degenerate triangle. In this case, the third party may egual the sum of the other two.
#In this case in the condition instead of the sign ">" you should use "> =" 