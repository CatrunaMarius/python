#Sample Input

#chris alan
#Sample Output

#Chris Alan

#def solve(s):

#     for x in s.split():
#        s = s.replace(x, x.capitalize(), 1) # <--- Using max argument
#        print(s)

#s = input()
#b =solve(s)

#metoda 2
#a_string = input().split(' ')
#print(' '.join((word.capitalize() for word in a_string)))

#metoda 3
def solve(s):
    l=s.split(" ")
    a = [i.capitalize() for i in l]       
    return " ".join(a)

if __name__ == '__main__':
  

    s = input()

    result = solve(s)
    print(result)

    