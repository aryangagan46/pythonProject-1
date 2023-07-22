# class HDMC_Hubli():
#
#     def __init__(self,path):
#         self.path = path
#
#     def create_file(self):
#         file = open(path + 'new.txt', "w+")
#         file.write('HUBLI DHARWAD MUNICIPAL CORPORATION -RANI CHENNAMMA CIRCLE - HUBLI\n')
#         file.write("\n Welcome to HUbli-Dharwad Municipal corporation\n "
#                    "\n 1. Admin Dept \n 2. Finance Dept \n 3. Revenue Dept \n 4. Tax Dept.")
#         file.seek(0)
#         content = file.read()
#         print("*****************************************")
#         print(" File Created with name :", content , "\n")
#         file.close()
#
#
#     def read_file(self):
#         print("***************************************************************")
#         file = open(path + 'new.txt', "r+")
#         content = file.read()
#         print("*****************File has the below content**************\n", content)
#         print()
#         file.close()
#
#
#     def append(self):
#         file = open(path + 'new.txt', "a+")
#         print()
#         file.write(" 2.Finance Dept")
#         file.close()
#
# path =  r'c:\New\\'
#
# HDMC = HDMC_Hubli(path)
# HDMC.create_file()
# HDMC.read_file()
# HDMC.append()


class ORION_MALL():

    def __init__(self,path):
        self.path = path


    def UG_Floor(self):

        file = open(path + "UG_Floor_Details.txt", "w+")
        file.write("\n UG_FLOOR_DETAILED_VEHICLE_PARKING_FLOORS\n")
        file.write("\n 1). TOTAL VEHICLE ACCEPTED  >= 300\n")
        file.seek(0)
        context = file.read()
        print(" File is created with :", context)
        file.close()

    def UG2_FLOOR(self):
        print()
        file = open(path + "UG_Floor_Details.txt", "r+")
        content = file.read()
        print(" Floor Contains the mentioned Details :", content)

    def FIRST_FLOOR(self):
        print()
        file = open(path +"UG_Floor_Details.txt", "a+")
        print()
        file.write("\n FIRST FLOOR CONTAINS SHOPS :\n"
                   "\n 1). KFC. \n 2). Mc Donalds. \n 3). Burger King.")
        file.seek(0)
        content1 = file.read()
        print(" Data for Floor is :", content1)
        file.close()

path =  r'c:\New\\'

hotel = ORION_MALL(path)
hotel.UG_Floor()
hotel.UG2_FLOOR()
hotel.FIRST_FLOOR()

