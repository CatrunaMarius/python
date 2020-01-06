
#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

#For Example:

#Www.HackerRank.com → wWW.hACKERrANK.COM
#Pythonist 2 → pYTHONIST 2
#Input Format

#A single line containing a string S.
#Output Format

#Print the modified string s .

#Sample Input 0

#HackerRank.com presents "Pythonist 2".
#Sample Output 0

#hACKERrANK.COM PRESENTS "pYTHONIST 2".

def swap_case(s):
    a=""#prea rezultatul coversiei
    for leter in s:
        if leter.isupper() == True:
            a+=(leter.lower)
        else:
            a+=(leter.upper())
 
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


#metoda 2
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#metoda 3
def swap_case(s):
    return ''.join(map(lambda c: c.upper() if c.islower() else c.lower(), s))
    #metoda 3.1
    #return "".join([x.upper() if x.upper()!=x else x.lower() for x in list(s) ])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)