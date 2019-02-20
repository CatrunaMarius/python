#Class with one property and one method
class A:
    class_field = 10

    def method(self, value):
        self.obj_field = A.class_field + value

a1 =A()
a2 =A()

a1.method(3)
a2.method(100)
print(a1.obj_field)
print(a2.obj_field)

print(A.class_field)