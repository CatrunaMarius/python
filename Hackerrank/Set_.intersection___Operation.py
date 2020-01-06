

#Sarcină
#Studenții District College au abonamente la ziarele engleze și franceze. 
#Unii studenți s-au abonat doar la engleză, alții s-au abonat doar la franceză, iar alții s-au abonat la ambele ziare.

#Vi se oferă două seturi de numere de rol. Un set s-a abonat la ziarul englez, un set s-a abonat la ziarul francez.
# Sarcina dvs. este să găsiți numărul total de studenți care s-au abonat la ambele ziare.

#Formatul de intrare

#Prima linie conține n, numărul de studenți care s-au abonat la ziarul englez.
#A doua linie conține n numere de roluri separate în spațiu ale elevilor.
#A treia linie conține b, numărul de studenți care s-au abonat la ziarul francez.
#Cea de-a patra linie conține numere de roluri separate în spațiu ale elevilor.
#Output Format

#Output the total number of students who have subscriptions to both English and French newspapers.


#Sample Input

#9
#1 2 3 4 5 6 7 8 9
#9
#10 1 2 3 11 21 55 6 8
#Sample Output

#5

_ , a = input() , set(input().split())
_ , b = input() , set(input().split())
print(len(a.intersection(b)))