

#Având în vedere numele și notele pentru fiecare student dintr-o clasă de fizică a N studenți,
# stocați-le într-o listă cuibărită și imprimați numele (ele) oricărui elev (i) care are a doua notă cea mai mică.

#Notă: Dacă există mai mulți studenți cu aceeași notă, ordonați-le numele alfabetic și imprimați fiecare nume pe o nouă linie.

#Formatul de intrare

#Prima linie conține un număr întreg, N, numărul de studenți.
#Rândurile 2N ulterioare descriu fiecare elev peste 2 linii; prima linie conține numele unui elev, iar a doua linie conține nota lor.
#Format de iesire

#Tipăriți numele (elevii) oricărui student (i) care are a doua notă de fizică;
# dacă există mai mulți studenți, ordonați-le numele în ordine alfabetică și imprimați-le pe fiecare linie nouă.

#Sample Input 0

#5
#Harry
#37.21
#Berry
#37.21
#Tina
#37.2
#Akriti
#41
#Harsh
#39
#Sample Output 0

#Berry
#Harry
#Sample input 1
#5
#Harsh
#20
#Beria
#20
#Varun
#19
#Kakunami
#19
#Vikas
#21
#Sample Output1
#Beria
#Harsh
#marks=[]
#studentScore = []
#for _ in range(int(input())):
#        #inputurile nume si scorul
#        name = input()
#        score = float(input())
#        #creaza un counter care tine evidenta fiecaru student ajuta sa adugam un student nou in lista
#        #creand pt fiecare student nou o lista cu numele si scorul optinut
#        marks += [[name, score]]
#        print(marks)
#        #conter care tine evidenta scolului fiecarui student
#        studentScore += [score]
#        print(type(studentScore))


#studentScore = list(dict.fromkeys(studentScore))
##print('sort list: ',type(studentScore) )
##creare unei liste sortata a studentScore
#b=sorted(studentScore)

#print('sort list: ',b)
#b1=sorted(studentScore)[1]

#for a,c in sorted(marks):
#    if c==b1:
#        print(a)

#metoda 2

marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])
    print(marksheet)

second_highest = sorted(list(set([marks for name, marks in marksheet])))#[1]
print(second_highest)
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))