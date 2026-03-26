#encapsulation
#wrapping the data and methods called as
# and data should not mmodify outside or read
#want to access needs a structure way
#in getter and setter methods



class Student:
    def __init__(self,n,m):
        self.name = n
        self.__marks = m

    def info(self):
        print(self.name,self.__marks)

    def getmarks(self):
        #restrictions only for admin can read
        return self.__marks
    
    def setmarks(self,m):
        if m>0 and m<=100:
            self.__marks = m

# s1 = Student('raju',56)
# s1.info()
# s1.setmarks(78)
# res = s1.getmarks()
# #print(s1._Student__marks)
# print(res)

#so if you wants to use the setter and getter methods in variable way you can use @property


class Student2:
    def __init__(self,n,m):
        self.name = n
        self.__marks = m

    def info(self):
        print(self.name,self.__marks)

    @property
    def marks(self):
        #restrictions only for admin can read
        return self.__marks
    @marks.setter
    def marks(self,m):
        if m>0 and m<=100:
            self.__marks = m

s1 = Student2('raju',56)
s1.info()
s1.marks = 78#accessing as variable
res = s1.marks#acessing as a variable
#print(s1._Student__marks)
print(res)
