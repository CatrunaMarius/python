
#Domnul Anant Asankhya este administratorul hotelului INFINITE. Hotelul are o cantitate infinită de camere.

#Într-o zi frumoasă, un număr finit de turiști vin să stea la hotel.
#Turistii constau din:
#→ Un căpitan.
#→ Un grup necunoscut de familii format din K din membri pentru fiecare grup în care K ≠ 1.

#Căpitanului i s-a oferit o cameră separată, iar restului li s-a oferit o cameră per grup.

#Domnul Anant are o listă neordonată de intrări ale camerei aranjate la întâmplare. 
#Lista constă din numerele de cameră pentru toți turiștii. 
#Numerele camerei vor apărea de K ori pe grup, cu excepția camerei căpitanului.

#Domnul Anant are nevoie să îl ajute să găsească numărul camerei căpitanului.
#Nu vă este cunoscut numărul total de turiști sau numărul total de grupuri de familii.
#Nu știți decât valoarea lui K și lista numerelor camerei.


#Sample Input

#5
#1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
#Sample Output

#8


k = int(input())
arr=list(map(int, input().split()))
myset = set(arr)
print(arr)
print(myset)
print(sum(myset)*k)
print(sum(arr))



print(((sum(myset)*k)-(sum(arr)))//(k-1))

#metoda 2

#nom = int(input())
#members = list( input().split())
#rooms = set()   # Contains all the rooms.
#room_more_mem = set()   # Contains only the rooms with families.

#for m in members:
#        if m not in rooms:
#                rooms.add(m)
#        else:
#                room_more_mem.add(m)
#print(rooms.difference(room_more_mem).pop())

#metoda 3
#k = int(input())
#L = str(input()).split(" ")
#family = L
#total = set(L)
#for r in set(L): 
#    try:
#        family.remove(r)
#    except:
#        pass
#print ("".join((total - set(family))))

#metoda 4
#get inputs from stdin
#input()
#group = input().strip().split()
#rooms = set(group)
##remove set of rooms from original group
#for r in rooms:
#    group.remove(r) 
##the new set should not contain the captain room 
#non_captain = set(group)
##print the poped only remaining element from difference
#print(rooms.difference(non_captain).pop())

#metoda 5
#_ = input()
#a = input().split()
#s = set()
#t = set()
#for i in a:
#    if i not in s:
#        s.add(i)
#        t.add(i) 
#    else:
#        t.discard(i)
#print(t.pop())