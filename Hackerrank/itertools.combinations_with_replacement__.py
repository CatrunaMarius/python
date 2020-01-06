from itertools import combinations_with_replacement as comb

#s, k = input().split()
#for i in comb(sorted(s), int(k)):
#    print(''.join(i))

#metoda 2 cu join este mai rapd decat ce este aici
#s, k = input().split()
#for el in comb (sorted(s),int(k)):
#    print(*el, sep='')

#metoda 3
#s, k = input().split() 
#print(*[''.join(p) for p in comb(sorted(s), int(k))], sep='\n')

#metoda 4
#s = input().split()
#string, number = sorted(s[0]), int(s[1])
#print(*list(map(''.join, comb(string, number))), sep='\n')

#metoda 4.1
s,k = input().split()
print(*map(''.join, comb(sorted(s),int(k))),sep='\n')