
#Definiți o clasă numită Circle care poate fi construită printr-o rază. Clasa Circle are o metodă care poate calcula zona.

#sugestii
#Utilizați def methodName (self) pentru a defini o metodă.

class Circle(object):
    def __init__(self, r):
        self.radius =r
    def area(self):
        return self.radius**2*3.14
aCircle = Circle(2)
print(aCircle.area())

#metoda 2
class Circle():
    def __init__(self,r):
        self.radius=r
    def area(self):
        return 3.1416*(self.radius**2)

circle =Circle(5)
print(circle.area())

#Problema 2
#Definiți o clasă numită Rectangle care poate fi construită după lungime și lățime Clasa Rectangle are o metodă care poate calcula zona.

#sugestii
#Utilizați def methodName (self) pentru a defini o metodă.

class Rectangel(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

eRactangle =Rectangel(2,10)
print(eRactangle.area())



#Definiți o clasă numită Shape și subclasa Square. Clasa Square are o funcție init care ia o lungime ca argument.
# Ambele clase au o funcție de zonă care poate imprima în mod implicit aria formei unde zona Shape este 0.

#sugestii
#Pentru a înlocui o metodă din super-clasă, putem defini o metodă cu același nume în super-clasă.

class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,l):
        Shape.__init__(self)
        self.length =l

    def area(self):
        return self.length*self.length

e=Square(3)
print(e.area())

#problema 3
#Vă rugăm să ridicați o excepție RuntimeError.

#sugestii
#UUse raise () pentru a ridica o excepție.

raise(RuntimeError("sonthing wrong"))
