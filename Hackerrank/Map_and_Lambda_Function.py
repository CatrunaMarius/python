

#Să învățăm câteva concepte noi Python! Trebuie să generezi o listă a primelor N numere fibonacci, 0 fiind primul număr. Apoi, aplicați funcția de hartă și o expresie lambda pentru a cubula fiecare număr de fibonacci și a tipări lista.

#Concept

#Funcția map () aplică o funcție fiecărui membru al unui iterabil și returnează rezultatul. 
#Este nevoie de doi parametri: în primul rând, funcția care urmează să fie aplicată și în al doilea rând, funcționează.
#Să zicem că vi se oferă o listă de nume și trebuie să imprimați o listă care conține lungimea fiecărui nume.

#Lambda este o singură expresie funcție anonimă adesea folosită ca funcție în linie.
# În cuvinte simple, este o funcție care are o singură linie în corpul său. Se dovedește foarte util în programarea funcțională și GUI.
#Notă:

#Funcțiile Lambda nu pot utiliza instrucțiunea return și pot avea doar o singură expresie.
# Spre deosebire de def, care creează o funcție și îi atribuie un nume, lambda creează o funcție și returnează funcția în sine.
#  Lambda poate fi folosit în liste și dicționare.

#Formatul de intrare

#O linie de intrare: un număr întreg N.
#Format de iesire

#O listă pe o singură linie care conține cuburile primelor N numere de fibonacci.

#Sample Input

#5
#Sample Output

#[0, 1, 1, 8, 27]
#Explanation

#The first 5 fibonacci numbers are [0,1,1,2,3], and their cubes are [0,1,1,8,27] .

cube = lambda x: pow(x,3)# complete the lambda function 
def fibonacci(n):
     # return a list of fibonacci numbers
     lis = [0,1]
     for i in range(2,n):
         lis.append(lis[i-2] + lis[i-1])
     return(lis[0:n])

n = int(input())
print(list(map(cube, fibonacci(n))))



#metoda 2
inp = int(input())

cube = lambda x: x**3 # complete the lambda function

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

print(list(map(cube, list(fibonacci(inp)))))
