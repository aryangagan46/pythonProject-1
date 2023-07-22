def create_file():

    path = r'c:\New\\'
    file = open(path + 'new.txt', "w")
    file.write('Darshan\n')
    file.write("\nWelcome to Hubli-Dharwad Municipal corporation\n 1.Admin Dept\n")
    print("Dept 1: -------------------File Created with name :", file.name,"\n")
    file.close()

create_file()

def read_file():

    path = r'c:\New\\'
    file = open(path + 'new.txt', "r")
    content = file.read()
    print("File has the below content---------------\n\n",content)
    print()
    file.close()

read_file()

def append():
    path = r'c:\New\\'
    file = open(path + 'new.txt', "a")
    print()
    file.write(" 2.Finance Dept")
    file.close()

append()

"""
w = new file creating
r = read the existing file
a = add the content into existing file
"""



