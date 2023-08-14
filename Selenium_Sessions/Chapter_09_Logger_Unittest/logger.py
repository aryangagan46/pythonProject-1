import logging
def add(x,y):
    return x+y

def substratc(x,y):
    return x-y

add_result = add(2,2)
print("Addition Result:" ,add_result)

logging.warning("Addition result:{}".format(add_result))

substratc_result = substratc(2,2)
print("Substraction result:",substratc_result)

logging.warning("Substraction result:{}".format(substratc_result))
