#student marks,average,info

class Student:
    def __init__(self,n,a,marks):
        self.name = n
        self.age = a
        self.marks = marks

    def info(self):
        print(f'student name is {self.name} and age is {self.age}')

    def average(self):
        avg = sum(self.marks)//3
        print(f'student average marks are {avg}')

s = Student('harish',21,[80,85,75])
s.info()
s.average()