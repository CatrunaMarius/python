
#Task

#You are given a date. Your task is to find what the day is on that date.

#Sample Input

#08 05 2015
#Sample Output

#WEDNESDAY

#metoda 1 incepatori
print("=== metoda 1 ===")
import calendar
#calendar.Calendar(calendar.SUNDAY)
user_input = input().split()
month = int(user_input[0])
day = int(user_input[1])
year = int(user_input[2])
c = calendar.weekday(year, month, day)

if c == 0:
    print("MONDAY")
elif c == 1:
    print("TUESDAY")
elif c == 2:
    print("WEDNESDAY")
elif c==3:
    print("THURSDAY")
elif c==4:
    print("FRIDAY")
elif c== 5:
    print("SATURDAY")
elif c==6:
    print("SUNDAY")

#metoda 2
print("=== metoda 2 ===")
import calendar
m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())

#metoda 3
print("=== metoda 3 ===")
import datetime

print(datetime.datetime.strptime(input(), '%m %d %Y').strftime('%A').upper())

#metoda 4
print("=== metoda 4 ===")
import calendar as ca
d,m,y = ([int(i) for i in input().split(' ')])
a = ca.weekday(y,d,m)
n = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
print( n[a])

#metoda 5
print("=== metoda 5 ===")
import calendar

string = list(map(int,input().split()))
day_num = calendar.weekday(string[2], string[0], string[1])
print((calendar.day_name[day_num]).upper())