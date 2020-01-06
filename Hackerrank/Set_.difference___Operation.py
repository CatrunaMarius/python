

#Output Format

#Output the total number of students who are subscribed to the English newspaper only.

#Sample Input

#9
#1 2 3 4 5 6 7 8 9
#9
#10 1 2 3 11 21 55 6 8
#Sample Output

#4

_ , x = input(), set(input().split())
_ , y = input(), set(input().split())
print(len(x.difference(y)))