#The readines() method aceasta citeste doar ce este pe prima linie
f = open("text1.txt")
text = f.readline()
f.close

print(text)
