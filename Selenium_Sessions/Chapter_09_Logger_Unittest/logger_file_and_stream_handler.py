import logging

""""
creating 

file handler - writes to disk file
stream handler - writes to terminal

"""

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s, %(message)s') #used for both output stream and file

streamHandler = logging.StreamHandler() #creating ooutput stream foromat to terminal
streamHandler.setFormatter(formatter)

file_handler = logging.FileHandler('test3.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler) #creating output stream from to disk file
logger.addHandler(streamHandler)

def add(x,y):
    return x+y

num1 = 3
num2 = 2
add_result = add(num1,num2)

logger.debug("Addition result of num1: {} and num2: {} is = {}".format(num1,num2,add_result))
