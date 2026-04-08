#static methods
#these methods are helps to build a utility function
#static functions dont need a instance
#we can access through the class
# we can access the class variables also
#lets see the example

class A:
    class_variable = 1234567890

    def __init__(self,n,a):
        self.name = n
        self.age = a 
    
    @staticmethod
    def add(a,b):
        print(a+b)
        print(A.class_variable)
    @staticmethod
    def sub(a,b):
        print(a-b)
        print(A.class_variable)
    

A.add(1,2)
A.sub(10,3)