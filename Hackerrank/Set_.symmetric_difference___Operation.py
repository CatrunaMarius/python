
#Output Format

#Output total number of students who have subscriptions to the English or the French newspaper but not both.

#Sample Input

#9
#1 2 3 4 5 6 7 8 9
#9
#10 1 2 3 11 21 55 6 8
#Sample Output

#8

_ , x = input(), set(input().split())
_ , y = input(), set(input().split())
print(len(x.symmetric_difference(y))) 