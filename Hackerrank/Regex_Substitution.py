

#Instrumentul re.sub () (sub înseamnă substituție) evaluează un model și, pentru fiecare potrivire valabilă, apelează la o metodă (sau lambda).
#Metoda este apelată la toate meciurile și poate fi utilizată pentru a modifica șiruri în moduri diferite.
#Metoda re.sub () returnează șirul modificat ca o ieșire.

#Aflați mai multe despre re.sub ().

#Transformarea corzilor

#Cod

#import re

##Squaring numbers
#def square(match):
#    number = int(match.group(0))
#    return str(number**2)

#print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")

#Output

#1 4 9 16 25 36 49 64 81

#Replacements in Strings

#Code

#import re

#html = """
#<head>
#<title>HTML</title>
#</head>
#<object type="application/x-flash" 
#  data="your-file.swf" 
#  width="0" height="0">
#  <!-- <param name="movie"  value="your-file.swf" /> -->
#  <param name="quality" value="high"/>
#</object>
#"""

#print re.sub("(<!--.*?-->)", "", html) #remove comment
#Output

#<head>
#<title>HTML</title>
#</head>
#<object type="application/x-flash" 
#  data="your-file.swf" 
#  width="0" height="0">

#  <param name="quality" value="high"/>
#</object>


#Sarcină

#Vi se oferă un text de N linii. Textul conține && și || simboluri.
#Sarcina dvs. este de a modifica aceste simboluri la următoarele:

#&& → și
#|| → sau
#Atât && cât și || ar trebui să aibă un spațiu "" pe ambele părți.

#Output Format

#Output the modified text.
#Sample Input

#11
#a = 1;
#b = input();

#if a + b > 0 && a - b < 0:
#    start()
#elif a*b > 10 || a/b < 1:
#    stop()
#print set(list(a)) | set(list(b)) 
##Note do not change &&& or ||| or & or |
##Only change those '&&' which have space on both sides.
##Only change those '|| which have space on both sides.
#Sample Output

#a = 1;
#b = input();

#if a + b > 0 and a - b < 0:
#    start()
#elif a*b > 10 or a/b < 1:
#    stop()
#print set(list(a)) | set(list(b)) 
##Note do not change &&& or ||| or & or |
##Only change those '&&' which have space on both sides.
##Only change those '|| which have space on both sides.    

import re

s= int(input())
for i in range(s):
    print( re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))



#metoda 3
for _ in range(int(input())):
        s = input()
        s = re.sub(r" \&\&(?= )", " and", s)
        s = re.sub(r" \|\|(?= )", ' or', s)
        print(s)

#metoda 4
for _ in range(int(input())):
    print(re.sub(r' [|]{2}(?= )', ' or', re.sub(r' [&]{2}(?= )', ' and', input())))

#metoda 5
for _ in range(int(input())):
    line = input()
    
    while ' && ' in line or ' || ' in line:
        line = line.replace(" && ", " and ").replace(" || ", " or ")
    
    print(line)