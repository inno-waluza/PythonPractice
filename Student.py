class Student():
    ##innocent's class
    def __init__(self, name , age , pg):
        self.name = name
        self.age = age
        self.pg = pg
    def details(self):
        print("student name is " + self.name.title())
        print("student age is " + self.age)
        print("student program is " + self.pg)

nm = input("enter your name ")
ag = input("enter your age ")
pg = input("enter your program of study ")

student = Student(nm,ag,pg)
student.details()
