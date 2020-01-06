

# Învățați să pronunțați
#Vi se oferă un document XML valid și trebuie să imprimați scorul acestuia. Scorul este calculat prin suma punctajului fiecărui element.
# Pentru orice element, scorul este egal cu numărul de atribute pe care le are.

#Formatul de intrare

#Prima linie conține N, numărul de linii din documentul XML.
#Următoarele N linii urmează conținând documentul XML.

#Format de iesire

#Afișează o singură linie, scorul întreg al documentului XML dat.

#Sample Input

#6
#<feed xml:lang='en'>
#    <title>HackerRank</title>
#    <subtitle lang='en'>Programming challenges</subtitle>
#    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#    <updated>2013-12-25T12:00:00</updated>
#</feed>
#Sample Output

#5

#Explicaţie

#Eticheta de alimentare și subtitrare au fiecare atribut - lang.
#Titlul și etichetele actualizate nu au atribute.
#Eticheta de legătură are trei atribute - rel, type și href.

#Deci, scorul total este 1 + 1 + 3 = 5.

#Este posibil să existe orice nivel de cuibărit în documentul XML. Pentru a afla despre analizarea XML, consultați aici.

#NOTĂ: Pentru a analiza și genera un arbore de elemente XML, utilizați următorul cod:

#>> import xml.etree.ElementTree ca etree
#>> tree = etree.ElementTree (etree.fromstring (xml))
#Aici, XML este variabila care conține șirul.
#De asemenea, pentru a găsi numărul de taste într-un dicționar, utilizați funcția len:

#>> dicti = {'0': 'Acesta este zero', '1': 'Acesta este unul'}
#>> print (len (dicti))

#2

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    return sum(len(child.attrib) for child in node.iter())

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


    #metoda 2
xml = ''.join(raw_input() for _ in xrange(input()))
import xml.etree.ElementTree as etree
tree = etree.ElementTree(etree.fromstring(xml))

def traverse(node):
  return len(node.attrib) + sum(traverse(child) for child in node)

print (traverse(tree.getroot()))