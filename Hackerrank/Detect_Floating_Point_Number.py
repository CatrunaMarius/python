
#^ says start of the expression.

#[-+]? says it can start with either - or +.

#[0-9] says any number from 0-9 can be followed after it.

#* says that whichever thing it follows[in this case it is[0-9]], it can repeat arbitrarily times, even 0 times.

#'.' is placeholder for any character.(for the answer it should be '\.' instead of '.' ; '\' is escape character. Because of this you can literally mean a dot in expression).

#again[0-9] as explained earlier.

#'+' says that whichever thing it follows[in this case it is[0-9]], it can repeat arbitrarily times, but atleast one time.

#$ follows whichever thing it should come in the end.

#Sorry for my bad english.And someone please correct if something is wrong.


import re

for _ in range(int(input())):
    
    print(bool(re.search(r'^[-+]?[0-9]*\.[0-9]+$',input() )))
    
#metoda 2
[print(bool(re.match(r'[-+]?[0-9]*\.[0-9]{1,}$',input()))) for i in range(int(input()))]

#metoda 3
for _ in range(int(input())):
     print(bool(re.match(r'[+-]?\d*[.]\d+$', input())))  # Using special sequences 

#metoda 4
count=int(input().strip())
for _ in range(count):
    ans=False
    try:
        string=input().strip()
        number=float(string)
        ans=True
        number=int(string)
        ans=False
    except:
        pass
    print(ans)

#metoda 5
def is_float(txt):
    try:
        float(txt)
        return True
    except ValueError:
        return False

n = int(input())
lines = [input().strip() for _ in range(n)]
for l in lines:
    if(l=='0'): print(False)
    else:
        print(is_float(l))

#metoda 5.1
for _ in range(int(input())):
    s = input()
    try:
        int(s)
        print(False)
    except:
        try:
            float(s)
            print(True)
        except:
            print(False)
