from abc import ABC,abstractmethod

#if you wants to implement abstraction
#you have to use abc and abstract method,
#without this there is no meaning of abstraction
#whatever you implement in base class, you have to implement in child class.

class Calculator(ABC):
    def __init__(self,n):
        self.n = n
    @abstractmethod
    def isperfect(self):
        pass
    @abstractmethod
    def isprime(self):
        pass

    def info(self):
        print('info from base class')