#Sample Input 0

#ABCDEFGHIJKLIMNOQRSTUVWXYZ
#4
#Sample Output 0

#ABCD
#EFGH
#IJKL
#IMNO
#QRST
#UVWX
#YZ

import textwrap

def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
    #metoda 2
    for i in range(0,len(string)+1,max_width):
        result=string[i:i+max_width]
        if len(result)==max_width:
            print(result)
        else:
            return(result)

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)