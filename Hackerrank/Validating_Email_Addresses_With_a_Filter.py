
#You are given an integer N followed by N  email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.


#Valid email addresses must follow these rules:

#It must have the username@websitename.extension format type.
#The username can only contain letters, digits, dashes and underscores.
#The website name can only have letters and digits.
#The maximum length of the extension is 3.

#Concept

#A filter takes a function returning True or False and applies it to a sequence, returning a list of only those members of the sequence where the function returned True. A Lambda function can be used with filters.

#Let's say you have to make a list of the squares of integers from 0 to 9 (both included).

#>> l = list(range(10))
#>> l = list(map(lambda x:x*x, l))


#Acum, aveți nevoie de acele elemente care sunt mai mari de 10, dar mai mici de 80.

#>> l = list(filter(lambda x: x > 10 and x < 80, l))

#Formatul de intrare

#Prima linie de intrare este numărul întreg N, numărul de adrese de e-mail.
# Urmează N linii, fiecare conținând un șir.

 
#Format de iesire

#Sortează o listă care conține adresele de e-mail valide în ordine lexicografică. Dacă lista este goală, scoateți o listă goală, [].

#Sample Input

#3
#lara@hackerrank.com
#brian-23@hackerrank.com
#britts_54@hackerrank.com
#Sample Output

#['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']


def check_valid(email):
    try:
        username, url = email.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False
    
    if username.replace("-", "").replace("_", "").isalnum() is False:
        return False
    elif website.isalnum() is False:
        return False
    elif len(extension) > 3:
        return False
    else:
        return True

n = int(input())
emails = [input() for email in range(n)]

valid = list(filter(check_valid, emails))
print(sorted(valid))

#metoda 2
import re
def fun(s):
    return bool(re.search('[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s))
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

#metod 3
import re

def fun(s):
    try:
        user,website,domain=re.split('\@|\.',s)
    except:
        return False
    processed=user.replace('-','').replace('_','')
    return all( [processed.isalnum(), website.isalnum(), len(domain)<=3] )
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)