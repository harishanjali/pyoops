#monkey patching
#changing the behaviour of the class by other class is monkey patching

class A:
    def display(self):
        print('display from A')

def show():
    print('i am print from show function')

a = A()
a.display = show#monkey patching
a.display()