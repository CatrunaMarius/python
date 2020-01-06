#input 5
import string
def print_rangoli(size):
    alpha = string.ascii_lowercase
    
    #metoda 1
    width = 4 * size - 3
      
    for i in list(range(size))[::-1] + list(range(1, size)):
          print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(width, '-'))

    
    
    
    
    L=[]

    #metoda 2
    for i in range(n):
      s = "-".join(alpha[i:n])
      L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))
    
     
    ##metoda 3
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append(s[::-1]+s[1:])

    width = len(L[0])

    for i in range(n-1, 0, -1):
        print(L[i].center(width, "-"))

    for i in range(n):
        print(L[i].center(width, "-")) 



n = int(input())
print_rangoli(n)