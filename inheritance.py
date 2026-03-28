#if you want the one function in parent, you can inerit it and use.

#let see the problem first

# class A:
#     def display(self):
#         print('some logic')

# class B:
#     def display(self):
#         print('some logic')

#so in the above logic we are facing a problem that code is repeating, so we can use the function in another class
#after inherititng the paretn, we will get all data and methods except protected vars

#if you wants to over ride a fucntions from parent yiu can do in child
#five types of inheritance
#1.single inheritance
#2.multiple inheritnace
#3.multilevel inheritance
#4.heirarcial inheritance
#5.hybrid inheritance

#single inheritance
class A:#parent/Super/base class
    def __init__(self):
        print('consructor from  A')
    def display(self):
        print('some logic from A')

class B(A):#child/sub/derive class
    # def __init__(self):
    #     print('consructor from  B')
    def show(self):
        print('from B class')

    def display(self):#this is called method overriding
        print('method overrding')
# b = B()
# b.display()
# b.show()

#multiple inheritance
class A:
    def display(self):
        print('display from A')

class B:
    def show(self):
        print('show from B')
    def display(self):
        print('display from B')

class C(B,A):
    def info(self):
        print('info from C')

#diamond problem
#same method is coming from diffent base classes, this ambiguity is diamond problem
#so in this situation we  have two display functions in class a and class b,
# so in this case display function will call based on the order we are inheriting
#inheritance order (A,B) or (B,A)
#whatver will be first, that method will call in that object
#this order decides by MRo-method resolution order
# obj = C()
# obj.display()
# obj.show()
# obj.info()

# print('MRO',C.mro())#it will give order of priority to the classes
# print('directory',dir(C))

#multilevel inheritance
class Customer:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def info(self):
        print(self.name,self.age,)
class Employee(Customer):
    def __init__(self,n,a,empn,empsl):
        super().__init__(n,a)
        self.empno = empn
        self.empsl = empsl
    def info(self):
        super().info()
        print(self.empno,self.empsl)

class Manager(Employee):
    def __init__(self, n, a, empn, empsl,rights):
        super().__init__(n, a, empn, empsl)
        self.special = rights
    def info(self):
        super().info()
        print(self.special)

# obj = Customer('harish',25)
# obj.info()
# obj = Employee('harish',25,7155,40000)
# obj.info()
# obj = Manager('harish',25,7155,40000,'manage')
# obj.info()

#heirarchial inheritance
'''     A
       /  \
      /    \
      B     C
'''

class A:
    def display(self):
        print('display from A')

class B(A):
    def show(self):
        print('show from B')

class C(A):
    def info(self):
        print('info from C')

# obj = C()
# obj.info()
# obj.display()

# obj = B()
# obj.show()
# obj.display()


#hybrid inheritance

'''
        A
       /  \
      /    \
      B     C     
             \
              \
               D
'''

class A:
    def display(self):
        print('display from A')

class B(A):
    def show(self):
        print('show from B')

class C(A):
    def info(self):
        print('info from C')

class D(C):
    def impress(self):
        print('impress from D')

obj = D()
#isinstnace-whether the object is related to that class or not
res = isinstance(obj,B)
res = isinstance(obj,D)
res = isinstance(obj,C)
print(res)
obj.display()
obj.info()
obj.impress()