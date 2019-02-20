#Change the order of digits of an intiger to the reverse

n1=int(input("An intiger: "))
n2=0

while n1>0:
    digit = n1 % 10
    n1=n1 //10
    n2=n2*10
    n2=n2+digit

print("Inverse number: ", n2)
