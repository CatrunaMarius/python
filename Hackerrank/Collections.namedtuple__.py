

#Dr. John Wesley are o foaie de calcul care conține o listă de identificare, mărci, clasă și nume ale studentului.

#Sarcina ta este de a ajuta Dr. Wesley să calculeze notele medii ale studenților.
#Formatul de intrare

#Prima linie conține un număr întreg N, numărul total de studenți.
#A doua linie conține numele coloanelor în orice ordine.
#Următoarele N linii conțin mărci, ID-uri, nume și clasă, sub numele lor de coloană.

#Sample Input

#TESTCASE 01

#5
#ID         MARKS      NAME       CLASS     
#1          97         Raymond    7         
#2          50         Steven     4         
#3          91         Adrian     9         
#4          72         Stewart    5         
#5          80         Peter      6   
#TESTCASE 02

#5
#MARKS      CLASS      NAME       ID        
#92         2          Calum      1         
#82         5          Scott      2         
#94         2          Jason      3         
#55         8          Glenn      4         
#82         2          Fergus     5
#Sample Output

#TESTCASE 01

#78.00
#TESTCASE 02

#81.00

from collections import namedtuple
#metoda 1
n = int(input())
a = input()
total = 0
Student = namedtuple('Student', a)
#print(Student)
for _ in range(n):
    student = Student(*input().split())
    total += int(student.MARKS)
print('{:.2f}'.format(total/n))

#metoda 2
(n, categories) = (int(input()), input().split())
Grade = namedtuple('Grade', categories)
marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]
print((sum(marks) / len(marks)))

#metoda 3
N = int(input())
fields = input().split()

total = 0
for i in range(N):
    students = namedtuple('student',fields)
    field1, field2, field3,field4 = input().split()
    student = students(field1,field2,field3,field4)
    total += int(student.MARKS)
print('{:.2f}'.format(total/N))


#metoda 4
#import collections, statistics
#print('%.2f' % statistics.mean(next((int(student(*row).MARKS) for row in (input().split() for i in range(size))) for size, student in [[int(input()), collections.namedtuple('Student', input())]])))