class Calculator:
    def __init__(self,a,b=20):
        self.a = a
        self.b = b
    
    def addition(self):
        return self.a+self.b
    
    def multi(self):
        return self.a*self.b
    
    def divide(self):
        return self.a/self.b
    
obj1 = Calculator(10,20)
obj2 = Calculator(20,30)
obj3 = Calculator(10,5)
res = obj1.addition()
res = obj2.multi()
res = obj3.divide()
print(res)
