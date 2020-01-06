
#Sample Input

#2 1
#5 6
#Sample Output

#7.00+7.00i
#-3.00-5.00i
#4.00+17.00i
#0.26-0.11i
#2.24+0.00i
#7.81+0.00i



import math
#metoda 1
#class Complex(complex):
#    def __add__(self, no):
#        return Complex(complex.__add__(self, no))

#    def __sub__(self, no):
#        return Complex(complex.__sub__(self, no))

#    def __mul__(self, no):
#        return Complex(complex.__mul__(self, no))

#    def __truediv__(self, no):
#        return Complex(complex.__truediv__(self, no))

#    def mod(self):
#        return Complex(complex.__abs__(self))

#    def __str__(self):
#        return '{0.real:.2f}{0.imag:+.2f}i'.format(self)

#if __name__ == '__main__':
#    c = map(float, input().split())
#    d = map(float, input().split())
#    x = Complex(*c)
#    y = Complex(*d)
#    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')




#metoda 2
#class Complex(object):
#    def __init__(self, real, imaginary):
#        self.real = real
#        self.imaginary = imaginary

#    def __add__(self, no):
#        a = complex(self.real, self.imaginary)
#        b = complex(no.real, no.imaginary)
#        return Complex((a+b).real , (a+b).imag).__str__()
        
#    def __sub__(self, no):
#        a = complex(self.real, self.imaginary)
#        b = complex(no.real, no.imaginary)
#        return Complex((a-b).real , (a-b).imag).__str__()
        
#    def __mul__(self, no):
#        a = complex(self.real, self.imaginary)
#        b = complex(no.real, no.imaginary)
#        return Complex((a*b).real , (a*b).imag).__str__()

#    def __truediv__(self, no):
#        a = complex(self.real, self.imaginary)
#        b = complex(no.real, no.imaginary)
#        return Complex((a/b).real , (a/b).imag).__str__()

#    def mod(self):
#        return Complex(abs(complex(self.real, self.imaginary)), 0)

#    def __str__(self):
#        if self.imaginary == 0:
#            result = "%.2f+0.00i" % (self.real)
#        elif self.real == 0:
#            if self.imaginary >= 0:
#                result = "0.00+%.2fi" % (self.imaginary)
#            else:
#                result = "0.00-%.2fi" % (abs(self.imaginary))
#        elif self.imaginary > 0:
#            result = "%.2f+%.2fi" % (self.real, self.imaginary)
#        else:
#            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#        return result

#c = map(float, input().split())
#d = map(float, input().split())
#x = Complex(*c)
#y = Complex(*d)
#print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

class Complex(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, n):
        comp = n + complex(self.real, self.imag)
        return Complex(comp.real, comp.imag)

    def __sub__(self, n):
        comp = n - complex(self.real, self.imag)
        return Complex(comp.real, comp.imag)

    def __mul__(self, n):
        comp = n * complex(self.real, self.imag)
        return Complex(comp.real, comp.imag)

    def __truediv__(self, n):
        comp = n / complex(self.real, self.imag)
        return Complex(comp.real, comp.imag)

    def mod(self):
        comp = complex(math.sqrt(self.real**2 + self.imag**2))
        return Complex(comp.real, comp.imag)

    def __str__(self):
        if self.imag == 0:
            result = "{:.2f}+0.00i".format(self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+{:.2f}i".format(self.imag)
            else:
                result = "0.00-{:.2f}i".format(abs(self.imag))
        elif self.imag > 0:
            result = "{:.2f}+{:.2f}i".format(self.real, self.imag)
        else:
            result = "{:.2f}-{:.2f}i".format(self.real, abs(self.imag))
        return result
c = map(float, input().split())
d = map(float, input().split())
x = Complex(*c)
y = Complex(*d)
print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
