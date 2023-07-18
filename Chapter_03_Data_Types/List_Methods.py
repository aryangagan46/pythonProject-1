#******************List Methods*************

'Input'
print()
roll_Number = [20, 50, 21, 10, 45, 23]
print('Input is : {}' .format(roll_Number))
print()


'(1.) Sort'

roll_Number.sort()
print("1. Roll Numbers in Sort format : {}".format(roll_Number))
print()
#Output : 1. Roll Numbers in Sort format : [10, 20, 21, 23, 45, 50]

#****************************

'(2.) Reverse'

roll_Number.reverse()
print("2. Roll Numbers in Reverse format : {}" .format(roll_Number))
print()
#Output : 2. Roll Numbers in Reverse format : [50, 45, 23, 21, 20, 10]

#****************************

'(3.) Maximum Value'

print("3. Maximum Number in Roll Number is : {}" .format(max(roll_Number)))
print()
#Output : 3. Maximum Number in Roll Number is : 50

#****************************

'(4.) Minimum Value'

print("4. Minimum Number in Roll Number is : {} ".format(min(roll_Number)))
print()
#Output : 4. Minimum Number in Roll Number is : 10

#****************************

'(5.) Pop '

roll_Number.pop()
print("5. Exploring POP Method : {}" .format(roll_Number))
print()
#Output : Exploring POP Method : [50, 45, 23, 21, 20]

roll_Number.pop(3)
print("6. Exploring POP Method with 3rd Index: {}" .format(roll_Number))
print()
#Output : Exploring POP Method with 3rd Index: [50, 45, 23, 20]

#*****************************