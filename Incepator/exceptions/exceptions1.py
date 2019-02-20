#A non-existent variable
a=10
b=105
c=3.5
var = input("the variable: ")

try:
    exec("print("+var+")")
except NameError:
    print("No such variable")
