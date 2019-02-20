#A simple example of polymorphism


class T1:
    n =10
    def total(self, n):
        print(int(self.n)+int(n))

class T2:
    def total(self, s):
        print(len(str(s)))
t1=T1()
t2=T2()
t1.total(45)
t2.total(45)