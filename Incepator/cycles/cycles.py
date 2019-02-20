from random import randint

#implementarea varabilei random, nr secret 
secret_num =randint(1,100)

#implementarea variabilelor
user_num =-1
try_count=1

#lupa, 
while secret_num != user_num:
    print("%d try: "%try_count,end='') #ce trebuie sa introduca userul si nr de incercarei
    user_num =int(input())#implementare inputului de la tastatura
    if user_num <secret_num:
        print("Too less")
    elif user_num >secret_num:
        print("Too much")
    else:
        print("You guessed it!")
    try_count +=1
