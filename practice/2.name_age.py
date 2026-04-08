#persons age and name

class Person:
    def __init__(self,n,a):
        self.name = n
        self.age = a

    def info(self):
        return 'Your name is  '+ self.name + ' and your age is ' + str(self.age)
    
p = Person('harish',25)
res = p.info()
print(res)