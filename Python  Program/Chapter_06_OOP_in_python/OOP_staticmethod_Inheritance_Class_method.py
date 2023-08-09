import datetime


class Student():                                #Parent Class

    school_name = "Indian Public School"        #Class Variable

    def __init__(self,name, rollnum):
        self.name = name                        #Instance Variable
        self.rollnum = rollnum
        print("hey am calling by object by default")

    def student_info(self):                     #Instance Method
        print("Student info parent class method : school information\n Name:"
        " {}\n Rollnum: {}\n ".format(self.name, self.rollnum))
        print("school name", Student.school_name)

    @staticmethod
    def is_weekday(day):
        """
        neither applicable for class nor for instance but still needed in that case for static
        :methods
        :return:
        """
        if day.weekday() == 5 or day.weekday() == 6:
            print("Weekend")
        else:
            print("Weekday")

    def weekday(day):
        pass

class HighschoolStudent(Student):   #CHILD CLASS ITS INHERITING THE PROPERTIES OF STUDENT(PARENT) CLASS

    def __init__(self,name, rollnum, sports):
        self.sports = sports
        super().__init__(name,rollnum)

    def student_info(self):
        print("Student info child class method High school information \n Name:"
        "      {}\n Rollnum:      {}\n Sports:  {}\n".format(self.name, self.rollnum,self.sports))

        #method overriding - polymorphism
        super().student_info()

    @classmethod
    def class_fees(cls, fees):
        cls.fees = fees
        print("School Name {} & fees {}k".format(cls.school_name, cls.fees))

Highschool1= HighschoolStudent('amar', 1, 'cricket')    #object creation
Highschool1.student_info()                              #calling the method
Highschool1.class_fees(15)
mydate  = datetime.date(2023,7,10)
print( mydate )
HighschoolStudent.is_weekday( mydate )

