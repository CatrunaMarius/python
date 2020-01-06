#Modulul itertools standardizează un set principal de instrumente rapide, cu memorie eficientă,
# care sunt utile de unul singur sau în combinație. Împreună, formează o algebră iteratoare, 
# făcând posibilă construcția de instrumente specializate succint și eficient în Python pur.

#Pentru a citi mai multe despre funcțiile din acest modul, consultați documentația lor aici.

#Vi se oferă o listă de N cu litere mici în limba engleză. Pentru un număr întreg K, 
#puteți selecta orice indici K (presupuneți o indexare bazată pe 1) cu o probabilitate uniformă din listă.

#Găsiți probabilitatea ca cel puțin unul dintre indicii K selectați să conțină litera: „a”.

#from functools import reduce
#N = int(input())
#L = input().split()
#K = int(input())
#M = ''.join(L).count('a')

#print (1.0 - reduce(lambda x,y: x*y,[(1.0-M*1.0/(N-i)) for i in range(K)]))


from itertools import combinations

#metoda 2
#_,s,n = input(),input().split(),int(input())
#t = list(combinations(s,n))
#f = [i for i in t if 'a' in i]
#print(len(f)/len(t))

#metoda 3
N = int(input())
lista = input().replace(' ','')
K = int(input())
clist = list(combinations(lista,K))
print('%.3f'%(sum([int('a' in i) for i in clist])/len(clist)))

#metoda 4
#n, number, k = int(input()), input().split().count('a'), int(input())
#not_a = 1
#for i in range(k):
#    not_a = not_a * (n - number - i) / (n - i)
#print(1-not_a)



