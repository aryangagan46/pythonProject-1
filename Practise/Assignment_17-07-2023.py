class Flipkart_Ecom():

    def __init__(self, username, password, categories1, categories2):

        self.username = username
        self.password = password
        self.categories = categories1
        self.categories0 = categories2

    def Login(self):

        print("Welcome to Flipkart.com")
        while True:
            Enter_Username = input("Enter Username/Mobile Number):----")
            Enter_Password = input("Enter Password (with in 8 character):----")

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
        for key, value in categories1.items():
            print(key, value)
            print()

    def categories1(self):
        input("Select Category:-->")
        for key, value in Groceries.items():
            print(key, value)

        print("<<<<<<<<<<<<<<<<<<<<<<< End of the Groceries List >>>>>>>>>>>>>>>>>>>")
    def categories2(self):
        print()
        input("Select Category:-->")
        for key2, value2 in Mobile.items():
            print(key2, value2)

        print("<<<<<<<<<<<<<<<<<<<<<<< End of the Mobile/ Electronics List >>>>>>>>>>>>>>>>>>>")


"""Inputs"""
username = "Madivalar"
password = "1234578"

categories1 = {
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

Mobile = {
    "Apple-14_Pro_Max": "Rs: 1,10,000",
    "Samsung_S_23": "Rs: 85,000",
    "Nokia_X_20": "Rs: 55,000",
    "Nothing_X": "Rs: 45,000",
    "Oneplus_Hazelwood": "Rs: 53,000"
}

obj1 = Flipkart_Ecom(username, password, categories1, categories1)
obj1.Login()
obj1.Dashboard()
#obj1.password()
obj1.categories1()
obj1.categories2()