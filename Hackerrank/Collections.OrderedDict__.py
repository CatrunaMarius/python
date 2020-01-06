
#Sunteți managerul unui supermarket.
#Aveți o listă de N articole împreună cu prețurile lor pe care consumatorii le-au cumpărat într-o anumită zi.
#Sarcina dvs. este să imprimați fiecare item_name și net_price în ordinea primei apariții.

#Formatul de intrare

#Prima linie conține numărul de articole, N.
#Următoarele N linii conțin numele și prețul articolului, separate printr-un spațiu.




#Sample Input

#9
#BANANA FRIES 12
#POTATO CHIPS 30
#APPLE JUICE 10
#CANDY 5
#APPLE JUICE 10
#CANDY 5
#CANDY 5
#CANDY 5
#POTATO CHIPS 30
#Sample Output

#BANANA FRIES 12
#POTATO CHIPS 60
#APPLE JUICE 20
#CANDY 20

from collections import OrderedDict 

#metoda 1
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    #print(item, space, quantity)
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)

#metoda 2
od = OrderedDict()
for i in range(int(input())):
  *item, price = input().split()
  item = ' '.join(item)
  od.setdefault(item, 0)
  od[item] = od[item] + int(price)
for k,v in od.items():
  print(k + ' ' + str(v))

#metoda 3
number_ = int(input())
odict = OrderedDict()
for i in range(number_):
    litem = input().split(' ')
    #print(litem)
    price = int(litem[-1])
    item_name = " ".join(litem[:-1])
    if odict.get(item_name):
        odict[item_name] += price
    else:
        odict[item_name] = price

for i,v in odict.items():
    print(i,v)
#metoda 4
def convert(val):
    m = {
            list: lambda x: " ".join(x),
            str: lambda x: int(x)
        }
    return m[type(val)](val)

d = OrderedDict()
num_items = int(input())

for _ in range(num_items):
    *head, tail = input().split()
    item_name, item_price = map(lambda x: convert(x), [head, tail])
    d[item_name] = d.get(item_name, 0) + item_price

for k, v in d.items():
    print(k,v)