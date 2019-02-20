#operațiuni bitrate
n1=input("binary n1: ")
n2=input("binary n2: ")
print()


#Strings n1 and n2 are converted to
# decimal numbers, since bitwise 
#operations can be performed only 
#with numbers. While the binary 
#representation of a number is a string.
n1=int(n1,2)
n2=int(n2,2)

#In computer memory, binary operations
# are performed on bits of numbers,
#alrhough we specify decimal numbers 
#as operands. Also, the result is 
#a decimal number.
bit_or =n1|n2 #| -bitwise OR
bit_and =n1&n2 #& -bitwise AND
bit_xor =n1^n2 #^ -exclusive OR

#The bin() function converts a decimal
# number to a binary number, which is 
#a string, the first two characters 
#of which are '0b'

bit_or =bin(bit_or)
bit_and = bin(bit_and)
bit_xor =bin(bit_xor)

print("n1: %10s" % bin(n1))
print("n2: %10s" % bin(n2))
print("   ------------" )
print("OR: %10s" % bit_or)
print("AND: %10s" % bit_and)
print("XOR: %10s" % bit_xor)