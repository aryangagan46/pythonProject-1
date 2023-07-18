#**********Example-1************

print('Print String:')
school = 'INDIAN PUBLIC SCHOOL INDIRANAGAR'
print(school)

print('Type of variables:')
print(type(school))

print('Type of variables:')
age = 23
print(type(age))

print('Accessing string or indexing:')
print(school[0:7])

print('Update/concatenate string:')
print(school + '-------Bangalore'+ 'PIN CODE = 560070')

print('Check the function is in string or integer')
print(school.isdigit())           # Check the function it is string or interger

print('Check the count inside the condition')
print(school.count('A'))          # Count the string inside the condition

print('Insert / update the Index element')
school.insert(3, "Dharwad")         #"Insert" used to update the data in any index using index number


print('Append or update the element value at last index')
school.append("Darshan")            # "append" used for update the value at end.
print(school)




# list = [87,76,4,8,6,7,4,2,34,]  # Input
# list.sort()                     # Condition - it arrange the numbers in Ascending order.
# print(list)