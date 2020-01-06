

#Vi se oferă patru puncte A, B, C și D într-un sistem de coordonate carteziene tridimensionale. Vi se cere să imprimați unghiul dintre planul realizat de punctele A, B, C și B, C, D în grade (nu radiene). Fie unghiul să fie PHI.
#cos (PHI) = (X.Y) / | X || Y |
# unde X = AB x BC și Y = BC x CD.

#Aici, X.Y înseamnă produsul punct al X și Y, iar AB x BC înseamnă produsul încrucișat al vectorilor AB și BC. De asemenea, AB = B-A.

#Formatul de intrare

#O linie de intrare care conține valorile numărului flotant separat de spațiu al coordonatelor X, Y și Z ale unui punct.

#Format de iesire

#Ieșirea unghiului corect până la două zecimale.

#Sample Input

#0 4 5
#1 7 6
#0 5 9
#1 7 2
#Sample Output

#8.19


import math


class Points(object):
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __sub__(self, no):
        return  Points((self.x-no.x),(self.y-no.y),(self.z-no.z))

    def dot(self, no):
        return (self.x*no.x)+(self.y*no.y)+(self.z*no.z)

    def cross(self, no):
        return Points((self.y*no.z-self.z*no.y),(self.z*no.x-self.x*no.z),(self.x*no.y-self.y*no.x))
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))


#metoda 2
#class vector:
#    def __init__(self, x=0, y=0, z=0):
#        self.x = x
#        self.y = y
#        self.z = z
               
#    def __mul__(self, k):
#        return vector(self.x * k, self.y * k, self.z * k)
    
#    def __add__(self, other):
#        s, o = self, other
#        return vector(s.x + o.x, s.y + o.y, s.z + o.z)
   
#    def __sub__(self, other):
#        return self + other * -1
        
#    # dot product
#    def __mod__(self, other):
#        s, o = self, other
#        return (s.x * o.x) + (s.y * o.y) + (s.z * o.z)
    
#    # modulus
#    def __abs__(self):
#        return math.sqrt(self % self)
    
#    # cross product
#    def __xor__(self, other):
#        s, o = self, other
#        x = (s.y * o.z) - (s.z * o.y)
#        y = (s.z * o.x) - (s.x * o.z)
#        z = (s.x * o.y) - (s.y * o.x)
#        return vector(x, y, z)
    
#def read_vector():
#    return vector(*map(float, input().split()))
    
#A = read_vector()
#B = read_vector()
#C = read_vector()
#D = read_vector()

#X = (B - A) ^ (C - B)
#Y = (C - B) ^ (D - C)

#phi = math.degrees(math.acos(X % Y / math.sqrt((X % X) * (Y % Y))))
#print('%.2f' % phi)   

