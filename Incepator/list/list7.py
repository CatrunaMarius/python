#Find the longest word in a string 

string = "python java c c++ javascript pascal php"
print(string)

words=string.split()

id_longest =0

for i in range(1,len(words)):
    if len(words[id_longest])<len(words[i]):
        id_longest =i
print(words[id_longest])