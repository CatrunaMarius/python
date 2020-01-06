
#Vi se dau cuvinte. Unele cuvinte se pot repeta. Pentru fiecare cuvânt, emiteți numărul său de apariții. Ordinea de ieșire ar trebui să corespundă cu ordinea de apariție a cuvântului. Consultați intrarea / ieșirea eșantionului pentru clarificări.

#Dacă următoarea șir este dată ca intrare pentru program:

#4
#bcdef
#ABCDEFG
#BCDE
#bcdef
#Apoi, rezultatul programului ar trebui să fie:

#3
#2 1 1
#sugestii
#Alcătuiește o listă pentru a obține ordinea de introducere și un dicționar pentru a număra frecvența cuvântului

n = int(input())
word_list = []
word_dict ={}

for i in range(n):
    word = input()
    if word not in word_dict:
        word_list.append(word)
    word_dict[word] = word_dict.get(word, 0) +1
print(len(word_list))
for word in word_list:
    print(word_dict[word], end=' ')

#Program 2
#Vi se oferă un string. Sarcina dvs. este să numărați frecvența literelor string și să imprimați literele în ordinea descrescătoare a frecvenței.

#Dacă următoarea string este dată ca intrare pentru program:

#aabbbccde
#Apoi, rezultatul programului ar trebui să fie:

#b 3
#a 2
#c 2
#sugestii
#Numărați frecvența cu dicționarul și sortați după valoarea din articolele din dicționar

word = input()
dct = {}
for i in word:
    dct[i] = dct.get(i,0)+1

dct = sorted(dct.items(),key=lambda x:(-x[1],x[0]))
for i in dct[:3]:
    print(i[0],i[1])

#program 3

#Scrieți un program Python care acceptă un șir și calculați numărul de cifre și litere.

#Intrare

#Hello321Bye360
#producție

#Digit - 6
#Scrisoarea - 8
#sugestii
#Utilizați funcția isdigit () și isalpha ()

word = input()
digit, letter = 0,0
for char in word:
    digit+=char.isdigit()
    letter+=char.isalpha()

print("Digit -",digit)
print("Letter -", letter)

#program 4
#S-a dat un număr N. Căutați suma de la 1 la N folosind recursul

#Intrare

#5
#producție

#15
#sugestii
#Faceți o funcție recursivă pentru a obține suma

def rec(n):
    if n ==0:
        return n
    return rec(n-1) +n

n = int(input())
sum = rec(n)
print(sum)
