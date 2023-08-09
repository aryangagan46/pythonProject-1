#pgm to calculate the sum of numbers - here
#hence we are using while
#until the user enters zero

total = 0

number = int(input('Enter a Number: '))

#add numbers until number is zero
while number != 0:
    total += number     # total = total + number

    # take integer input again
    number = int(input('Enter a number: '))

print('total =', total)

"""
examples of list of students
for - 100 students
while - not sure of the students number

similarly for number of files to read
"""

#sum of two numbers
total = 0
for i in range(0,2):
    number = int(input('enter a number: '))
    total += number
print("total of two numbers", total)
