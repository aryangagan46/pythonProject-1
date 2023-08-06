
class Washingmachine():                                         #Parent Class

    WashingMachine1 = 'Samsung Electronics Washing machine'     #Class Variable

    def __init__(self,Item1):                                    #Method
        print('*********************************************************')
        print("Washing Machine Company: ",Washingmachine.WashingMachine1)
        self.clothtype1 = Item1                                  #Instance Variable
        self.timer1 = Item1
        self.temperature1 = Item1
        print()

    def Type(self,type1,type2):
        self.FrontLoad1 = type1
        self.TopLoad1 = type2
        print("There are Two types of Waching Machines",
              "\n1.",self.FrontLoad1,
              "\n2.",self.TopLoad1)
        print()

    @classmethod
    def Count_type(cls, Counts):                                #Class method
        cls.Counts1 = Counts
        print("No. of cloths count for ",Item1['clothtype'],"is: {} Nos.".format(cls.Counts1))

    @staticmethod                                               #Static method
    def is_timer1(Num):
        if Num["timer"] == 10 or Num["timer"] == 15:
            print()
            print("Result: Machine Under spin mode")
        else:
            print("Result: Machine under Rinse Mode")


class Other_Details(Washingmachine):

    def __init__(self,Item1,type1,type2,Cloth):
        self.Cloth_category1 = Cloth
        super().__init__(Item1,type1,type2)


    def Cloth_category(self):
        print("Cloth Types with Basic specifications: {} ".format(self.Cloth_category1))

Item1 ={
"clothtype" : "denim",
"timer" : "100 sec",
"temp." : "40 deg"
}
Item2 ={
"clothtype" : "Cotton",
"timer" : "150 sec",
"temp." : "30 deg"
}

type1 = 'FrontLoad'
type2 = 'TopLoad'

#
SamSungEle = Washingmachine(Item1)
SamSungEle.Type(type1,type2)
SamSungEle.Count_type(10)

#Staticmethod- I/P
Timers = {'timer' : 9}
SamSungEle.is_timer1(Timers)

Category1 = Other_Details("Cloth")
Category1.Cloth_category()


