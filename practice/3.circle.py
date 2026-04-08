#area and circumference of circle

class Circle:
    def area(self,r):
        return 3.14*r*r
    def circumference(self,r):
        return 2*3.14*r
    
c = Circle()
area = c.area(10)
circumference = c.circumference(10)
print(area,circumference)