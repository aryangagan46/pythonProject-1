"""
Single and multilevel Inheritance :
calling super method using child object
"""
class Student:

    def __init__(self):
        self.a = 5
        self.b = 10

    def info(self):
        print("Primary School info")
        print(self.a)
        print(self.b)

    @classmethod
    def sample_cls_method(cls):
        print("this is class method")

#single inheritance

class Highschool(Student):                      #single inheritance

    def info(self):
        print("High School info")

    stu1 = Student()
    stu1.info()

#multilevel inheritance
class College(Highschool): #multilevel

    def __init__(self):
        print("this is init method from college class")

    def info(self):
        print("College info")

coll1 = College()

class Music():

    def music_info(self):
        print("has details of student intrested in music")
    print("music class")

class MusicAcademy(Student,Music): #multiple inheritance

    st1 = Student()
    st1.info()

    Ms1 = Music()
    Ms1.music_info()