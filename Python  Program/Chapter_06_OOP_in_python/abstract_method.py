"""
abstract base class
example :API design : others can design based on their requirment
"""

from abc import ABC , abstractmethod

class VRL(ABC):
    @abstractmethod
    def Bus_details(self):
        pass

class Abhibus(VRL): 
    def Bus_details(self):
        print("Welcome to VRL Logistics Ltd : by Abhibus")

class RedBus(VRL):
    def Bus_details(self):
        print("Welcome to VRL Logistics Ltd : by Redbus")

A = Abhibus()
A.Bus_details()
R = RedBus()
R.Bus_details()

print("******************************************************")

class VRL():

    print()
    print("<<<<<<---Parent Webpage: VRL Logistics Limited--->>>>>>" )
    print()
    def __init__(self, RedBus, Abhibus, Paytm):
        self.Red_Bus = RedBus
        self.Abhi_bus = Abhibus
        self.Paytm_Bus = Paytm


    def OfficialWebVRL(self):

        print("Welcome to Vijayanand Roadlines (VRL) : Hubli")


class Platforms_Redbus(VRL):

    def __init__(self, RedBus, Abhibus, Paytm):
        # super.__init__(RedBus,Abhibus,Paytm)
        super().__init__(RedBus, Abhibus, Paytm)

    def OfficialWebVRL(self):

        for Key1,values1 in RedBus.items():
            print("Official Webpage for Redbus is :",(Key1,values1))

        print()

class Platforms_Abhibus(VRL):

    def __init__(self, RedBus, Abhibus, Paytm):
        super().__init__(RedBus, Abhibus, Paytm)

    def OfficialWebVRL(self):

        for Key2,value2 in Abhibus.items():
            print("Official Webpage for Abhibus is:", (Key2,value2))
        print()

class Platforms_Paytm(VRL):

    def __init__(self, RedBus, Abhibus, Paytm):
        super().__init__(RedBus, Abhibus, Paytm)

    def OfficialWebVRL(self):

        for Key3,value3 in Paytm.items():
            print("Official Webpage for Paytm is :",(Key3, value3))

RedBus = {
"Route No 01" : "Bangalore to Hubli",
"Bus Fare" : "Rs. 2500",
"Bus Type" : "Multi Axel Volvo AC Sleeper"
}

Abhibus = {
"Route No 02" : "Hubli to Udupi",
"Bus Fare" : "3000",
"Bus Type" : "Ambari_Utsav"
}

Paytm = {
"Route No 03" : "Hubli to Panvel",
"Bus Fare" : "4000",
"Bus Type" : " AC Sleeper"
}

Main = Platforms_Redbus(RedBus,Abhibus,Paytm)
Main.OfficialWebVRL()
Main1 = Platforms_Abhibus(RedBus,Abhibus,Paytm)
Main1.OfficialWebVRL()
Main2 = Platforms_Paytm(RedBus,Abhibus,Paytm)
Main2.OfficialWebVRL()

