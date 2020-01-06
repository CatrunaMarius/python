
#Output Format

#Output True or False for each test case on separate lines.

#Sample Input

#3
#5
#1 2 3 5 6
#9
#9 8 5 6 3 2 1 4 7
#1
#2
#5
#3 6 5 4 1
#7
#1 2 3 5 6 8 9
#3
#9 8 2
#Sample Output

#True 
#False
#False

for _ in range(int(input())):
    _, a = input(), set(input().split())
    _, b = input(), set(input().split())
 
    print(a.issubset(b))

