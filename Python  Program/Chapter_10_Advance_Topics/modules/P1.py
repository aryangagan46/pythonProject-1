
class TV:

    def __init__(self,model,manufacturer):
        self.model = model
        self.manufacturer = manufacturer


    def TV_Model(self):
        print("1).TV Brand Name {}\n 2).the Model is {}".format(self.manufacturer,self.model))



model = {
"MODEL_NAME" : "IOS-DESKTOP-232"
}

manufacturer = {
"BRAND is " : "APPLE"
}


Obj1 = TV(model,manufacturer)
Obj1.TV_Model()


