
#În această provocare, sarcina este depanarea codului existent pentru a executa cu succes toate fișierele de test furnizate.

#Considerați că vocalele din alfabet sunt a, e, i, o, u și y.

#Funcția score_words ia o listă de cuvinte minuscule ca argument și returnează un scor astfel:

#Scorul unui singur cuvânt este 2 dacă cuvântul conține un număr egal de vocale. În caz contrar, scorul acestui cuvânt este 1.
# Scorul pentru întreaga listă de cuvinte este suma scorurilor tuturor cuvintelor din listă.

#Debugați funcția dată punctele de parolă astfel încât să returneze un scor corect.

#Funcția dvs. va fi testată în mai multe cazuri prin codul șablonului blocat.

#Formatul de intrare

#Intrarea este citită de șablonul de cod blocat furnizat. În prima linie, există un singur număr întreg n, care indică numărul de cuvinte. 
#În a doua linie, există n cuvinte minuscule separate de spațiu.

#Format de iesire

#Ieșirea este produsă de șablonul de cod furnizat și blocat. 
#Apelează funcții score_words cu lista de cuvinte citite de la intrare ca argument și tipărește scorul returnat la ieșire.

#Sample Input 0

#2
#hacker book
#Sample Output 0

#4


#Explicație 0

#În intrare există două cuvinte: hacker și carte.
# Scorul cuvântului hacker este 2, deoarece conține un număr egal de vocale, 
# adică 2 vocale, iar scorul cărții este 2 pentru același motiv. 
# Astfel, scorul total este 2 + 2 = 4.
#Sample Input 1

#3
#programming is awesome
#Sample Output 1

#4


#Explicație 1

#Există 3 cuvinte în intrare: programare, este 1 și minunat. 
#Scorul programării este întrucât conține 3 vocale, un număr impar de vocale.
# Scorul de este este de asemenea 1, deoarece are un număr impar de vocale. 
# Scorul minunat este de 2, deoarece conține 4 vocale, un număr egal de vocale.
#  Astfel, scorul total este 1 + 1 + 2 = 4.

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score


n = int(input())
words = input().split()
print(score_words(words))