

#Vi se dau n cuvinte. Unele cuvinte se pot repeta. Pentru fiecare cuvânt, emiteți numărul său de apariții. 
#Ordinea de ieșire ar trebui să corespundă cu ordinea de apariție a cuvântului. 
#Consultați intrarea / ieșirea eșantionului pentru clarificări.

#Formatul de intrare

#Prima linie conține numărul întreg, n.
#Următoarele n linii conțin fiecare un cuvânt.

#Ieșire 2 linii.
#Pe prima linie, emiteți numărul de cuvinte distincte din intrare.
#Pe a doua linie, emiteți numărul de apariții pentru fiecare cuvânt distinct, în funcție de aspectul lor în intrare.

#Sample Input

#4
#bcdef
#abcdefg
#bcde
#bcdef

#Sample Output

#3
#2 1 1

from collections import Counter, OrderedDict

#class OrderedCounter(Counter, OrderedDict):
#    pass
#d = OrderedCounter(input() for _ in range(int(input())))
#print(len(d))
#print(*d.values())

#metoda 2
words = OrderedDict()

for _ in range(int(input())):
    word = input()
    
    words.setdefault(word, 0)
    words[word] += 1
 
print(words)    
print(len(words))
print(*words.values())


##metoda 3
##define empty ordered dictionary, which counts occurences
#dict = OrderedDict()

#for i in range(int(input())):
#    #If input not in the dictionary, then add it
#    #else increment the counter
#    key = input()
#    if not key in dict.keys():
#        dict.update({key : 1})
#        continue
#    dict[key] += 1

#print(len(dict.keys()))
#print(*dict.values())

##metoda 4
#l={}
#for i in range(int(input())):
#    x=input()
#    if x not in l:
#        l[x]=1
#    else:
#        l[x]=l[x]+1
#print(len(l))
#for i in l:
#    print(l[i],end=" ") 