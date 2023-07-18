"""
Inheritance: Inheriting parent class properties and polymorphism : method overriding
super() using it to do declare base class variables and also to call base class method
"""
import self as self

# class Student():    #Parent Class
#
#     school_name = "Indian Public School"        #Class Variable
#
#     def __init__(self,name, rollnum):
#         self.name = name                        #Instance Variable
#         self.rollnum = rollnum
#         print("hey am calling by object by default")
#
#     def student_info(self):                     #Instance Method
#         print("Student info parent class method : school information\n Name:"
#         " {}\n Rollnum: {}\n ".format(self.name, self.rollnum))
#         print("school name", Student.school_name)
#
# # class HighschoolStudent(Student):   #CHILD CLASS ITS INHERITING THE PROPERTIES OF STUDENT(PARENT) CLASS
# #
# #     def __init__(self,name, rollnum, sports):
# #         self.sports = sports
# #         super().__init__(name,rollnum)
# #
# #     def student_info(self):
# #         print("Student info child class method High school information \n Name:"
# #         "      {}\n Rollnum:      {}\n Sports:  {}\n".format(self.name, self.rollnum,self.sports))
# #
# #         #method overriding - polymorphism
# #         super().student_info()
#
# Highschool1= HighschoolStudent('amar', 1, 'cricket')   #object creation
# Highschool1.student_info()      #calling the method
#
print()

# #
# class Xuv_Cars():
#
#     Name_of_the_car = " Mahindra XUV "
#
#     def __init__(self,name1,name2):
#         self.XUV_500 = name1
#         self.XUV_700 = name2
#         print("XUV Mahindra Car Variants ")
#         print()
#
#     def Mahindra_Car_Varient(self):
#         print("PARENT Class")
#         print("XUV Varient release in year 2023-2024 are:",Xuv_Cars.Name_of_the_car)
#         print(" 1). Mahindra Car XUV Varients 1 is -  {}\n 2). Mahindra Car XUV Varient 2 is - {}\n"
#               .format(self.XUV_500,self.XUV_700))
#
#
# # class Car_color_model(Xuv_Cars):
# #
# #
# #     def __init__(self,XUV_500, XUV_700, color, model):
# #         self.color = color
# #         self.model = model
# #         super().__init__(XUV_500,XUV_700)
# #         super().Mahindra_Car_Varient()
#
#     #
#     # def Mahindra_Car_Varient(self):
#     #     print("CHILD CLASS")
#     #
#     #     print(" 3).Color of the both XUV's are - {}\n 4).Model of the both XUVs are {}\n "
#     #           .format(self.color,self.model))
#
#

# Mahindra_Cars = Car_color_model('XUV-500','XUV_700','red',2017)
# Mahindra_Cars.Mahindra_Car_Varient()
#
#Duplicate
# class Bank():
#
#     Bank_Name = 'State Bank of India_Hubli'
#
#     def __init__(self, Name, Account_Num, Branch):
#         self.Customer_Name = Name
#         self.Customer_Account_Num = Account_Num
#         self.Branch_Name = Branch
#     print()
#     print("******----Customer Database - Corporate Office_Bangalore Division----******")
#     print()
#     def Customer_Details(self):
#
#         print("1). Customer_Name: {}\n"
#               "2). Customer_Account_Num: {}\n"
#               "3). Branch Name : {}\n"
#                 .format(self.Customer_Name,self.Customer_Account_Num,self.Branch_Name))
#
#
# class Accoutn_Details(Bank):
#
#     def __init__(self,Name, Account_Num, Branch, CIF_Num, Mobile_Num):
#         self.Customer_CIF_Number = CIF_Num
#         self.Customer_Mobile_Num = Mobile_Num
#         print("Bank Name : ", Bank.Bank_Name)
#         print()
#         print("Customer Account Details  --->:")
#         print()
#         super().__init__(Name,Account_Num,Branch)
#         super().Customer_Details()
#
#     def Customer_Details(self):
#         print("****----Other Details required for KYC process:---->")
#         print("4). Customer CIF number is : {}\n"
#               "5). Customer Mobile Number is : {}\n"
#         .format(self.Customer_CIF_Number,self.Customer_Mobile_Num))
#
# class KYC_Details(Accoutn_Details):
#
#     def __init__(self, Name, Account_Num, Branch, CIF_Num, Mobile_Num,Adharcard):
#         self.Adhar_Card_Number = Adharcard
#         super().__init__(Name,Account_Num,Branch,CIF_Num,Mobile_Num)
#         super().Customer_Details()
#
#     def Customer_Details(self):
#         print("****----Customer KYC Detail :---->")
#         print("6). Aadhar Card Seeding with NEW Bank Account Num.: {}".format(self.Adhar_Card_Number))
#
# class Address(KYC_Detail):
#
#     def __init__(self,Name, Account_Num, Branch, CIF_Num, Mobile_Num,Adharcard,Address):
#         self.Communication_Address = Address
#         super().__init__(Name, Account_Num, Branch, CIF_Num, Mobile_Num,Adharcard,)
#         super().Customer_Details()
#
#     def Customer_Details(self):
#         print()
#         print("****---Contact Address---->")
#         print("7). Address For Communication:--> {}".format(self.Communication_Address))
#
# class Other_Bank_Details(Addres):
#
#     def __init__(self,Name, Account_Num, Branch, CIF_Num, Mobile_Num,Adharcard,Address,
#                  IFSC, MICR, BRANCH_CODE, ZIPCODE):
#         self.Branch_IFSC_Code = IFSC
#         self.Branch_MICR_Code = MICR
#         self.Branch_Code = BRANCH_CODE
#         self.Branch_Zip_Code = ZIPCODE
#         super().__init_(Name, Account_Num, Branch, CIF_Num, Mobile_Num,Adharcard,Address)
#         super().Customer_Details()
#
#     def Customer_Details(self):
#         print()
#         print("****----Other Bank Details:---->")
#         print("8). Bank IFSC Code: {}\n"
#               "9). Bank MICR Code: {}\n"
#               "10).Bank Branch Code: {}\n"
#               "11).Bank ZipCode: {}\n"
#               .format(self.Branch_IFSC_Code,self.Branch_MICR_Code,self.Branch_Code,self.Branch_Zip_Code))
#
# Bank1 = Other_Bank_Details('Darshan', 2393837263,'Hubli', 9898778987 ,
# 7200000002, 237878665645, 'Navanagar- Hubli', 'SBIN0000838',
# '0000838', 3342536273, 582101)
# Bank1.Customer_Details()


