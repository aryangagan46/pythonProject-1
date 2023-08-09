# #Write a pgm to add Numbers
#
# Progress_Report = [100, 99, 98, 97, 96, 95]
# print(" Marks in Each subject is :", Progress_Report)
# print()
# result = 0
#
# for num in Progress_Report:
#     print(" Marks in subject:", num)
#     result = result + num
#     print()
#     print(" Total Maximum Number (Iterativley) :", result )
#
# print()
# print(" Total Maximum Marks:", result)
#
# print("******************************************************")
#
# def Maximum_marks_in_report():
#     Progress_Report = [100, 99, 98, 97, 96, 95]
#     print(" Marks in Each subject is :", Progress_Report)
#     print()
#     result = 0
#
#     for num in Progress_Report:
#         print(" Marks in subject:", num)
#         result = result + num
#         print()
#         print(" Total Maximum Number (Iterativley) :", result)
#
#     print()
#     print(" Total Maximum Marks:", result)
#
# Maximum_marks_in_report()
#
# def Iterative_letters():
#
#     List = ["Darshan Madivalar"]
#     print(" My Name is :", List)
#
#     for Letters in List:
#         for Iterative in Letters:
#             print(Iterative)
#
# Iterative_letters()
#
#
# def Iterative_Integers():
#
#     Num = ['12545567543.d']
#     print(" Integers in List is :", Num)
#
#     for Numb in Num:
#         for Numb1 in Numb:
#             print(Numb1)
#
# Iterative_Integers()
#
# print()
#
# #Find Even Number in List
#
# def Even_Odd_Iterative():
#
#     List4 = ['Darshan Madivalar']
#     List1 = [1, 2, 3, 423, 4, 3, 8, 43, 22]
#
#     for Even in List1:
#         if Even % 2 == 0:
#             print(Even)
#
#     print()
#     for Odd in List1:
#         if Odd % 2 ==1:
#             print(Odd)
#     print()
#     for Letters1 in List4:
#         #for Letters2 in List4:
#          print(Letters1[0:7])
#          print(Letters1[8:17])
#     print()
#
# Even_Odd_Iterative()

#
# val = (1,2,'darshan')
#
# # print(val[2])
# val[2] = "Rahul"




# #1st Aproach
# dict = {"firstname": "Darshan", "Last Name" : "Madivalar", "Gender" : "Male" }
# print(dict)
#
# #2nd Aproach
# dict = {}
# dict["firstname"] = "Darshan"
# dict["Last Name"] = "Madivalar"
# dict["Gender"] = "Male"
# print(dict)
#
# #3rd Aproach - Print Particular Variable in Dictionary
# print(dict["Gender"])
#
#
# print()
#
# #if else Condition
#
# list = "Good Morning"
#
# if list == "Good Morning":
#     print('Condition Matches')
#
# else:
#     print("Condition Doesn't Match")
#
# print("if else condition is complete")
#
# print()
#
# ---------------#for loop Condition------------------
#
# obj = [1,2,3,4,5,6,7,8]
#
# for i in obj:
#     print(i)
#
# print()
#
# for i in obj:
#     print(i*2)
#
# print()
# for j in obj[1:6]:      #--------- (n-1) at last index
#     print(j)
#
# print()
# #obj = [1,2,3,4,5,6,7,8]
# sum = 0
# for j in obj[0:6]:
#     sum = sum + j
# print(sum)

print()
#--------------------Jump Condition--------------------

# for k in range (1, 20, 2):
#     print(k)
#
# print()
# for m in range (10):
#     print(m)

#----------------while Loop Condition---------------------

#used to check the coondition
# it = 5
# while it >= 1:
#     print(it)
# #     it = it -1
#
# #skip middle of the list
# #
# it = 10
# while it !=4:
#     print(it)
#     it = it - 1
#
# #Break condition
#
# it = 10
# while it > 1:
#     if it == 3:
#             break
#     print(it)
#     it = it - 1

#Continue Condition
#
# it = 10
# while it > 1:
#     if it ==7:
#         it = it -1
#         continue
#     if it == 3:
#         break
#     print(it)
#     it = it -1

#Functions

#IT IS A GROUP OF RELATED STATEMENTS THAT PERFORM SPECIFIC TASK

#FUNCTION DECLERATION
#
# def Greetme(name):
#
#     print(" Goodmorning"+ name)
#
# def addinteger(a,b):
#     return a + b
#     #print(addinteger(a,b))
#
# Greetme("Darshan")
# addinteger(2,3)

def prime():
    a = int(input("enter number"))
    if a == 1:
        for x in range(2, a):
            if (a % x) == 0:
                print("not prime")
            break
    else:
        print("Prime")

prime()