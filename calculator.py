class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.result = 0
    def add(self):
        self.result = self.a + self.b
        return self.result
    def sub(self):
        self.result = self.a - self.b
        return self.result
    def divide(self):
        self.result = self.a//self.b
        return self.result
    def multi(self):
        self.result = self.a*self.b
        return self.result
    def continued(self,v,opn):
        self.a = self.result
        self.b = v
        if opn=='add':
            self.add()
        elif opn=='sub':
            self.sub()
        elif(opn=='multi'):
            self.multi()
        elif(opn=='divide'):
            self.divide()
        return self.result

    
o1 = Calculator(10,20)
o1.add()
o1.continued(45,'add')
o1.continued(45,'sub')
o1.continued(2,'multi')
o1.continued(2,'divide')
print(o1.result)