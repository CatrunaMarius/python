

#Vi se oferă un fragment de cod HTML de N linii.
#Sarcina dvs. este să detectați și să imprimați toate etichetele HTML, atributele și valorile atributelor.

#Tipăriți elementele detectate în următorul format:

#Tag1
#Tag2
#-> Attribute2[0] > Attribute_value2[0]
#-> Attribute2[1] > Attribute_value2[1]
#-> Attribute2[2] > Attribute_value2[2]
#Tag3
#-> Attribute3[0] > Attribute_value3[0]


#Simbolul -> indică faptul că eticheta conține un atribut. Este urmat imediat de numele atributului și de valoarea atributului.
#Simbolul> acționează ca un separator de atribute și valori de atribut.

#Dacă o etichetă HTML nu are atribut, atunci pur și simplu imprimați numele etichetei.

#Notă: Nu detectați nicio etichetă HTML, atribut sau valoare de atribut în etichetele de comentarii HTML (<! - Comentarii ->). Comentariile pot fi multiline.
#Toate atributele au o valoare a atributului.

#Formatul de intrare

#Prima linie conține un număr întreg N, numărul de linii din fragmentul de cod HTML.
#Următoarele N linii conțin cod HTML.

#Format de iesire

#Tipăriți etichetele HTML, atributele și valorile atributelor în ordinea apariției lor de sus în jos în fragment.

#Formatați-vă răspunsurile așa cum este explicat în enunțul de probleme.

#Sample Input

#9
#<head>
#<title>HTML</title>
#</head>
#<object type="application/x-flash" 
#  data="your-file.swf" 
#  width="0" height="0">
#  <!-- <param name="movie" value="your-file.swf" /> -->
#  <param name="quality" value="high"/>
#</object>
#Sample Output

#head
#title
#object
#-> type > application/x-flash
#-> data > your-file.swf
#-> width > 0
#-> height > 0
#param
#-> name > quality
#-> value > high


#Explicaţie

#head tag: Tipăriți eticheta de cap doar pentru că nu are atribut.

#title tag: Tipăriți eticheta pentru titlu doar pentru că nu are atribut.

#obiect tag: Imprima eticheta obiect. În următoarele 4 linii, imprimați tipul, datele, lățimea și înălțimea atributelor împreună cu valorile respective.

#<! - Comentariu -> etichetă: Nu detectați nimic în interior.

#tag param: Tipăriți eticheta param. În următoarele 2 rânduri, imprimați numele atributelor împreună cu valorile respective.
#metoda 1
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

parser = MyHTMLParser()

for i in range(int(input())):
    parser.feed(input())

#metoda 2
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]
        
html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#metoda 3
import re

text = ''
for _ in range(int(input())):
    text = re.sub(r'<!.+-->',r' ',(text+input()))

for er in re.findall(r'<([^/][^>]*)>', text):
    if ' ' in er:       
        for ere in re.findall(r'([a-z]+)? *([a-z-]+)="([^"]+)', er):
            if ere[0]:
                print(ere[0])          
            print('-> '+ere[1]+' > '+ere[2])
    else:
        print(er)



#metoda 4

from html.parser import HTMLParser
HTML = ''
for i in range(int(input())):
    HTML += input()
class tag(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            print(*['-> ' + attr[0]+ ' > ' + attr[1] for attr in attrs],sep='\n')

parser = tag()
parser.feed(HTML)