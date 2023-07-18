# print("Write a Program to add numbers")
# def add_two_numbers():
#     a = 2
#     b = 3
#     c = a + b
#     print("Sum", c)
#
# add_two_numbers()
#
#
# print()
# print("Write a Program to add numbers with parameters")
# def add_two_nnumbers_1(a,b):
#     c = a + b
#     print("sum", c)
#
# add_two_nnumbers_1(2, 5)
#
# print()
# print("Write a Program to add numbers with RETURN Statement")
# def add_two_numbers_2(a,b):
#     c = a + b
#     return c
#
# print()
# print("Write a Program to add numbers with RETURN Statement")
# def add_two_numbers_3(*arg):
#
#     data = arg
#     sum = 0
#     for i in data:
#         sum = sum + i
#     return sum
# result = add_two_numbers_3(3,2,4)
# print(result)
#
# print("Write a Program to add numbers with RETURN Statement")
# def add_two_numbers_3(*arg, **kwargs):
#
#     data = arg
#     data_kw = kwargs
#     sum = 0
#     for i in data:
#         sum1 = sum + i
#         print(sum1)
#
#     for j, k in data_kw.items():
#         print(j, k)
#
# result = add_two_numbers_3(3,2,4,name = 'darshan')
# print(result)
#
# print("Write a Program to add numbers & dictionary Statement")
# #
# print()
# def function(*wes, **kwargs):
#     data = wes
#     data_kw = kwargs
#     for i in data:
#         print(i)
#     for a, b in data_kw.items():
#         print(a, b)
# function(10, 20, [44,45,66,77,88], name = 'darshan')


""" Write a program to print the Student list using class"""

class students():
    def __init__(self,name, list):          #initialize object details
        self.student_name = name            #self details ex: filling the form
        self.list = list

    def student_details(self):
        print("name", self.student_name)
        print("list", self.list)

    def Student_total_Marks(self):
        result = 0
        for Marks in list:
            result = result + Marks
        print("Total Marks:", result)

    def Student_max_marks(self):
        for Maxi in list:
            maxi = max(list)
        print("Maximum marks is:", maxi)

    def Student_min_Marks(self):
        for Mini in list:
            mini = min(list)
        print("Minimum Marks is:", float(mini))

    def Student_Percentage(self):
        for perc in list:
            perc = (sum(list)/(6))
        print("Student Percentage:", round(perc, 2))

name = 'darshan'
list = [55,67,54,88,77,86]

obj1 = students(name, list)     #creating objects
obj1.student_details()          #calling methods using the object
obj1.Student_total_Marks()
obj1.Student_max_marks()
obj1.Student_min_Marks()
obj1.Student_Percentage()