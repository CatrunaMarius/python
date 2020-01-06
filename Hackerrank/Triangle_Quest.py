#Sample Input

#5
#Sample Output

#1
#22
#333
#4444


for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    #metoda 1 nu este permis stringu chiar daca este corecta
    print(str(i)*i)
    #metoda 2
    print((10**(i)//9)*i)
    #metoda 3
    print(sum(map(lambda x : i *10**x, range(i))))