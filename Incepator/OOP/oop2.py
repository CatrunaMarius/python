#Exemple with inheritance
class Block:
    def __init__(self, width, length, height):
        self.w = width
        self.l =length
        self.h = height
    def volume(self):
        return self.w*self.l*self.h

class ColorBlock(Block):
    def __init__(self, width, length, height, color):

        Block.__init__(self, width, length, height)
        self.c =color

class BorderBlock(Block):
    border = 1

    def volume(self):
        w = self.w + BorderBlock.border
        l = self.l + BorderBlock.border
        h = self.h + BorderBlock.border
        return w*l*h

block1 = ColorBlock(3, 2, 0.5 , "red")
block2 = BorderBlock(1, 1, 1)

print(block1.volume())
print(block2.volume())
        
