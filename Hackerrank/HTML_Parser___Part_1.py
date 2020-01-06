
"""#HTML
#Hypertext Markup Language este un limbaj de marcare standard utilizat pentru crearea de pagini Web World Wide.

#Analizare
#Parsingul este procesul de analiză sintactică a unui șir de simboluri. Implică rezolvarea unei șiruri în părțile sale componente și descrierea rolurilor lor sintactice.

#HTMLParser
#O instanță HTMLParser este alimentată cu date HTML și apelează la metodele de gestionare atunci când se întâlnesc etichete de pornire, etichete finale, text, comentarii și alte elemente de marcare.

#Exemplu (bazat pe documentația originală Python):

#Cod
#from HTMLParser import HTMLParser

## create a subclass and override the handler methods
#class MyHTMLParser(HTMLParser):
#    def handle_starttag(self, tag, attrs):
#        print "Found a start tag  :", tag
#    def handle_endtag(self, tag):
#        print "Found an end tag   :", tag
#    def handle_startendtag(self, tag, attrs):
#        print "Found an empty tag :", tag

## instantiate the parser and fed it some HTML
#parser = MyHTMLParser()
#parser.feed("<html><head><title>HTML Parser - I</title></head>"
#            +"<body><h1>HackerRank</h1><br /></body></html>")
#Output

#Found a start tag  : html
#Found a start tag  : head
#Found a start tag  : title
#Found an end tag   : title
#Found an end tag   : head
#Found a start tag  : body
#Found a start tag  : h1
#Found an end tag   : h1
#Found an empty tag : br
#Found an end tag   : body
#Found an end tag   : html


#.handle_starttag (tag, attrs)

#Această metodă este chemată să gestioneze eticheta de început a unui element. (De exemplu: <div class = 'marci'>)
#Argumentul etichetei este numele etichetei convertite în minuscule.
#Argumentul Attrs este o listă de (nume, valoare) perechi care conține atributele găsite în pachetele <> ale etichetelor.


#.handle_endtag (tag)

#Această metodă este chemată să gestioneze eticheta finală a unui element. (De exemplu: </div>)
#Argumentul etichetei este numele etichetei convertite în minuscule.


#.handle_startendtag (tag, attrs)

#Această metodă este chemată să gestioneze eticheta goală a unui element. (De exemplu: <br />)
#Argumentul etichetei este numele etichetei convertite în minuscule.
#Argumentul Attrs este o listă de (nume, valoare) perechi care conține atributele găsite în pachetele <> ale etichetelor.
"""

#Sarcină

#Vi se oferă un fragment HTML de linii N.
#Sarcina dvs. este de a tipări etichetele de început, etichetele finale și etichetele goale separat.

#Formatează-ți rezultatele în felul următor:

#Start : Tag1
#End   : Tag1
#Start : Tag2
#-> Attribute2[0] > Attribute_value2[0]
#-> Attribute2[1] > Attribute_value2[1]
#-> Attribute2[2] > Attribute_value2[2]
#Start : Tag3
#-> Attribute3[0] > None
#Empty : Tag4
#-> Attribute4[0] > Attribute_value4[0]
#End   : Tag3
#End   : Tag2


#Aici, simbolul -> indică faptul că eticheta conține un atribut. Este urmat imediat de numele atributului și de valoarea atributului.
#Simbolul> acționează ca un separator al atributului și a valorii atributului.

#Dacă o etichetă HTML nu are atribut, atunci pur și simplu imprimați numele etichetei.
#Dacă un atribut nu are o valoare a atributului, atunci imprimați pur și simplu numele valorii atributului ca Niciuna.

#Notă: Nu detectați nicio etichetă HTML, atribut sau valoare de atribut în etichetele de comentarii HTML (<! - Comentarii ->). Comentariile pot fi, de asemenea, multiline.

#Formatul de intrare

#Prima linie conține N întreg, numărul de linii dintr-un fragment de cod HTML.
#Următoarele N linii conțin cod HTML.

#Format de iesire

#Tipăriți etichetele HTML, atributele și valorile atributelor în ordinea apariției lor de sus în jos în fragmentul dat.

#Folosiți o formatare corectă, așa cum este explicat în declarația de probleme.

#Sample Input

#2
#<html><head><title>HTML Parser - I</title></head>
#<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
#Sample Output

#Start : html
#Start : head
#Start : title
#End   : title
#End   : head
#Start : body
#-> data-modal-target > None
#-> class > 1
#Start : h1
#End   : h1
#Empty : br
#End   : body
#End   : html

from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for ele in attrs:
            print('->',ele[0],'>',ele[1])
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for ele in attrs:
            print('->',ele[0],'>',ele[1])

#metoda 1
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
for _ in range(int(input())):
      parser.feed(input())

#metoda 2
parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())

#metodat 3 completa redefinita
import re

tag_filter = re.compile(r"(?<=<)(?:.*?)(?=>)")
attrib_filter = re.compile(r"([\w-]+)(?:=[\"'](.*?)[\"'])?")

s = ""

# get input stream
for _ in range(int(input())):
    s += input()

# discard comments
s = re.sub(r"(?:<!--(.|\s)*?(?:-->))","",s)

# extract individual tag information
tags = tag_filter.findall(s)

# iterate over the extracted tag information
for tag in tags:
    # tag handling logic
    if tag[0] == "/":
        print("End   :",tag[1:])
    else:
        attribs = attrib_filter.findall(tag)
        if tag[-1] == "/":
            print("Empty :",attribs[0][0])
        else:
            print("Start :",attribs[0][0])
            
        for i in range(1,len(attribs)):
            a = attribs[i][0]
            if attribs[i][1] == '': 
                v = 'None' 
            else: 
                v = attribs[i][1]
            print("-> {} > {}".format(a,v))

#metoda 4 DRY
from html.parser import HTMLParser
n = int(input())

page = []
for line in range(n):
  page.append(str(input()))

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,args):
        self.handler("Start",tag,args)
    def handle_endtag(self,tag):
        self.handler("End",tag)
    def handle_startendtag(self,tag,args):
        self.handler("Empty",tag,args)
    def handler(self,type,tag,args=[]):
        print("%-6s: %s" % (type,tag))
        if len(args) > 0:
            for a in args:
                print("-> %s > %s" % (a[0],a[1]))

parser=MyHTMLParser()
parser.feed("\n".join(page))

#metoda 5 DRY
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def _handler_factory(msg):
        msg = msg.ljust(6) + ':'
        def handler(self, tag, attrs=[]):
            print(msg, tag)
            for a in attrs:
                print("-> %s > %s" % a)
        return handler

    locals().update(zip(
        map("handle_{}tag".format, ("start", "end", "startend")),
        map(_handler_factory, ("Start", "End", "Empty"))
    ))

MyHTMLParser().feed(' '.join(input() for _ in range(int(input()))))