"""Write a program to define method using Different type of Data Types and Operators"""
def method_using_string_data_types():
    """Input"""
    print()
    print('''*****"Defining String datatype Methods**********"''')
    print()
    print('1. Print String:')
    school = ["INDIAN PUBLIC SCHOOL INDIRANAGAR"]
    print(school)

    print()
    print('2. Type of variables:')
    print(type(school))

    print()
    print('3. Type of variables:')
    age = 23
    print(type(age))

    print()
    print('4. Accessing string or indexing:')
    print(school[0:7])

    print()
    print('5. Update/concatenate string:')
    print(school + ['-------Bangalore'] + ['PIN CODE = 560070'])

    print()
    print('6. Check the function is in string or integer')
    print(type(school))

    print()
    print('7. Check the count inside the condition')
    print(school.count('A'))

    print()
    print('8. Insert / update the Index element')
    school.insert(3, "Dharwad")
    print(school)
    print()

def method_using_list_data_types():

    print()
    print('''*****"Defining list datatype Methods*********"''')

    'Input'
    list1 = [10, 20, 30, 40, 50, 60]
    print()

    print("1. Update the 5th Index Element: ")
    subject = list1[5]
    print(subject)

    print()
    print("2. Slicing :")
    multiple_item = list1[3:5]
    print(multiple_item)

    print()
    print("3. print the 5th Index Element :")
    print(list1[5])

    print()
    print("4. delete 0th Index element :")
    del (list1[0])
    print(list1)

    print()
    print("5. Nested List :")
    collection = [1, 2, 3], [4, 5, 6], [7, 8, 9, 10]

    for name in collection:
        for num in name:
            print("\t", num)

    print()

    print("6. Nested list with mixed data types :")
    list_mixed = ['10-', 'darshan-', ['a', 'b', 'c']]

    for List1 in list_mixed:
        for Dashboard in List1:
            print('\t\t\t', Dashboard)

    print("7. Nested list with mixed data type with output for 1st index element :")
    Name = ({'Darshan'}, {'12'}, ['89.4'])

    for List2 in Name:
        for List3 in List2:
            print(List3[1])
    print()
def method_using_list_data_types_with_others():
    print()
    print('''********"Defining list datatype with others Methods*********"''')
    'Input'
    print()
    roll_Number = [20, 50, 21, 10, 45, 23]
    print('Input is : {}'.format(roll_Number))
    print()

    '(1.) Sort'

    roll_Number.sort()
    print("1. Roll Numbers in Sort format : {}".format(roll_Number))
    print()

    '(2.) Reverse'

    roll_Number.reverse()
    print("2. Roll Numbers in Reverse format : {}".format(roll_Number))
    print()

    '(3.) Maximum Value'

    print("3. Maximum Number in Roll Number is : {}".format(max(roll_Number)))
    print()

    '(4.) Minimum Value'

    print("4. Minimum Number in Roll Number is : {} ".format(min(roll_Number)))
    print()

    '(5.) Pop '

    roll_Number.pop()
    print("5. Exploring POP Method : {}".format(roll_Number))
    print()

    roll_Number.pop(3)
    print("6. Exploring POP Method with 3rd Index: {}".format(roll_Number))
    print()

    print()
    print("INPUT is :")
    list1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print(list1)

    print()
    print("1. Length of the list :")
    print(len(list1))

    print()
    print("2. Iteration :")
    for int in list1:
        print(int)

    print()
    print("3. Membership :")
    if 12 in list1:
        print("100 is present in the list")
    else:
        print("element is not present in the list")

    print()
    print("(4.) Concatenation")

    list2 = [20, 40, 60, 80, 100]
    print("Input for List2 is :", list2)
    list3 = list1 + list2
    print(list3)

    print()
    print("(5.) Append value 120:")
    list2.append(120)
    print(list2)

    print()
    print("(6.) Extend element [140,160,180]:")
    list2.extend([140, 160, 180])
    print(list2)

    print()
    print("(7.) Insert element 0 at 3rd index")
    list2.insert(3, 0)
    print(list2)
    print()


