#Readind a text file to the list

data = []
for i in open("text.txt"):
    data.append(i)

print(data)
'''
for i in range(len(data)):
    if data[i][-1] == '\n':
        data[i] = data[i][:-1]'''

#or
for i in range(len(data)):
    data[i] = data[i].strip()

print(data)