

# Învățați să pronunțați
#.handle_comment (date)
#Această metodă este numită atunci când este întâlnit un comentariu (de ex. <! - comentariu ->).
#Argumentul de date este conținutul din eticheta de comentariu:

#.handle_data (date)
#Această metodă este apelată la procesarea datelor arbitrare (de exemplu, nodurile text și conținutul <script> ... </script> și <style> ... </style>).
#Argumentul de date este conținutul textului HTML.

#Sarcină

#Vi se oferă un fragment de cod HTML de N linii.
#Sarcina dvs. este de a imprima comentariile cu o singură linie, comentariile cu mai multe linii și datele.

#Tipăriți rezultatul în următorul format:

#Notă: Nu imprimați date dacă date == '\ n'.

#Formatul de intrare

#Prima linie conține N întreg, numărul de linii din fragmentul de cod HTML.
#Următoarele N linii conțin cod HTML.

#Format de iesire

#Imprimați comentariile cu o singură linie, comentariile cu mai multe linii și datele în ordinea apariției acestora de sus în jos în fragment.

#Formatați răspunsurile așa cum este explicat în enunțul problemei.

#Sample Input

#4
#<!--[if IE 9]>IE9-specific content
#<![endif]-->
#<div> Welcome to HackerRank</div>
#<!--[if IE 9]>IE9-specific content<![endif]-->
#Sample Output

#Multi-line Comment
#[if IE 9]>IE9-specific content
#<![endif]
#Data
# Welcome to HackerRank
#Single-line Comment
#[if IE 9]>IE9-specific content<![endif]

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
     def handle_comment(self, data):
          number_of_line = len(data.split('\n'))
          if number_of_line>1:
            print('>>> Multi-line Comment')
          else:
            print('>>> Single-line Comment')
          if data.strip():
            print(data)
     
     def handle_data(self, data):
         if data.strip():
             print (">>>Data\n", data)
  
  
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#metoda 2
class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        if '\n' in comment:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
            
        print(comment)
    
    def handle_data(self, data):
        if data == '\n': return
        print('>>> Data')
        print(data)

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#metoda 3
class MyHTMLParser(HTMLParser):
        def handle_comment(self, data):
                if "\n" in data:
                        print(">>> Multi-line Comment  ", data, sep="\n")
                else:
                        print(">>> Single-line Comment  ", data, sep="\n")
        def handle_data(self, data):
                if data != "\n":
                        print(">>> Data", data, sep="\n")

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#metoda 4
import sys
from html.parser import HTMLParser

class P(HTMLParser):
  def handle_comment(self, data):
      c = 'Multi' if '\n' in data else 'Single'
      print('>>> {}-line Comment\n{}'.format(c, data.rstrip()))
      
  def handle_data(self, data):
    if len(data) > 2:
      print('>>> Data\n{}'.format(data.rstrip()))

p = P()
p.feed(sys.stdin.read())

#metoda 5
import re
def handle_data(self, data):
	regex = re.compile(r'\S+')
	if regex.search(data):
		print(">>> Data")
		print(data)
def handle_comment(self, data):
	regex = re.compile(r'\n+')
	if regex.search(data): print(">>> Multi-line Comment")
        else: print(">>> Single-line Comment")
        print(data)

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()