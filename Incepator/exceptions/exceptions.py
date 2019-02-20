#if a string is entered not a number as expected

n= input("Entre a number: ")

while type(n) != float:
    try:
        n = float(n)
    except ValueError:
        print("Input error!")
        n = input("Entre a number: ")
print(n/2)