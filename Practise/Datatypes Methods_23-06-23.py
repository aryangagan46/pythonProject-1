"""INPUTS"""

Name = "ajay, rajesh, Chetan"
String = ["Darshan", "Raju", "Arbaz", "Prajwal"]
X = "My name is Darshan"
my_list = [1, 2, 3, 4, 7, 7, 5]

print('************************************************************')
print('LIST DATATYPES METHODS')
print()

print('Accessing Element:')
print(my_list[0])
print()

print('clear')
my_list1 = [1, 2, 3, 4, 5]
my_list1.clear()
print(my_list1)
print()

print('Slicing:')
print(my_list[1:4])
print()

print('Modifying Element:')
my_list[2] = 10
print(my_list)
print()

print('LIST METHODS:')

print('Append:')
my_list.append(6)
print(my_list)
print()

print('Extend:')
another_list = [7, 8, 9]
my_list.extend(another_list)
print(my_list)
print()

print('Insert:')
my_list.insert(2, 20)
print(my_list)
print()

print('Remove:')
my_list.remove(4)
print(my_list)
print()

print('Pop:')
popped_element = my_list.pop(3)
print(popped_element)
print()

print('Index:')
index = my_list.index(5)
print(index)
print()

print('Count:')
count = my_list.count(7)
print(count)
print()

print('Integer Sort:')
my_list.sort()
print(my_list)
print()

print('String Sort:')
String.sort()
print(String)
print()

print('Integer Reversal:')
my_list.reverse()
print(my_list)
print()

print('String Reversal:')
String.reverse()
print(String)
print()

print('List Comprehension:')
squares = [x ** 2 for x in my_list]
print(squares)
print()

'apply a particular function passed in its argument to all of the list'
'elements stores the intermediate result and only returns the final summation value'

print('reduce')

from functools import reduce

# Example 1: Find the product of all numbers in a list
numbers = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# Example 2: Concatenate strings in a list
words = ["Hello", " ", "world", "!"]
sentence = reduce(lambda x, y: x + y, words)
print(sentence)

# Example 3: Find the maximum number in a list
numbers = [10, 5, 7, 14, 2]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)
print()

# Sums up the numbers in the list
print('sum')
my_list = [1, 2, 3, 4, 5]
result = sum(my_list)
print(result)
print()

print('Ord')
'Returns an integer representing the Unicode code '
'point of the given Unicode character'

my_list = ['a', 'b', 'c']
result = []
for char in my_list:
    result.append(ord(char))
print(result)
print()

print('cumulative')
'Apply a particular function passed in its argument to all of the'
'list elements returns a list containing the intermediate results'

import itertools

my_list = [1, 2, 3, 4, 5]
cumulative_sum = list(itertools.accumulate(my_list))
print(cumulative_sum)
print()

print('Filter')
'tests if each element of a list is true or not'


def is_even(n):
    return n % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(is_even, numbers))
print(filtered_numbers)
print()

print('MAP')
'returns a list of the results after'
'applying the given function to each item of a given iterable'

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)
print()

print('LAMBDA')
'lambda function can have any number of arguments but only '
'one expression, which is evaluated and returned.'

my_list = [1, 2, 3, 4, 5]
new_list = list(map(lambda x: x * 2, my_list))
print(new_list)
print()

print('************************************************************')

print()
print('STRINGS DATATYPES METHODS:')
print()
# Converts the first character of a string to uppercase and the rest to lowercase.

print('First letter Upper : ---Capitalize:')
FLC = Name.capitalize()
print(FLC)

# Converts the first character of a string to lowercase and the rest to uppercase.

print('First letter Lowercase:----lower:')
FLL = Name.lower()
print(FLL)

'''Converts the All character of a string to uppercase.'''

print('All letter Uppercase:')
ALU = Name.upper()
print(ALU)

# Converts the all character of a string to lowercase.

print('All letter lowercase:')
ALL = Name.lower()
print(ALL)

# Splits a string into a list of substrings based on a specified separator.
print('Split:')
Split = X.split()
print(Split)

# Strip Removes leading and trailing whitespace from a string.
print('strip:')
text = "   Hello, World!   "
clean_text = text.strip()
print(clean_text)

# Replaces occurrences of a specified substring with another substring.
print('replace:')
text = "Hello, World!"
new_text = text.replace("World", "Python")
print(new_text)

print('************************************************************')

print()
print('Tuples are immutable, meaning their elements cannot \n'
      'be--modified once created.Therefore, there are no \n'
      'built-in methods specific to tuples for modifying their contents')
print()

print('************************************************************')

print()
print('DICTIONARY DATATYPE METHODS:')
print()

print('Keys: Returns a list of all keys in the dictionary.:')
my_dict = {"apple": 5, "banana": 3, "orange": 2}
keys = my_dict.keys()
print(keys)
print()

print('Values: Returns a list of all values in the dictionary.:')
my_dict = {"apple": 5, "banana": 3, "orange": 2}
values = my_dict.values()
print(values)
print()

print('items(): Returns a list of all key-value pairs in the dictionary.:')
my_dict = {"apple": 5, "banana": 3, "orange": 2}
items = my_dict.items()
print(items)
print()

print('get(): Returns the value associated with a specified key.:')
my_dict = {"apple": 5, "banana": 3, "orange": 2}
value = my_dict.get("banana")
print(value)
print()

print('pop(): Removes and returns the value associated with a specified key.:')
my_dict = {"apple": 5, "banana": 3, "orange": 2}
value = my_dict.pop("banana")
print(value)
print(my_dict)
print()

print('update(): Updates the dictionary with key-value pairs from another dictionary.:')
my_dict = {"apple": 5, "banana": 3}
new_items = {"orange": 2, "grape": 4}
my_dict.update(new_items)
print(my_dict)
print()

print('************************************************************')

print()
print('SETS DATATYPE METHODS:')
print()

print()
print('add(): Adds an element to the set.:')
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
print()

print('remove(): Removes a specified element from the set.:')
my_set = {1, 2, 3, 4}
my_set.remove(2)
print(my_set)
print()

print('union(): Returns a new set containing all unique elements from two or more sets.:')
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

result_set = set1.union(set2, set3)
print(result_set)
print()

print('intersection(): Returns a new set containing common elements '
      'between two or more sets.:')

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 5, 6, 7}

result = set1.intersection(set2, set3)
print(result)
print()

print('difference(): Returns a new set containing elements present '
      'in the current set but not in another set.:')

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

diff_set = set1.difference(set2)
print(diff_set)
print()

print('************************************************************')

print()
print('FOR LOOP METHODS:')
print()

print('Traditional Construction:')
print()
print('Brick and Mortar:')
data = [1, 2, 3, 'hello', True]
for item in data:
    print(type(item))

print('Timber Frame Construction:')
print()
print('Constructing buildings using wooden frames:')
data = ['apple', 3.14, True, [1, 2, 3]]
for item in data:
    print(type(item))

print('Steel Frame Construction:')
print()
print('Building structures using steel frames:')
data = {'name': 'John', 'age': 25, 'is_student': True}
for key, value in data.items():
    print(key, type(value))

print('Prefabricated Construction:')
print()
print('Assembling buildings using pre-made components:')
data = ('apple', 3.14, 10, False)
for item in data:
    print(type(item))

print('Sustainable Construction:')
print()
print('Environmentally-friendly building methods:')
data = {1, 2, 3, 4, 5}
for item in data:
    print(type(item))

print('************************************************************')
