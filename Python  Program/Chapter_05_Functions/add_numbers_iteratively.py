"""WRITE A PROGRAM TO ADD THE NUMBERS ITERATIVELY """

#Input
list = [ 44, 45, 98, 65, 77, 66]
print("Marks in the Progress Report is", list)

result = 0
for num in list:
    print(" Marks for each Subject ", num)
    result = result + num
    print( " Result of each iteration", result)

print(" Final sum of marks:" , result)

print("********************************************************************")

"Call the Program using Function"

def Maximum_Marks_in_the_progress_report():

    Progress_report = [98, 97, 99, 89, 93, 99]
    print("Marks in subject is :", Progress_report )

    Maximum_Marks = 0
    for Marks in Progress_report:
        print(" Marks in subject is :\n", Marks)
        Maximum_Marks = Maximum_Marks + Marks
        print(" Total Maximum Marks in Subject is :", Maximum_Marks)

Maximum_Marks_in_the_progress_report()

def Iterative_Letters():

    Name = ['Darshan']
    print(" Print your each letters of name iteratively")

    for letters in Name:
        for List in letters:
            print(List)

Iterative_Letters()

def Find_even_numbers(Tab):

    Table = [0,1,2,3,4,5,6,7,8,9,10]
    print(" Numbers in Table is: ", Table)

    for Even in Table:
        if Even % 2 == 0:
            print("Print even number from Table :", Even)

    print('\n')

    for Odd in Table:
        if Odd % 3 == 0:
            print("Print Odd number from Table :", Odd)

    print('\n')

    for String in Tab:
        if String in Names2:
           print(String)

Names2 = ['Darshan, Harsha, Arbaz']
Find_even_numbers(Names2)


