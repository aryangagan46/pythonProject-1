"""******* PRACTISE PROGRAM ***********"""

'Find the flow of water(TMC) in Dam'


name = 'XYZ DAM'
number_of_Gates_in_dam = 5
Flow_data = [100000, 200000, 150000, 250000, 120000]


print('*************************************')
print("Name of the Dam is: {}" .format(name))
print('*************************************')
print("Total Number of Gates in Dam is : {}" .format(len(Flow_data)))
print('*************************************')

Gates = 5

for index, Gates in enumerate(Flow_data):
    print("Flow of water in gate", index, 'is:', Gates)

if 300000 >= (max(Flow_data)):
    print('*************************************')
    print("Result: Mentioned Water Data is Maximum, So Water flows in Gate "
          "-------->", Flow_data.index(max(Flow_data)))
else:
    print('*************************************')
    print('Result: Mentioned Water Data is Less, so WATER flows in GATE '
          '-------->', Flow_data.index(min(Flow_data)))

print('***************Report End****************')
