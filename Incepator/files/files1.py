#The reaad() method
f=open("text.txt")
text = f.read()
f.close()

print(repr(text))
text = text.split('\n')
print(text)
                 
