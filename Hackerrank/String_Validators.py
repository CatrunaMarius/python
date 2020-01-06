#Vi se dă un string.
#Sarcina dvs. este să aflați dacă stringul conține: 
#caractere alfanumerice, 
#caractere alfabetice, 
#cifre, minuscule și caractere mari.
#Sample Input

#qA2
#Sample Output

#True
#True
#True
#True
#True

s = input()
#metoda 1
#print(any(c.isalnum() for c in s))
#print(any(c.isalpha()for c in s))
#print(any(c.isdigit()for c in s))
#print(any(c.islower()for c in s))
#print(any(c.isupper()for c in s))


#metoda 2
#for f in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']:
#	print(any(getattr(c, f)() for c in s))


#metoda 3
#result = ["False", "False", "False", "False", "False"]
#for i in s:
#        if i.isalnum():
#            result[0] = "True"
#        if i.isalpha():
#            result[1] = "True"
#        if i.isdigit():
#            result[2] = "True"
#        if i.islower():
#            result[3] = "True"
#        if i.isupper():
#            result[4] = "True"
#print(*result, sep="\n")


#metoda 4
for fn in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print(any(fn(c) for c in s))

#metoda 5
#methods = [str.isalnum,  str.isalpha,  str.isdigit, str.islower, str.isupper]
#for res in map( lambda m: any( map(m,s) ), methods):
#    print(res)