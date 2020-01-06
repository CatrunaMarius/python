
#Sarcină
#Aveți un set ne gol, și trebuie să executați N comenzi date în N linii.

#Comenzile vor fi pop, ștergeți și aruncați.

#Formatul de intrare

#Prima linie conține n număr întreg, numărul de elemente din setul s.
#A doua linie conține n elemente separate în spațiu ale setului s. Toate elementele sunt numere întregi non-negative, mai mici sau egale cu 9.
#A treia linie conține numărul întreg N, numărul de comenzi.
#Următoarele N linii conțin fie comenzi pop, eliminare și / sau eliminare urmate de valoarea lor asociată.

#Sample Input

#9
#1 2 3 4 5 6 7 8 9
#10
#pop
#remove 9
#discard 9  
#discard 8
#remove 7
#pop 
#discard 6
#remove 5
#pop 
#discard 5
#Sample Output

#4

n = int(input())
s = set(map(int, input().split())) 
#for i in range(int(input())):
#    eval('s.{0}({1})'.format(*input().split()+['']))

#print(sum(s)) 


#metoda 2
#methods = {
#    'pop' : s.pop,
#    'remove' : s.remove,
#    'discard' : s.discard
#}
#args = None
#for _ in range(int(input())):
## 5
#    method, *args = input().split()

#    if len(args) > 1:
#        [methods[method](*map(int, arg)) for arg in args]
#    else:
#        methods[method](*map(int, args))

#print(sum(s))



N=int(input())

for i in range(N) :

  choice=input().split()
  if choice[0]=="pop" :
    s.pop()
  elif choice[0]=="remove" :
    s.remove(int(choice[1]))
  elif choice[0]=="discard" :
    s.discard(int(choice[1]))
print (sum(s))