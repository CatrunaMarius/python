#hackerrank
#Ambii jucători primesc aceeași string,.
#Ambii jucători trebuie să realizeze substraturi folosind literele stringului.
#Stuart trebuie să facă cuvinte începând cu consoane.
#Kevin trebuie să facă cuvinte începând cu vocale.
#Jocul se încheie atunci când ambii jucători au făcut toate substraturile posibile.

#def minion_game(string):
#    voweles = 'AEIOU'
#    kevin = 0
#    stusc = 0

#    for i in range(len(string)):
#        if string[i] in voweles:
#            kevin += (len(string)-i)
#        else:
#            stusc += (len(string)-i)
#    if kevin>stusc:
#        print("kevin",kevin)
#    elif kevin<stusc:
#        print("start", stusc)
#    else:
#        print("draw")

#metoda 2

#def minion_game(string):
#   vowels, L = 'AEIOU', len(s)
#   K = sum([L-i for i in range(L) if s[i] in vowels])
#   S = sum([L-i for i in range(L) if s[i] not in vowels])
#   print(['Stuart '+str(S),['Kevin '+str(K),'Draw'][K==S]][K>=S])

#metoda 3
def minion_game(string):
    S = 0
    K = 0
    for place,char in enumerate(string):
        if char in 'AEIOU':
            K += len(string) - place
        else:
            S += len(string) - place

    if S>K:
        print("Stuart {0}".format(S))
    elif K>S:
        print("Kevin {0}".format(K))
    else:
        print("Draw")

s = input()
minion_game(s)

 