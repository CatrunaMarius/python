
#You are given a string S.
#Your task is to find out whether S is a valid regex or not.

#Sample Input

#2
#.*\+
#.*+
#Sample Output

#True
#False

import re
for _ in range(int(input())):
    ans = True
    try:
        reg = re.compile(input())
    except re.error:
        ans = False
    print(ans)

#metoda 2
for i in range(int(input())):  
    try:
        print(bool(re.compile(input())))
    except:
        print('False')

#metoda 3
def isvalidregex(regex):
    try: re.compile(regex)
    except re.error: return False
    return True

for i in range(int(input())):
    print(isvalidregex(input()))