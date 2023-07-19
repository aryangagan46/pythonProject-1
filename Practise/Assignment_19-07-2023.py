"""
Write a pgm to find the student percentage
"""

class MGMK_School():

    def __init__(self,student_name,student_percentage,student_class):
        self.student_name = student_name
        self.student_percentage = student_percentage
        self.student_class = student_class

    def Student_Database(self):
        print()
        print("Database Contains list of Students with Percentage secured in Vth class. ")
        print()
    def Student_Names(self):

        for student,names in student_name.items():
            print(student,names)

class Percentage_secured(MGMK_School):

    def __init__(self,student_name,student_percentage,student_class):
        super().__init__(student_name,student_percentage,student_class)

    def Student_Percentages(self):
        while True:

            percentage = float(input("Enter the percentage: --->"))
            if percentage == 60 or percentage == 65:
                print({},format(self.student_name))
                break
            elif percentage == 66 or percentage == 70:
                print({},format(self.student_name))
                break
            else:
                print({},format(self.student_name))



student_name = {

"Student1 -" : "Darshan M",
"Student2 -" : "Darshan SR",
"Student3 -" : "Harshit"

}

student_percentage = {
"Percentage for Darshan" : "60%",
"Percentage for Darshan SR" : "70%",
"Percentage for Harshit" : "80% "
}

student_class = {
"Class1" : "5 - A Sec. ",
"Class2" : "5 - B Sec. ",
"Class3" : "5 - C Sec. "
}

MGMK_School = Percentage_secured(student_name,student_percentage,student_class)
MGMK_School.Student_Percentages()