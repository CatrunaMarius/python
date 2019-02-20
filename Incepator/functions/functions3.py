#Fibonacci functions

def fib_n(item):
    f1 = f2 = 1

    while item > 2:
        buff =f2
        f2 =f1 +f2
        f1 = buff
        item -= 1
    return f2

def fib_row(item):
    f1 = f2 =2
    print(f1, f2, end=' ')
    while item >2:
        buff =f2
        f2 = f1+f2
        f1 = buff
        print(f2, end=' ')
        item -= 1
    print()

n = int(input())
m = fib_n(n)
print(m)

fib_row(n)