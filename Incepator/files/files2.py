#The readline() method
f = open("text1.txt")
text =[]

i = f.readline()

while i != '':
    text.append(i)
    i = f.readline()

f.close()
print(text)
