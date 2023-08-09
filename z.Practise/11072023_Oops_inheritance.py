#Parent class method
class NWKRTC:

    # Class Variable
    Bus_Num = "KA-26-F-2023"
    Bus_Num1 = "KA-63-F-2024"
    print()
    print("Welcome to [N-W-K-R-T-C] ---- Gadag-Betageri Depot")

    # Default Constructor
    def __init__(self,Fare):
        self.Type = Fare                         #Instance Varibale
        print()
        print("Bus Route:::: GADAG(BETAGERI) ----->>>>> GOA(Panaji)")
        print("Bus Number is:",NWKRTC.Bus_Num)

    #Instance Method
    def Bus_Type(self):
        print()
        print("Bus Class and Types:")
        print()
        for Buses, Class in Fare.items():
            print(Buses,Class)
    print('*************************************************')

#Child Class Method
class MSRTC(NWKRTC):

    #Initialise Constructors from Parent Class

    def __init__(self):
        NWKRTC.__init__(self, Fare)
        print("parent class variable---------------------------",self.Type)


    def getFare(self):
        print('*************************************************')
        print()
        print("Welcome to [M -S-R-T-C] Mumbai DEPOT")
        print()
        print("BuS Route:::: MUMBAI(KURLA) ----->>>>>>> HUBBALLI(GOKUL)")
        print("Bus Number is:", MSRTC.Bus_Num1)
        print()
        for Buses1,Clases1 in Fare1.items():
            print(Buses1,Clases1)

    @staticmethod
    def Availability(Reserve):
        print("---------------------------------------------------------")
        print(Reserve["Avail"])
        if Reserve["Avail"] <= 5:
            print()
            print("Booking status for route GADAG ---->>>> GOA")
            print("Note: Ohoooo---SORRY--BUS was canceled due to No Bookings")
        elif Reserve["Avail"] <=45:
            print()
            print("Alert: Wohhhh---Limited Seat Available - FILLING FASTTTTT - Hurry Up")
        else:
            print()
            print("Note: Ohoooo-SORRY--No Booking Allowed, Bus Was Full")

    @classmethod
    def Buses_Count(cls,Count1,Count2):
        cls.Bus_GDG = Count1
        cls.Bus_HBL = Count2
        print()
        print("Bus Running status for Different Routes:")
        print("1). Current Running Status for Route GADAG -->> GOA is:- {}".format(cls.Bus_GDG),"Buses")
        print()
        print("2). Current Running Status for Route MUMBAI -->> HUBLI is:- {}".format(cls.Bus_HBL),"Buses")


Fare1 = {
"1). Shivneri SCANIA - Rs." : 2500,
"2). Ashwamedha AC Volvo Multi Axel- Rs." : 2000,
"3). Parivarthan Laal Pari- Rs." : 1500,
"4). Shivshahi AC Semi-Sleeper- Rs.": 1000
}

Fare = {
"1). Ambari Dream Class- Rs." : 2000,
"2). AIRAVAT VOLVO MULTI AXEL- Rs.": 1500,
"3). AC SLEEPER- Rs.": 1000,
"4). RAJAHAMSA- Rs.": 600
}


#Parent Class
BUS_ROUTE = NWKRTC(Fare)
BUS_ROUTE.Bus_Type()

#Child Class
BUS_ROUTE1 = MSRTC()
BUS_ROUTE1.getFare()

#Staticmethod
Avail1 = {'Avail' : 46}
BUS_ROUTE1.Availability(Avail1)

#classmethod
Counts = MSRTC()
Counts.Buses_Count(5, 7)