def method_using_dictionary_data_type():
    print()
    print('''********"Defining dictionary datatype Methods**********"''')
    '''Input'''
    print()
    dict1 = {'AVATAR Budget': 4000, 'KGF Budget': 2000, 'KANTARA Budget': 1000}
    print('Budget Input for Movies :', dict1)

    print()

    print("Print KEY & VALUE")
    for key, value in dict1.items():
        print("%s %s" % (key, value))
    print()
    print("PRINT KEY ONLY")
    for key1 in dict1.keys():
        print(key1)
    print()
    print("PRINT VALUE ONLY")
    for value1 in dict1.values():
        print(value1)
    print()

    print()
    print("Update the New Key-Value element KABZAA :")
    dict1['KABZAA'] = 1500
    print(dict1)
    print()


def methods_using_tuple_data_types():
    print()
    print('''*************"Defining tuple datatype Methods*************"''')
    "Input"
    print()
    list0 = [1, 0, 2, 4, 5, 7]
    print("Input for List0 is :", list0)
    list1 = [1, 0, 2, 4, 5, 7]
    print("Input for List1 is :", list1)
    tuple0 = (1, 3, 2, 4, 5)
    print("Input for tuple0 is :", tuple0)

    print()
    print('*** Accessing/indexing ***')
    print(list0[2])

    print()
    print('*** Slicing tup[1:3] ***')
    print(list0[1:3])

    print()
    print('*** iterate the tuple using for ***')
    for Nat in tuple0:
        print(Nat)

    print()
    print('*** membership ***')

    if 5 in list0:
        print("Element is present in list 0")
    else:
        print("Element is not present in list 0")

    print()
    print('*** Find Maximum and Minimum Element in list ***')
    print()
    print('*** Maximum number in list0 ***')
    print(max(list0))
    print()
    print('*** Minimum number in list0 ***')
    print(min(list0))

    print()
    print('**** Conversion from tuple to list and vice versa ****')
    print()

    tuple1 = tuple(list0)
    print(tuple1)
    print()
    list3 = list(tuple0)
    print(list3)

    print()
    print('**** Concatenate List to List ****')
    list5 = list0 + list1
    print(list5)
    print()


def method_using_set_data_types():
    print()
    print('''************"Defining set datatype Methods************"''')
    print()
    "Input"
    print("Creating a set for Integer element: ")
    bus_route_number = {122, 114, 116, 118, 115}
    print('BMTC Bus Route Number:', bus_route_number)
    print()

    print("creating a set for string element: ")
    metro_route = {'Blue', 'Purple', 'Yellow', 'Green', 'Red'}
    print('BMRCL Metro_Route :', metro_route)
    print()

    print("create a set for mixed elements: ")
    mixed_set = {'Hello', 101, -2, 'Bye'}
    print('Set of mixed data types:', mixed_set)
    print()

    print("create empty dictionary:")
    empty_dict = {}
    print(type(empty_dict))

    print()
    print("create an empty set: ")
    empty_set = set()
    print(type(empty_set))
    print()

    print("print integers except duplicate integer: ")
    numbers = {2, 4, 6, 6, 2, 8}
    print("Input is: {2, 4, 6, 6, 2, 8}")
    print(numbers)
    print()


def methods_using_set_mutable_data_types():
    print()
    print('''************"Defining set mutable datatype Methods************"''')
    print()
    print("add element in set data type")
    numbers1 = {10, 20, 30, 40, 'apple','cat'}
    print("Input is :", numbers1)
    numbers1.add(50)
    print(numbers1)

    print()
    print("add new set with existing set: ")
    place = {'Bengaluru', 'Hubli', 'kalaburgi'}
    region = {'South', 'Northwest', 'Northeast'}
    place.update(region)
    print(place)

    print()
    print("remove element from set: ")
    remove = place.discard('Bengaluru')
    print(remove)

    print()
    numbers2 = {'apple', 'bat', 'cat', 'dog', 10, 20}
    print("Input is :", numbers2)
    print()
    print("Perform union operation using | :")
    print("Union Using |: ", numbers1 | numbers2)

    print()
    print("Perform Intersection operation using & :")
    print("Union Using &:", numbers1 & numbers2)

    print()
    print("Perform Difference operation using - :")
    print("Union Using - :", numbers1 - numbers2)
    print()


    print("*************Arithmetic Operators***********************")
