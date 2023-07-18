print('********Practice on Dictionary Data types********')

'''Input'''
print()

dict1 = {'AVATAR Budget:': 4000, 'KGF Budget:': 2000, 'KANTARA Budget:': 1000}
print('Input is:', dict1)

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

print('***********Practice on list Data types**********')

'''Input'''
Rice = [50, 55, 60, 65, 70, 75, 80]
print('Different Rice prices in Market:', Rice)
print()

print('Print 2nd index element:')
print(Rice[2])

print('Print 0 to 3rd index element:')
print(Rice[0:3])

print('update 3rd index with 20:')
Rice[3] = 20
print(Rice)

print('delete 3rd index element from list:')
del Rice[3]
print(Rice)

print()
print('Nested List')

Wheat = [60, 48], [97, 30, 78, 94]

for price in Wheat:
    for High in price:
        print("\t", High)

print()

Fruits = ['Mango'], ['Apple'], ['34'], ['57']

for Items in Fruits:
    for Mix in Items:
        print('\t \t', Mix)

print()

Connection = ({'apple'}, ['ball'], {'cat'}, ['dog'])

for Things in Connection:
    for AnimalThings in Things:
        print(AnimalThings[0], AnimalThings[1], AnimalThings[2])

print()

print('**************************************')

'Input'
print()
roll_Number = [20, 50, 21, 10, 45, 23]
print('Input is : {}' .format(roll_Number))
print()


'(1.) Sort'

roll_Number.sort()
print("1. Roll Numbers in Sort format : {}".format(roll_Number))
print()

'(2.) Reverse'

roll_Number.reverse()
print("2. Roll Numbers in Reverse format : {}" .format(roll_Number))
print()


'(3.) Maximum Value'

print("3. Maximum Number in Roll Number is : {}" .format(max(roll_Number)))
print()


'(4.) Minimum Value'

print("4. Minimum Number in Roll Number is : {} ".format(min(roll_Number)))
print()


'(5.) Pop '

roll_Number.pop()
print("5. Exploring POP Method : {}" .format(roll_Number))
print()


roll_Number.pop(3)
print("6. Exploring POP Method with 3rd Index: {}" .format(roll_Number))
print()

print('**************************************')


'''Input'''
Bus_Number = [238, 401, 61, 241, 176, 252, 63, 75]
print('Input is:', Bus_Number)

print()
print('Length:  ')
print(len(Bus_Number))

print()
print("Iteration: ")
for Bus_Route in Bus_Number:
    print(Bus_Route)

print()
print('Membership: ')
if 238 in Bus_Number:
    print("Route to Majestic")
else:
    print(" Bus route changed")
print()

print("concatination:")
'''Input'''
Metro_Route = ["Purple", "Green", "Pink", "Yellow"]

Routes = Bus_Number+Metro_Route
print(Routes)
print()

print("Append: 333")
Bus_Number.append(333)
print(Bus_Number)
print()

print("Extend: Blue, 213 ")
Bus_Number.extend([213, 'darshan'])
print(Bus_Number)

print()
print("Insert : Airport")
Bus_Number.insert(0, 'Airport')
print(Bus_Number)
print()
