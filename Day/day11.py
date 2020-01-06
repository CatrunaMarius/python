
#Scrieți o funcție pentru a calcula 5/0 și utilizați try / except pentru a surprinde excepțiile.
# Sugestii Utilizați try / except pentru a surprinde excepții.

def cal():
    return 5/0

try:
    cal()
except ZeroDivisionError:
    print("divisition by zero")
except Exception:
    print("Caught an exception")
finally:
    print("In finally block for cleanup")

#metoda 2
def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("Why on earth you are divding a number by ZERO")
except:
    print("Any other exception")

#Problema 2
#Definiți o clasă de excepție personalizată care ia un mesaje string ca atribut.

#sugestii
#Pentru a defini o excepție personalizată, trebuie să definim o clasă moștenită de la Excepție.

class MyError(Exception):
    """My own exception class

    Attributes:
    msg -- explanation of the error"""

    def __init__(self, msg):
        self.msg =msg

error = MyError("somthing wrong")

#metoda 2
class CustomException(Exception):
    """Exception raised for custom purpose

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message):
        self.message = message

num = int(input())

try:
    if num<10:
        raise CustomException("Input is less than 10")
    elif num>10:
        raise CustomException("Input is grate than 10")
except CustomException as ce:
    print("The eroor raised :" +ce.message)

#Problema 3
#Presupunând că avem câteva adrese de e-mail în formatul „username@companyname.com”, vă rugăm să scrieți un program pentru a imprima numele de utilizator al unei adrese de e-mail date. Atât numele de utilizator, cât și numele companiei sunt compuse numai din litere.

#Exemplu: Dacă este introdusă următoarea adresă de e-mail ca intrare în program:

#john@google.com
#Apoi, rezultatul programului ar trebui să fie:

#john
#În cazul în care datele de intrare sunt furnizate la întrebare, ar trebui să presupunem că este o intrare de consolă.

#sugestii
#Folosiți \ w pentru a potrivi litere.

import re
emailAddress = input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print(r2.group(1))

#metoda 2
email = "john@google.com"
email=email.split("@")
print(email[0])
#metoda 3
email = input().split('@')
print(email[0])
#metoda 4
email = "john@google.com elise@python.com"
pattern= "(\w+)@\w+.com"
ans = re.findall(pattern,email)
print(ans)