def arithmetic_operators():

    "Input"
    print()
    x = 2.5
    print("Input for x is :", x)
    y = 3
    print("Input for y is :", y)
    print("Input")
    print("O = ", x)
    print("P =", y)

    # ARITHMETIC OPERATIONS FUNCTIONS:

    print()
    print("Addition")
    print("O + P = ", x + y)

    print()
    print("Difference")
    print("O - P = ", x - y)

    print()
    print("Multiplication")
    print("O * P = ", x * y)

    print()
    print("Division")
    print("O / P =", x / y)

    print()
    print("Modulus")
    print("O % P", x % y)

    print()
    print("Exponential")
    print(("O ** P", x ** y))

    print()
    print("Reminder/Floor Division")
    print(("O // P", x // y))


    print()
    print(" ********Assignment Operators*********")
def assignment_operators():

    "Input"
    apple_per_kg = 50
    a = (apple_per_kg)
    print("apple_per_kg is (a):", a)
    ball_per_piece = 20
    b = (ball_per_piece)
    print("ball_per_piece is (b):", b)
    coke_per_liter = 35
    c = (coke_per_liter)
    print("coke_per_liter is (c):", c)
    # Increment or decrement operator

    print()
    print("Input is : a = {}, b = {}, c = {}".format(a, b, c))
    print()
    d = 10
    d = d + 1
    d += 1
    print(" Value of d is : {} ".format(d))
    print()
    print(' c = a + b :- ', a + b)
    print()
    c += 1
    c = c + 1


    c += 1
    print(' c += 1 , c = c + 1 :- ', c)
    c -= 1
    print()
    print(' c -= 1, c = c - 1 :-', c)
    print()
    print(' c *=a, c=c*a :-', c * a)
    print()
    print(' c/=a, c = c/a :-', c / a)
    print()
    print(' c%=a, c=c%a :-', c % a)
    print()
    print(' c**=a = c = c**a', c ** a)

    print()
    print("******Bitwise Operators*******")
def bitwise_operator():

    "Inputs"

    print()
    a = 5
    print('Input for a is [0 1 0 1] :- ', a)
    print()
    b = 4
    print('Input for b is [0 1 0 0] :-', b)

    # 0001 = 1 # bitwise representation
    # 0011 = 3
    # 0100 = 4
    print()

    print("Output for Operations:-")
    print('a & b :-', a & b)
    print()
    print('a | b :-', a | b)
    print()
    print('~a :-', ~a)
    print()
    print('a << 2 :-', a << 2)
    print()
    print('a >> 2 :-', a >> 2)
    print()
    print("*********Comparision Operators*********")
def comparision_operator():

    "Inputs"
    print()
    Girish = 1000
    print('Girish has a amount of Rupees: ', Girish)
    Rajesh = 500
    print('Rajesh has a amount of Rupees: ', Rajesh)

    print()
    print("Is Both Has same Amount:")
    print('Girish == Rajesh :', Girish == Rajesh)

    print()
    print("is both hase difference amount:")
    print('Girish != Rajesh :', Girish != Rajesh)

    print()
    print("is Girish has More amount compare to Rajesh:")
    print('Girish > Rajesh :', Girish > Rajesh)

    print()
    print("is girish has less amount compare to Rajesh:")
    print('Girish < Rajesh :', Girish < Rajesh)

    print()
    print("is Girish amount has Morethan or equal to Rajesh:")
    print('Girish >= Rajesh :', Girish >= Rajesh)

    print()
    print("is Girish amount has lessthan or equal to Rajesh:")
    print('Girish <= Rajesh :', Girish <= Rajesh)

    print()
    print("is Girish amount equal to Rajesh:")
    if (Girish == Rajesh):
        print(" Both has a sufficient amount")
    else:
        print("Only girish has a more amount compare to rajesh")

    print()

    print("********** Identity Operators *********")

def identity_operators():

    "Input"
    print()
    population_in_ameraica = 26062023
    america = (population_in_ameraica)
    print('Population in America as on FY23 is:', america)
    population_in_azerbaijan = 16062023
    azerbaijan = (population_in_azerbaijan)
    print('Population in Azerbaijan as on FY23 is:', azerbaijan)

    print()
    print('is population in "america" has same in "azerbaijan" ??? ')
    if america is azerbaijan:
        print("Yes Population is about to same")
    else:
        print("No there is difference about nearly :", azerbaijan-america)

    print()
    print(("Memory location id for America :"), id(america))
    print(("Memory location id for Azerbaijan :"),id(azerbaijan))

    print()
    america = 2024 + america
    america += 2024
    print("Existing with Updated Population around 2024 is: ", america)
    print()
    print("Memory location id for America is changed to New :",id(america))

    print()
    if america is azerbaijan:
        print("yes population is same in both countries")
    else:
        print("Population in America is not same as in Azerbaijan")
    print()

    print("********Logical Operator**********")


def logical_operator():

    "Input"
    print()
    a = True
    print('Input for a :', a)
    b = False
    print('Input for b :', b)

    print()
    print('AND')
    print('a and b :-', a and b)

    print()
    print('OR')
    print('a or b :-', a or b)

    print()
    print('NOT')
    print('not b :-', not b)

    print()
    a = 2
    print('Input for a :', a)
    b = 2
    print('Input for b :', b)
    c = 0
    print('Input for c :', c)

    print()
    print('Find result for AND function:')
    if a == b and c:
        print('a and b are equal and c has some vale in it--------')
    else:
        print('either a and b are not equal or c has no value------')

    print()
    print('Find result for OR function:')
    if a == b or c:
        print('a and b are equal and c has some vale in it--------')
    else:
        print('either a and b are not equal or c has no value------')

    print()
    c = False
    print('Find result for NOT function for input (c = False:)')
    if not c:
        print('c is False, not of c logical condition result is True, '
              'hence printing this statement')
    print()

    print(" ************membership Operators*************")

def membership_opperators():

    print()
    print("Is RBI letter is mentioned in STATE_BANK_OF_INDIA ??")
    if 'RBI' in 'STATE_BANK_OF_INDIA':
        print('Yes--- SBI is present in STATE_BANK_OF_INDIA')
    else:
        print('No---Mentioned Letter is not present in STATE_BANK_OF_INDIA')

    SBI_Bank = [10, 20, 30, 40, 50]

    print()
    Amount = 1000
    print(Amount, "Rupees:")
    print("Above Mentioned Amount is Present in SBI_Bank: ?")
    RBI = Amount in SBI_Bank
    print(RBI)

    print()
    print("Is Amount:2000 Rupee Note present in SBI_Bank using 'IN' Method:")
    if 2000 in SBI_Bank:
        print('Yes,---- 2000 Rupee Note is present in SBI_Bank')
    else:
        print("No,---- 2000 Rupee Note is NOT present in SBI_Bank")

    print()
    print("Is Amount:2000 Rupee Note present in SBI_Bank using 'NOT IN' Method:")
    if 2000 not in SBI_Bank:
        print('Yes,---- 2000 Rupee Note is NOT present in SBI_Bank')
    else:
        print('NO,---- 2000 Rupee Note is Present in the SBI_Bank')

    print()

    Movie_Name = ('KGF', 'KANTARA', 'KABZAA')
    print("Is Mentioned Movie is present in Movie Name Data ??")
    Movie = 'KGF'
    if Movie in Movie_Name:
        print('Yes--- Movie : KGF is present in Movie Name Data')
    else:
        print('No,--- Mentioned Movie Name is not present in Data')
    print()

'''Calling methods for different Datatypes and Operators'''

method_using_string_data_types()
method_using_list_data_types()
method_using_list_data_types_with_others()
method_using_dictionary_data_type()
methods_using_tuple_data_types()
method_using_set_data_types()
methods_using_set_mutable_data_types()
arithmetic_operators()
assignment_operators()
bitwise_operator()
comparision_operator()
identity_operators()
logical_operator()
membership_opperators()