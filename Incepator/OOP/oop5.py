#Hiding the field from external access

class B:
    __count = 0

    def __init__(self):
        B.__count +=1

    def __del__(self):
        B.__count -=1

    @staticmethod
    def qty_objects():
        return B.__count

a=B()
b=B()
c=B()
print(b.qty_objects())
del a
print(B.qty_objects())
print(b.qty_objects())