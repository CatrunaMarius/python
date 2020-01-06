#hackerrank
#Sample Input 0
#2
#1 2
#Sample Output 0
#3713081631934410656

#metoda advansata
n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(hash(t))

#metoda simpla
n = int(input())
input_list= input().split()
#for i in range(n): sau
for i in range(len(input_list)):
    input_list[i]= int(input_list[i])
t = tuple(input_list)
print(hash(t))