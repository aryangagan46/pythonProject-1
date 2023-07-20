# # def create_file():
# #
# #     path = r'c:\New\\'
# #     file = open(path + 'new.txt', "w")
# #     file.write('Darshan\n')
# #     file.write("\nWelcome to Hubli-Dharwad Municipal corporation\n 1.Admin Dept\n")
# #     print("Dept 1: -------------------File Created with name :", file.name,"\n")
# #     file.close()
# #
# # create_file()
# #
# # def read_file():
# #
# #     path = r'c:\New\\'
# #     file = open(path + 'new.txt', "r")
# #     content = file.read()
# #     print("File has the below content---------------\n\n",content)
# #     print()
# #     file.close()
# #
# # read_file()
# #
# # def append():
# #     path = r'c:\New\
# #     \'
# #     file = open(path + 'new.txt', "a")
# #     print()
# #     file.write(" 2.Finance Dept")
# #     file.close()
# #
# # append()
# #
# # """
# # w = new file creating
# # r = read the existing file
# # a = add the content into existing file
# # """
# #
#
#
# class HDMC_Hubli():
#     #
#     # def __init__(self,path):
#     #     self.path = path
#
#     def create_file(self):
#         file = open(path + 'new.txt', "w+")
#         file.write('Darshan\n')
#         file.write("\nWelcome to HUbli-Dharwad Municipal corporation\n 1.Admin Dept\n")
#         file.seek(0)
#         content = file.read()
#         print("Dept 1: -------------------File Created with name :", content , "\n")
#         file.close()
#
#
#     def read_file(self):
#         file = open(path + 'new.txt', "r+")
#         content = file.read()
#         print("File has the below content---------------\n\n", content)
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
# HDMC = HDMC_Hubli()
# HDMC.create_file()
# HDMC.read_file()
# HDMC.append()


def funn(a, b, c):
    if (2 + c + b) < (8 + b + a):
        a = a & 0  # Assuming 'async' was meant to be '0'
    else:
        c = b + b
    b = (c + 12) + a
    return a + b + c

# Example usage
result = funn(3, 4, 5)
print(result)
