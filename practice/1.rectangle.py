#area of rectangle using class and object

class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length*self.breadth
    
reactangle = Rectangle(10,20)
res = reactangle.area()
print(res)