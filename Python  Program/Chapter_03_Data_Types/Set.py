student_id = {122,114,116,118,115}
print('Student ID:', student_id)
print()

#CREATE A SET OF STRING TYPE
vowel_letters = {'a','e','i','o','u'}
print('Vowel Letters:', vowel_letters)
print()

#create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)
print()

'''Creating an empty set is a bit tricky. Empty curly braces {} 
will make an empty dictionary in python'''

print()

empty_dict = {}
print(type(empty_dict))

print()
#create an empty set
empty_set = set()
print(type(empty_set))
print()

'''
No Duplicate in set and dictionary - list and tuple allows duplicates
'''

print()
numbers = {2,4,6,6,2,8}
print(numbers)
