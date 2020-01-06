

#Sarcină

#Vi se dau două valori a și b.
#Efectuați diviziunea întreagă și imprimați a / b.

#Format de iesire

#Imprimați valoarea a / b.
#În cazul ZeroDivisionError sau ValueError, imprimați codul de eroare.

#Sample Input

#3
#1 0
#2 $
#3 1
#Sample Output

#Error Code: integer division or modulo by zero
#Error Code: invalid literal for int() with base 10: '$'
#3
#a, b = int(input()), int(input())
#print(a//b)


#metoda 1
for i in range(int(input())):
 
 try:
    a,b = map(int,input().split())
    print(a//b)
 except ZeroDivisionError as e:
    print("Error Code: ",e)


 except ValueError as e:
   print("Error Code: ", e)

#metoda 2
for i in range(int(input())):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)
