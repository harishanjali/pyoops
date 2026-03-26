#access modifieres
#public/private/protected

#public-can access inside and outside
#private -  cannot access outside, can access inside - __marks
#potected- cannot access outside, can access parent, not child - _marks

# example

class Student:
    def __init__(self,n,m):
        self.name = n
        self.marks = m
    def info(self):
        print(self.name,self.marks)

    def getsign(self):
        if self.marks>70:
            print('happily signed')
        else:
            print('will discuss')

#so if you wants to access the private variable from outiside
#_Student__marks if it is private variable

s1 = Student('hari',73)
s1.getsign()