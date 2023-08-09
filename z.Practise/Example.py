# "Sum of 3 digit "
#
# num = int(input("Enter 3 digit:" ))
#
# a = num % 10
#
# num1 = num // 10
#
# b = num1 % 10
#
# c = num1 // 10
#
#
# sum = (a + b + c)
#
# print(sum)
#
# #*****************************************************
#
# #Input
# a = 2
# b = 3
#
# #Output
# a = 3
# b = 2

#*****************************************************

class Flipkart_Ecom():

    def __init__(self, username, password, Categories, Groceries, Electronics):
        self.username = username
        self.password = password
        self.Categories = Categories
        self.Groceries = Groceries
        self.Electronics = Electronics

    def Login(self):
        print("Welcome to Flipkart.com")
        while True:
            Enter_Username = input("Enter your Username:")
            Enter_Password = input("Enter your Password:")

            if Enter_Username == self.username and Enter_Password == self.password:
                print("Login was Successfull!")
                print()
                print("--------->>>>>>>>>> Navigating to Homepage <<<<<<<<<----------------")
                break
            else:
                print("Sorry....Login was Failed - Try Again")

    def Dashboard(self):
        print()
        print("::::::Welcome to Flipkart HomePage---Unique Happy for Shopping::::::")
        print()
        for key, value in Categories.items():
            print(key, value)
            print()

    def GroceriesList(self):
        while True:
            Z1 = input("Select Category:-->")
            if Z1 == '1':
                for Name, Item in Groceries.items():
                    print(Name, Item)
                break
            else:
                print("End of the List")
            print()


    def ElectronicsList(self):
        while True:
            Y1 = input("Select Category:-->")
            if Y1 == '2':
                for Name2, Item2 in Electronics.items():
                    print(Name2, Item2)
                break
            else:
                print("End of the List")
            print()


"""Credentials"""
username = "Darshan"
password = "12345"

Categories = {
    "1).": "Groceries",
    "2).": "Mobiles",
    "3).": "Home_Appliance",
    "4).": "Books"
}

Groceries = {
    "Rice_Sonamasuri_Steam": "60/kg",
    "Rice_Sonamasuri_Raw": "70/kg",
    "Rice_Bullet_Steam": "65/kg",
    "Rice_Bullet_Raw": "76/kg",
    "Rice_Basumathi_India_gate": "100/kg",
    "Wheat_Gujurat": "55/kg",
    "Jowar_Bijapur": "40/kg"
}

Electronics = {
    "Apple-14_Pro_Max": "Rs: 1,10,000",
    "Samsung_S_23": "Rs: 85,000",
    "Nokia_X_20": "Rs: 55,000",
    "Nothing_X": "Rs: 45,000",
    "Oneplus_Hazelwood": "Rs: 53,000"
}

obj1 = Flipkart_Ecom(username, password, Categories, Groceries, Electronics)
obj1.Login()
obj1.Dashboard()
obj1.GroceriesList()
obj1.ElectronicsList()
