

# def create_file():
#
#     path = r'c:\New\\'
#     file = open(path + 'new.txt', "w")
#     file.write('Darshan\n')
#     file.write("\nWelcome to HUbli-Dharwad Municipal corporation\n 1.Admin Dept\n")
#     print("Dept 1: -------------------File Created with name :", file.name,"\n")
#     file.close()
#
# create_file()
#
# def read_file():
#
#     path = r'c:\New\\'
#     file = open(path + 'new.txt', "r")
#     content = file.read()
#     print("File has the below content---------------\n\n",content)
#     print()
#     file.close()
#
# read_file()
#
# def append():
#     path = r'c:\New\\'
#     file = open(path + 'new.txt', "a")
#     print()
#     file.write(" 2.Finance Dept")
#     file.close()
#
# append()
#
# """
# w = new file creating
# r = read the existing file
# a = add the content into existing file
# """



class HDMC_Hubli():

    def __init__(self,path):
        self.path = path

    def create_file(self):
        print(self.path)
        file = open(path + 'new.txt', "w")
        file.write('Darshan\n')
        file.write("\nWelcome to HUbli-Dharwad Municipal corporation\n 1.Admin Dept\n")
        print("Dept 1: -------------------File Created with name :", file.name, "\n")
        file.close()


    def read_file(self):
        # print(self.path)
        file = open(path + 'new.txt', "r")
        content = file.read()
        print("File has the below content---------------\n\n", content)
        print()
        file.close()


    def append(self):
        # print(self.path)
        file = open(path + 'new.txt', "a")
        print()
        file.write(" 2.Finance Dept")
        file.close()

path =  r'c:\New\\'


HDMC = HDMC_Hubli(path)
HDMC.create_file()
HDMC.read_file()
HDMC.append()
