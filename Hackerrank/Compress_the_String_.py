#Sample Input

#1222311
#Sample Output

#(1, 1) (3, 2) (1, 3) (2, 1)
from itertools import *

#print(*[(len(list(c)), int(k)) for k, c in groupby(input())])

#metoda 2
s= input()
for i,j in groupby(s): 
    print((len(list(j)),int(i)), end=' ') 

#metoda 3 
#s = input()
#for k, g in groupby(s):
#    print("({}, {})".format(len(list(g)), k), end=" ")  

#metoda 4
#a=input()
#s=''
#for i in range(0,len(a)):
#    if i!=0:
#        if a[i]==a[i-1]:  
#            continue 
#    p=0
#    for j in range(i,len(a)):
#        if a[i]==a[j]:
#            p+=1
#        else:
#            break
#    s+='('+str(p)+', '+a[i]+')'+' '
#print(s) 