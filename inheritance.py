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
b = B()
b.display()
b.show()
