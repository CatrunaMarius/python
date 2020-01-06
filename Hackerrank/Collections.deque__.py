
#Sarcină

#Efectuați metode de atașare, pop, popleft și apendleft pe un dispozitiv gol d.

#Formatul de intrare

#Prima linie conține un număr întreg N, numărul de operații.
#Următoarele N linii conțin numele de metode și valorile lor separate în spațiu.

#Format de iesire

#Imprimați elementele separate ale spațiului de deque.

#Sample Input

#6
#append 1
#append 2
#append 3
#appendleft 4
#pop
#popleft
#Sample Output

#1 2

from collections import deque


#metoda 1
print("=== metoda 1 ===")
d = deque()
for _ in range(int(input())):
        func, *args = input().split()
        getattr(d, func)(*args)
print(*d)

#metoda 2
print("=== metoda 2 ===")
d = deque()
for _ in range(int(input())):
    eval('d.{0}({1})'.format(*input().split(), '')) 
print(*d)

#metode 3
print("=== metoda 3 ===")
d = deque()
for _ in range(int(input())):
    command, *args = input().split()
    getattr(d, command)(*map(int, args))
print(*d)

#metoda 4 pt incepatori
print("=== metoda 4 ===")
d = deque()
for _ in range(int(input())):
    line = input().split()
    if line[0] == 'append':
        d.append(line[1])
    elif line[0] == 'pop':
        d.pop()
    elif line[0] == 'popleft':
        d.popleft()
    elif line[0] == 'appendleft':
        d.appendleft(line[1])
print(*d)

#metoda 5 pentru incepatori
print("=== metoda 5 ===")
import re;
d = deque();
n = int(input());
str_val = '';
for i in range(n):
    key = input();
    number = re.match(r'(\w+)\s?(\d+)?',key);
    if(number):
        case = number.group(1);
        add = number.group(2);
        if(case == 'append'):
            d.append(add);
        elif(case == 'appendleft'):
            d.appendleft(add);
        elif(case == 'pop'):
            d.pop();
        elif(case == 'popleft'):
            d.popleft();
for j in d:
    str_val = str_val+' '+j;
str_val = re.sub(r'(^ )',"",str_val);
print(str_val);



#metoda 6
print("=== metoda 6 ===")
d = deque()
for _ in range(int(input())):
    inp = input().split()
    getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
print(*[item for item in d])