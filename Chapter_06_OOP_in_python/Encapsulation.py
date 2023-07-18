"""
Encapsulation : making variable or method private
and secure data variable and method with "double underscores" -private
"""

class Car():

    def __init__(self,speed,color):
        self.__speed = speed
        self.__color = color
        self.model = 'x111'
        self.__secure_details()

    def __secure_details(self):
        print("Secure details")

    def car_info(self):
        print("Car speed: {}\ncar color: {} ".format(self.__speed,self.__color))

c = Car(200, 'RED')
#When it is __we cannot set the speed
c.__speed = 300
c.color = 'Blue'
c.car_info()
#outside we cannot access
#c.__Secure_details() #this does not work as expected
# c._Car__secure_details()

class ford(Car):

    def __init__(self,speed,color):
        super().__init__(speed,color)

    def car_info(self):
        print("Car details model:",self.model)
        #cannot access private members
        # print("car details model:", self.__speed)   #this does not work as expected

f = ford(500,'white')
f.car_info()
# #trying to access secure method
# f.__secure_Details() this does not worl as expected