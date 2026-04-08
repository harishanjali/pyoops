from base import Calculator

class NewCalc(Calculator):
    def isprime(self):
        if self.n<2:
            return False
        for i in range(2,self.n//2+1):
            if self.n%2==0:
                return False
        else:
            return True
        
    def isperfect(self):
        s=0
        for d in range(1,self.n//2+1):
            if self.n%d==0:
                s+=d
        return s==self.n
    
c = NewCalc(6)
res = c.isprime()
res1=c.isperfect()
print(res,res1)
