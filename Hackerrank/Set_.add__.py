#Sample Input

#7
#UK
#China
#USA
#France
#New Zealand
#UK
#France 
#Sample Output

#5
i = input()
s = set()

for _ in range(int(i)):
    s.add(input().strip())
    
print(len(s))



#print (len(set([ input().strip() for _ in range(int(input().strip())) ])))