#hackerrank
#Trebuie să imprimați numărul de ocazii cu care se produce subcadrarea în stringul dat.
# Traversarea șirurilor va avea loc de la stânga la dreapta,
#  nu de la dreapta la stânga.
#Sample Input

#ABCDCDC
#CDC
#Sample Output

#2

'''def count_substring(string, sub_string):
 count =0

 for i in range(0,len(string)-len(sub_string)+1):

    try:

        if string[i:i+len(sub_string)]==sub_string:

            count+=1

    except IndexError:

        break

 return count
'''

def count_substring(string, sub_string):
    return(sum([1 for i in range(0, len(string) - len(sub_string) + 1) if (string[i:(len(sub_string)+i)] == sub_string)]))
   #metoda 2
   #count=0
    ##print(len(string),len(sub_string))
    #for i in range(0, len(string)-len(sub_string)+1):
    #    if string[i] == sub_string[0]:
    #        flag=1
    #        for j in range (0, len(sub_string)):
    #            if string[i+j] != sub_string[j]:
    #                flag=0
    #                break
    #        if flag==1:
    #            count += 1
    #return count
    #metoda 3
    counter=0
    i=0
    while i<len(string):
       if string.find(sub_string,i)>=0:
          i=string.find(sub_string,i)+1
          counter+=1
       else: break
    return counter
    #metoda 4
    count = 0
    while True:
      try:
        string = string[string.index(sub_string)+1:]
        count += 1
      except:
        break

    return count

string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)