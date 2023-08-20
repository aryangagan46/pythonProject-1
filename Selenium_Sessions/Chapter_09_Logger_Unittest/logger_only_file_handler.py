import logging

"""
creating only file handler and writes to only file
"""

logger = logging.getLogger()  #------->logger 1st step

logger.setLevel(logging.DEBUG) #------->2nd Step

formatter = logging.Formatter('%(levelname)s:%(name)s %(message)s')

file_handler = logging.FileHandler('test2.log') #3.a

file_handler.setLevel(logging.DEBUG) #3.b
file_handler.setFormatter(formatter) #3.c

logger.addHandler(file_handler) ########>> 3rd step

def add(x,y):
    return x+y

num1 = 3
num2 = 2
add_result = add(num1,num2)

logger.debug("Addition result of num1 {} and num2 {} is = {}".format(num1,num2,add_result))


"""

Logger

1). Get Logger
2). Set Logger
3). Add File Handler

    Create a File
            File --- Set level
                 --- SetFormatter

"""