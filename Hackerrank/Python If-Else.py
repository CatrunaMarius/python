import sys


N = int(raw_input().strip())

if N % 2 == 0:
    if N >= 2 and N <= 5:
        print "Not Weird"
    elif N >= 6 and N <= 20:
        print "Weird"
    elif N > 20:
        print "Not Weird"
else:
     print "Weird"

'''
utput Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

3

Sample Output 0

Weird

Explanation 0
n=3
n is odd and odd numbers are weird, so we print Weird.

Sample Input 1

24

Sample Output 1

Not Weird

Explanation 1
n=24
n>20  and n is even, so it isn't weird. Thus, we print Not Weird.
'''