#hackerrank
#Sample Input
#  this is a string   
#Sample Output
#   this-is-a-string

def split_and_join(line):
    
   # return line.replace(" ","-")
    line = line.split(" ")
    line = "-".join(line)
    return line

line = input()
a = split_and_join(line)
print(a)