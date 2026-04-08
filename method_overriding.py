#method overriding
#chanign the behaviour of exisitng method in parent class is known as method overriding.

class A:
    def sound(self):
        print('my sound is meow')

class B(A):
    def sound(self):#method overriding
        print('my sound is bow bow')

b =B()
b.sound()