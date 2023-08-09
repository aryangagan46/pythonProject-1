"""******* PRACTISE PROGRAM ***********"""

'Find the flow of water(TMC) in Dam'


name = 'XYZ DAM'
number_of_Gates_in_dam = 5
Flow_data = [100000, 200000, 150000, 250000, 120000]

print('*************************************')
print("Name of the Dam is: {}" .format(name))
print('*************************************')
print()
print("Total Number of Gates in Dam is : {}" .format(len(Flow_data)))
print('*************************************')

Gates = 5
print()


for index, Gates in enumerate(Flow_data):

    X = int(input("Enter the Water in TMC:---> "))
    print("Flow of water in gate", index, 'is:', Gates)

    if X >= (max(Flow_data)):
        print()
        print('*************************************')
        print("Result: Mentioned Water Data is Maximum, So Water flows in Gate "
              "-------->", Flow_data.index(max(Flow_data)))
    else:
        print()
        print('*************************************')
        print('Result: Mentioned Water Data is Less, so WATER flows in GATE '
              '-------->', Flow_data.index(min(Flow_data)))
    break

print('***************Report End****************')

try:

    even_numbers = [2, 4, 6, 8]
    print(even_numbers[2])

    result = even_numbers[2]/0

except ZeroDivisionError:
    print("Denominator cannot be 0. ")

except IndexError:
    print("Index out of Bound.")

finally:
    print(even_numbers)
    print("program ran successfully" )
