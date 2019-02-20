#determine the letter number in the alphabet

#Any lowercase letter should be entered.
c=input("Letter(a-z): ")

#the ord() function return the ordinal number of a character in the symbol table.
c=ord(c)

#The code of the firs letter of the alphabet.
a=ord('a')

#Since the letters folloe in order, by subtracting the character codes,we find the distance between them.
n=c-a

#since it is necessary to find not the distance, but the ordinal number of the letter in  the alphabet, we add1.
n=n+1

print("it's number is %d" % n)
