#hackerrank
#Sample Input

#abracadabra
#5 k
#Sample Output

#abrackdabra

def mutate_string(string, position, character):
    l = list(string)
    #l[position] = "%s" %character 
    l[position] = character 
    return ''.join(l)
    
#metoda 2
def mutate_string(string, position, character):
 
    return string[:position] + character + string[position + 1:]

#metoda 3
def mutate_string(string, position, character):
 
    return character.join([string[:position], string[position + 1:]])

#metoda 4
def mutate_string(string, position, character):
 
   return ("{}{}{}".format(string[:position], character, string[position+1:]))



s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)

