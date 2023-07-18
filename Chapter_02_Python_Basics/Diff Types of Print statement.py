'********* Different types of Print Statements **********'

fname  = ' Darshan'
lname = 'Madivalar'
age = 30
reg_number = 1001
percentage_obtained = 80.02
Total_Marks = 5050


print(" Name of the candidate is = %s \n Age of the candidate is = %d" %(fname,age))
print(" Full Name of the Candidate is = {} {}" "\n Register Number of the Candidate is = {}".format(fname,lname,reg_number))
print(" Percentage of the Candidate is  = {}" "\n Total Marks Obtained by the Candidate is = {} ".format(percentage_obtained,Total_Marks))


#************Example-1***********

name='Rajesh'
age=15
address='Gadag'
pincode=582101
weather_temperature= 36.72
place_exist= True
Country_name= 'INDIA'
Continent_Name= 'Asia'

print(" Name of the candidate is = %s \n age of the candidate is = %d \n address of the candidate is = %s" %(name, age, address))
print(" Name of the Candidate is = {}" "\n Age of the Candidate is = {}".format(name,age))
print(" Address of the candidate is = {}" "\n Pincode of the candidate is = {}".format(address, pincode))
print(" Current Weather at the place is = %d" %(weather_temperature))
print(" Country name is = %s" %(Country_name))
print(" Continent Name is = {}".format(Continent_Name))


#************Example-2*************

Customer_ID= 100
Customer_FirstName = 'Arvind'
Customer_LastName= 'Bhat'
Customer_Address= 'Bangalore'
FoodName = 'Biriyani'
Quantity = 2
Price = 150
Gst = (18/100)
Total_Price = ((Price*2)*Gst)+(Price*2)

print(" Customer ID is = %d \n Customer Name is = %s %s" %(Customer_ID,Customer_FirstName,Customer_LastName))
print(" Customer Address is = {} " "\n Food Quantity = {}" "\n Customer Food = {}" "\n Total Price = {}" .format(Customer_Address,Quantity,FoodName,Total_Price))


#**************Example-3*****************

Test_Case_ID = 'MBL_001'
Test_Scenario = 'MBL_TS_001_Keypad Functionality'
Test_Case1= '(a) Verify that all the required buttons,numbers 0-9,calling buttons etc... ' \
            'are present on display '
Test_Case2= '(a) Verify that user can make a call by pressing numbers and hitting ' \
            'calling(green) button'
Test_Data= 'if Any'
Seviarity='Critical'
Priority='P3'
Result='Pass'

print('1. Test Case for Mobile Keypad Application is : \n%s' %(Test_Case1))
print('2. Test Case for Mobile Keypad Application is : \n{}'.format(Test_Case2))
print('3. Seviarity for Test_Case1 is : %s' %(Seviarity))
print('4. Priority for  Test_Case2 is : {}' '\n5. Result is : {}'.format(Priority,Result))


