#whenever we create the user defined objects some inbuilt methods are inherited to that particular object.
#thsoe are __add__,__str__ etc

#lets see how we can overload or overcome this problem when we add the unsupporrted types.

class Quantity:
    def __init__(self,qty,y):
        self.qty = qty
        self.y = y
    def info(self):
        print('quantity',self.qty)

    def __add__(self,other):#involes when we perform +
        # obj = Quantity(self.qty,other.qty)
        return (self.qty+other.qty,self.y+other.y)
    def __gt__(self,other):#invokes when we perofrm >
        return self.qty>other.qty
    def __str__(self):#invokes when print calls
        return str(self.qty)
    
    def __repr__(self):
        return str(self.qty)

obj1 = Quantity(10,20)
obj2 = Quantity(20,30)

#res = obj1+obj2 this is wrong
#so dont violate the fundamental behaviour of operator 
res = obj1+obj2
print(res)
# res = obj1>obj2
# print(obj1,obj2)
# print([obj1,obj2])