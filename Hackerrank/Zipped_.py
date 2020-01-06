
#Sarcină

#Universitatea Națională efectuează un examen de N studenți la X subiecți.
#Sarcina ta este să calculezi scorurile medii ale fiecărui student.

#Formatul de intrare

#Prima linie conține N și X separate de un spațiu.
#Următoarele N linii conțin notele separate în spațiu obținute de studenți la un anumit subiect.

#Sample Input

#5 3
#89 90 78 93 80
#90 91 85 88 86  
#91 92 83 89 90.5
#Sample Output

#90.0 
#91.0 
#82.0 
#90.0 
#85.5   

#metoda 1
n, x = map(int, input().split()) 

sheet = []
for _ in range(x):
    sheet.append( map(float, input().split()) ) 

for i in zip(*sheet): 
    print( sum(i)/len(i) )

#metoda 2
[print(sum(i) / len(i) ) for i in zip( *[map(float, input().split()) for _ in range(int(input().split()[1])) ] ) ]

#metod 3
a,y = map(int, input().split())
scores = [map(float, input().split()) for _ in range(y)]

[print(sum(student)/y) for student in zip(*scores)]
