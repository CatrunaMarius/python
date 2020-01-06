#utput Format

#Print True if set  is a strict superset of all other  sets. Otherwise, print False.

#Sample Input 0

#1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
#2
#1 2 3 4 5
#100 11 12
#Sample Output 0

#False

#metoda 1
#a = set(input().split())
#print(all(a > set(input().split()) for _ in range(int(input()))))

#metoda 2
a = set(map(str, input().split(' ')))
is_strict_superset = []
for i in range(int(input())):
     is_strict_superset.append(a.issuperset(set(map(str, input().split(' ')))))
print(all(is_strict_superset))