#Original
class Bank():

    Bank_Name = 'State Bank of India_Hubli'

    def __init__(self, Name, Account_Num, Branch):
        self.Customer_Name = Name
        self.Customer_Account_Num = Account_Num
        self.Branch_Name = Branch
    print()
    print("******----Customer Database - Corporate Office_Bangalore Division----******")
    print()
    def Customer_Details(self):

        print("1). Customer_Name: {}\n"
              "2). Customer_Account_Num: {}\n"
              "3). Branch Name : {}\n"
                .format(self.Customer_Name,self.Customer_Account_Num,self.Branch_Name))


class Accoutn_Details(Bank):

    def __init__(self,Name, Account_Num, Branch, CIF_Num, Mobile_Num):
        self.Customer_CIF_Number = CIF_Num
        self.Customer_Mobile_Num = Mobile_Num
        print("Bank Name : ", Bank.Bank_Name)
        print()
        print("Customer Account Details  --->:")
        print()
        super().__init__(Name,Account_Num,Branch)
        super().Customer_Details()

    def Customer_Details(self):
        print("****----Other Details required for KYC process:---->")
        print("4). Customer CIF number is : {}\n"
              "5). Customer Mobile Number is : {}\n"
        .format(self.Customer_CIF_Number,self.Customer_Mobile_Num))

class KYC_Details(Accoutn_Details):


    def __init__(self, Name, Account_Num, Branch, CIF_Num, Mobile_Num, Adharcard):
        self.Adhar_Card_Number = Adharcard
        super().__init__(Name,Account_Num,Branch,CIF_Num,Mobile_Num)
        super().Customer_Details()

    def Customer_Details(self):
        print("****----Customer KYC Detail :---->")
        print("6). Aadhar Card Seeding with NEW Bank Account Num.: {}".format(self.Adhar_Card_Number))

class Address(KYC_Details):

    def __init__(self,Name, Account_Num, Branch, CIF_Num, Mobile_Num,Adharcard,Address):
        self.Communication_Address = Address
        super().__init__(Name, Account_Num, Branch, CIF_Num, Mobile_Num,Adharcard,)
        super().Customer_Details()

    def Customer_Details(self):
        print()
        print("****---Contact Address---->")
        print("7). Address For Communication:--> {}".format(self.Communication_Address))

class Other_Bank_Details(Address):

    def __init__(self,Name, Account_Num, Branch, CIF_Num, Mobile_Num,Adharcard,Address,
                 IFSC, MICR, BRANCH_CODE, ZIPCODE):
        self.Branch_IFSC_Code = IFSC
        self.Branch_MICR_Code = MICR
        self.Branch_Code = BRANCH_CODE
        self.Branch_Zip_Code = ZIPCODE
        super().__init__(Name, Account_Num, Branch, CIF_Num, Mobile_Num,Adharcard,Address)
        super().Customer_Details()

    def Customer_Details(self):
        print()
        print("****----Other Bank Details:---->")
        print("8). Bank IFSC Code: {}\n"
              "9). Bank MICR Code: {}\n"
              "10).Bank Branch Code: {}\n"
              "11).Bank ZipCode: {}\n"
              .format(self.Branch_IFSC_Code,self.Branch_MICR_Code,self.Branch_Code,self.Branch_Zip_Code))

Bank1 = Other_Bank_Details('Darshan', 2393837263,'Hubli', 9898778987 ,
7200000002, 237878665645, 'Navanagar- Hubli', 'SBIN0000838',
'0000838', 3342536273, 582101)
Bank1.Customer_Details()