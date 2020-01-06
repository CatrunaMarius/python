#hackerrang

n = int(input())
student_marks = {}
for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
query_name = input()
marks = student_marks[query_name]
print("%.2f"%(sum(marks)/3))

#metoda 2
marks = {}
for _ in range(int(input())):
    #inputul numele si notele optinute la cele 3 dispicpline
    line = input().split()
    #este creat un dictionar care va cuprinde toate 
     #line[0] reprenita variamila name iar cea ce urmeaza dupa egal sunt artibutori valori 
    marks[line[0]] = list(map(float, line[1:]))
print('%.2f' %(sum(marks[input()])/3))