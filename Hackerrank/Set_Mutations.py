
#Output Format

#Output the sum of elements in set .

#Sample Input

# 16
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
# 4
# intersection_update 10
# 2 3 5 6 8 9 1 4 7 11
# update 2
# 55 66
# symmetric_difference_update 5
# 22 7 35 62 58
# difference_update 7
# 11 22 35 55 58 62 66
#Sample Output

#38

#(_, A) = (int(input()),set(map(int, input().split())))
#B = int(input())
#for _ in range(B):
#        (command, newSet) = (input().split()[0],set(map(int, input().split())))
#        getattr(A, command)(newSet)

#print (sum(A))

#metoda 2
#m, base_set = input(), set(map(int, input().split()))
#for i in range(0,int(input())):
#    exec("base_set.{0}({1})".format(input().split()[0], set(map(int, input().split())) ))
#print(sum(base_set))

#metoda 3
#_, L = input(), set(input().split())
#for _ in range(int(input())):
#    getattr(L, input().split()[0])(set(input().split()))
#print(sum(map(int, L)))

#metoda 4
_ = int(input())
s1 = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    cmd, _ = input().split()
    s2 = set(map(int, input().split()))
    if(cmd == "intersection_update"):
        s1.intersection_update(s2)
    elif(cmd == "update"):
        s1.update(s2)
    elif(cmd == "symmetric_difference_update"):
        s1.symmetric_difference_update(s2)
    elif(cmd == "difference_update"):
        s1.difference_update(s2)

print(sum(s1))