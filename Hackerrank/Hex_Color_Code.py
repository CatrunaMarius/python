
#Culorile CSS sunt definite folosind o notare hexadecimală (HEX) pentru combinarea valorilor culorilor Roșu, Verde și Albastru (RGB).

#Specificațiile Codului de culoare HEX

#■ Trebuie să înceapă cu un simbol „#”.
#■ Poate avea 3 sau 6 cifre.
#■ Fiecare cifră este cuprinsă între 0 și F. (1,2,3,4,5,6,7,8,9,0, A, B, C, D, E și F).
#■ Literele A-F pot fi cu litere mici. (a, b, c, d, e și f sunt, de asemenea, cifre valabile).

#Examples

#Valid Hex Color Codes
##FFF 
##025 
##F0A1FB 

#Invalid Hex Color Codes
##fffabg
##abcf
##12365erff

#Vi se oferă N linii de cod CSS. Sarcina dvs. este de a imprima toate codurile de culori Hex valabile, în ordinea apariției lor de sus în jos.

#Model CSS Cod

#Selector
#{
#	Property: Value;
#}

#Formatul de intrare

#Prima linie conține, numărul de linii de cod.
#Următoarele linii conțin coduri CSS.

#Format de iesire

#Introduceți codurile de culoare cu simboluri '#' pe linii separate.

#Sample Input

#11
##BED
#{
#    color: #FfFdF8; background-color:#aef;
#    font-size: 123px;
#    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
#}
##Cab
#{
#    background-color: #ABC;
#    border: 2px dashed #fff;
#}   
#Sample Output

##FfFdF8
##aef
##f9f9f9
##fff
##ABC
##fff

#Explicaţie

##BED și #Cab îndeplinesc criteriile Codului de culoare Hex, dar sunt utilizate ca selectori și nu ca coduri de culoare în CSS-ul dat.

#Prin urmare, codurile de culori valide sunt:

## FfFdF8
##aef
## f9f9f9
##fff
##ABC
##fff

#Notă: Nu există comentarii (// sau / * * /) în Codul CSS.


N=int(input())

for i in range(0,N):
    s=input()

    x=s.split()

    if len(x)>1  and  '{' not in x:
        x=re.findall(r'#[a-fA-F0-9]{3,6}',s)
        [print(i) for  i in x]
#metoda 2
import re, sys
[print(j) for i in sys.stdin for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', i, re.I)]
#metoda 3
N = int(input())
for _ in range(N):
    line = input().strip()
    codes = [j for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})[\s:;,)]', line, re.I)]
    for code in codes:
        print (code)
#metoda 4
for i in range(int(input())):
    matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if matches:
        print(*matches, sep='\n')

#metoda 5
import re, sys
print(*re.findall("(?<!\n)#(?i:[\\da-f]{3}){1,2}", sys.stdin.read()), sep='\n')

#metoda 6
for i in range(0, int(input())):
    matches = re.findall(r"(#(?:[\da-f]{3}){1,2})(?!\w)(?=.*;)", input(), re.IGNORECASE)
    for m in matches:
        print(m)