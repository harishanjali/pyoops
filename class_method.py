#class method is used for entire class to perform some operations,
#for example if you wants to calculate the revenue of the college you can do with this.
#lets see how we can achieve this.

class Student:
    student_fees = []
    def __init__(self,n,a,c,f):
        self.name = n
        self.age = a
        self.course = c
        self.fees = f
        Student.student_fees.append(f)
    def info(self):
        print(f'student name is {self.name} and age is {self.age}')

    @classmethod
    def getrevenue(cls):
        total = sum(cls.student_fees)
        print(f'Total revenue is {total}')

s = Student('hari',21,'python',25000)
s1 = Student('siva',21,'python',25000)
s3 = Student('raju',21,'python',20000)
s.getrevenue()