

#Hai să ne cufundăm în decoratori! Vi se dau N numere mobile. Sortează-le în ordine crescătoare, 
#apoi imprimă-le în formatul standard prezentat mai jos:


#+91 xxxxx xxxxx

#Numerele date mobile pot avea +91,91 sau 0 înainte de numărul real de 10 cifre. 
#În mod alternativ, este posibil să nu existe deloc un prefix.

#Formatul de intrare

#Prima linie de intrare conține un număr întreg N, numărul de numere de telefon mobil.
#Urmează N linii care conțin fiecare un număr de telefon.

#Format de iesire

#Tipăriți N numere mobile pe linii separate în formatul dorit.

#Sample Input

#3
#07895462130
#919875641230
#9195969878
#Sample Output

#+91 78954 62130
#+91 91959 69878
#+91 98756 41230

#Concept

#La fel ca majoritatea altor limbaje de programare, Python are conceptul de închideri. 
#Extinderea acestor închideri ne oferă decoratori, care sunt un atu neprețuit.
# Puteți afla despre decoratori în 12 pași simpli aici.
#Pentru a rezolva întrebarea de mai sus, faceți o listă a numerelor de telefon și 
#treceți-o la o funcție care sortează tabloul în ordine crescătoare. 
#Realizați un decorator care standardizează numerele de telefon și aplicați-l funcției.
import re
def wrapper(f):
    def fun(l):
        # complete the function
         f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
         
         #metoda 2
         f('+91 {} {}'.format(n[-10:-5], n[-5:]) for n in l)
         
         #metoda 3
         f(map(lambda x: "+91 " + x[-10:-5] + " " + x[-5:], l))
          
         #metoda 4
         # regex to match tel. number and parse it into groups 
         pat = re.compile(r'(0|91|\+91)?(\d{5})(\d{5})')
        # give it standard prefix and copy the groups
         l = [re.sub(pat, r"+91 \2 \3", x) for x in l]
         f(l)       
         
         #metoda 5
         fl = []
         for no in l:
            if len(no) == 10:
                fl.append('+91 '+str(no[0:5]+' '+str(no[5:10])))
            elif len(no) == 11:
                fl.append('+91 '+str(no[1:6]+' '+str(no[6:11])))
            elif len(no) == 12:
                fl.append('+91 '+str(no[2:7]+' '+str(no[7:12])))
            elif len(no) == 13:
                no = no[0:3]+' '+str(no[3:8])+' '+str(no[8:13])
                fl.append(no)
         return f(fl)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 