#hackerrank
#Sample Input 0

#Ross
#Taylor
#Sample Output 0

#Hello Ross Taylor! You just delved into python.

def print_full_name(a, b):
   
    print("Hello %s %s! You just delved into python." %(a,b) )
    print("Hello {} {} ! You just delved into python.".format(a,b))

first_name = input()
last_name = input()
print_full_name(first_name,last_name)