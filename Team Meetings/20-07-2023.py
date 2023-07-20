
print("Write a Program using different operators")

def add_numbers():

    a = 2
    b = 6

    c = a + b
    c1 = a - b
    c2 = a * b
    c3 = a / b
    c4 = a > b
    c5 = a < b
    c6 = float(a % b)
    c7 = float(a // b)
    c8 = a ** b


    print("{}\n{}".format(c6,c7))
#
# add_numbers()

# # print("Write a Program to add numbers with RETURN Statement")

def add_two_numbers(*abc):

    data = abc

    sum = 0

    for a in data:
        sum = sum + a
    return sum

result = add_two_numbers(3,4,5,6,7,8,9,0,5,4,3,3,2,4,5,6,7,7)

print(result)