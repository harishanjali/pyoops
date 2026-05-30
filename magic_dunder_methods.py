#magic methods
#magic methods are the built-in-methods given by the python
#to do some operations likeadd,subtract,concattination,comparision etc.

#lets see with example

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,other,extra):
        # return other
        return self.x+other.x+extra.x+extra.y+other.y+self.y
    
a = Vector(2,2)
b = Vector(3,3)
c = Vector(4,4)
print(a+b+c)
