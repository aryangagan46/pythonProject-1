This program adds two numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {} and {} is {}'.format(num1, num2, sum))
print('The sum of %g and %g is %g' %(num1, num2, sum))
print("The Sum of Both the number is :", num1+num2)
print("The Sum of Both the number is :",sum)
print("The Sum of",num1,"and",num2, "is:",sum)



Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))



print('The sum is %.1f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))


"""Write a Program on Train Details in IRCTC portal"""
print()
class irctc():
    def __init__(self,Vandebharat, Duranto, Fare_AC_Exe):
        self.Train_Name1 = Vandebharat
        self.Train_Name2 = Duranto
        self.BaseFare1 = Fare_AC_Exe
        self.BaseFare2 = Fare_AC_Chair
    def Train_Number(self):
        print("1). Train Number1 :",Train_Number1, " - Dharwad to Bangalore:", self.Train_Name1)
        print()
        print("2). Train Number2 :",Train_Number2, " - Bangalore to Howrah:", self.Train_Name2,'Express')

    def Train_Coach(self):
        print()
        print("Train Name :", Train_Name2,"Train No.:",Train_Number2 )
        print("Coach Managment System")
        print()
        for AC_Coach in a:
            print("No. of AC Three Tier Coach is :", AC_Coach)
            for AC_Coach in b:
                print("No. of AC Two Tier Coach is :",AC_Coach)
                for AC_Coach in c:
                    print("No. of AC First Class Coach is :",AC_Coach)
                    for Sleeper_Coach in d:
                        print("No. of Sleeper Coach is", Sleeper_Coach)
        print("Total Coaches in",Train_Number2,Train_Name2,"is:", Total_Coach)


    def Train_Coach2(self):
        print()
        print("Train Name :", Train_Name1,": Train No.:", Train_Number1)
        print("Coach Managment System")
        print()
        for AC_Chaircar in a:
            print("No. of AC Chaircar is :", AC_Chaircar)
            for AC_Executive_Car in b:
                print("No. of AC Executive Coach is :", AC_Executive_Car)
        print("Total Coaches in", Train_Number1, Train_Name1, "is:", Total_Coach1)

    def Train_Fare(self):
        print()
        print("--Total Fare for AC Executive Car in ", Train_Number1,Train_Name1,"is Rs.--",Fare_AC_Exe)
        print()
        print("--Total Fare for AC First Class in ", Train_Number2, Train_Name2, "is Rs.--",Fare_AC_Chair)



print('******************************************************')
print()
#
# Train_Coach_Man = {"3AC" : 4,"2AC" : 6, "1AC" : 2, "Sleeper" : 9}
# Value1 = Tra

a = '4'
A = int(a)
b = '6'
B = int(b)
c = '2'
C = int(c)
d = '9'
D = int(d)

Total_Coach = A+B+C+D
Total_Coach1 = A+B
Train_Name1 = '
Train_Name2 = 'Duranto'
Train_Number1 = 20662
Train_Number2 = 12246
BaseFare = 1500
Fare_AC_Exe = [(BaseFare*0.18)+(BaseFare)]
Fare_AC_Chair = [(BaseFare/1.5)]

obj1 = irctc (Train_Name1, Train_Name2,Fare_AC_Exe)
obj1.Train_Number()
obj1.Train_Coach()
obj1.Train_Coach2()
obj1.Train_Fare()

print('******************************************************')
print()
Train_Name2 = 'Rajadhani'
Train_Name1 = 'Shathabdi'
Train_Number4 = 28374
Train_Number3 = 54637

obj2 = irctc (Train_Name1, Train_Name2,Fare_AC_Exe)
obj2.Train_Number()
obj2.Train_Coach()
obj2.Train_Coach2()
