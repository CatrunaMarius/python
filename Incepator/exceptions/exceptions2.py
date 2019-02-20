#Attempt to open non-Existent file

fname = input("File: ")

try: 
    f = open(fname)
except FileNotFoundError:
    print("Error. No this file!")
else:
    print(f.read())
