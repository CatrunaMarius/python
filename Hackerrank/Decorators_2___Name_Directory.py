
#Să folosim decoratori pentru a construi un director de nume! Vi se oferă câteva informații despre oameni. Fiecare persoană are un nume, prenume, vârstă și sex. Tipăriți numele lor într-un format specific, ordonat în funcție de vârstă în ordine crescătoare, adică numele celui mai tânăr trebuie tipărit mai întâi. Pentru două persoane de aceeași vârstă, imprimați-le în ordinea introducerii lor.

#Pentru Henry Davids, producția ar trebui să fie:
#    Mr. Henry Davids
#For Mary George, the output should be:

#Ms. Mary George


#Formatul de intrare

#Prima linie conține numărul întreg N, numărul de persoane.
#N linii urmează fiecare care conține valorile spațiale ale prenumelui, prenumelui, vârstei și, respectiv, sex.

#Format de iesire

#Nume de ieșire pe linii separate în formatul descris mai sus, în ordinea crescândă a vârstei.

#Sample Input

#3
#Mike Thomson 20 M
#Robert Bustle 32 M
#Andria Bustle 30 F
#Sample Output

#Mr. Mike Thomson
#Ms. Andria Bustle
#Mr. Robert Bustle

#Sample Input (stdin)

#10
#Blossom Blossom 10 F
#Bubbles Blossom 10 F
#Buttercup Blossom 9 F
#Blossom Bubbles 10 F
#Bubbles Bubbles 10 F
#Buttercup Bubbles 200 F
#Blossom Buttercup 30 F
#Bubbles Buttercup 30 F
#Buttercup Buttercup 10 F
#Butterblossom Bubblescup 10 F

#Expected Output

#Ms. Buttercup Blossom
#Ms. Blossom Blossom
#Ms. Bubbles Blossom
#Ms. Blossom Bubbles
#Ms. Bubbles Bubbles
#Ms. Buttercup Buttercup
#Ms. Butterblossom Bubblescup
#Ms. Blossom Buttercup
#Ms. Bubbles Buttercup
#Ms. Buttercup Bubbles
#Concept

#Pentru a sorta o listă cuibărită pe baza unui anumit parametru, puteți utiliza biblioteca de setări de elemente. Puteți citi mai multe despre asta aici.


import operator

def person_lister(f):
    def inner(people):
        # complete the function
        
        for ps in sorted(people, key=lambda x: int(x[2])):
            yield f(ps) 
        #metoda 2
        return (f(spers) for spers in sorted((person[:2]+[int(person[2])]+person[3:]+[idx] for idx, person in enumerate(people)), key=operator.itemgetter(2, 4)))             
        #metoda dar rezultatul care trebuie dar e foarte inceata
        return map(f, sorted(people, key=lambda x: x[2]))

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

#metoda 3
import operator
from functools import cmp_to_key
def my_sort_func(l1, l2):
    if int(l1[2]) < int(l2[2]):
        return -1
    
    if int(l1[2]) > int(l2[2]):
        return 1

    return 0

def person_lister(f):
    def inner(people):
    
      people.sort(key=cmp_to_key(my_sort_func))
        
      output = []
      for person in people:
            output.append(f(person))
        
      return output
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

#metoda 4
def age(x):
    return int(x[2])

def person_lister(f):
    def inner(people):
        return map(f,sorted(people, key=age))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')