import logging

"""to print DEBUG logger message we need to set the basicConfig otherwise by default it prints
only warning messages"""

logging.basicConfig(level=logging.DEBUG)

def add(x,y):
    return x+y

def substratc(x,y):
    return x-y

add_result = add(2,2)
print("Addition Result:" ,add_result)

logging.debug("Addition result:")
logging.warning("Addition result:{}".format(add_result))

substratc_result = substratc(2,2)
print("Substraction result:",substratc_result)

logging.warning("Substraction result:{}".format(substratc_result))
