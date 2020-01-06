#Sample Input

#10
#161 182 161 154 176 170 167 171 170 174
#Sample Output

#169.375

s=int(input())
#x = list(map(int, input().split()))
x = set(map(int, input().split()))
print(x)
#x =set(x)
#print(x)
print(sum(x)/len(x))






def average(array):
    
    
    return sum(set(array))/len(set(array))

n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)