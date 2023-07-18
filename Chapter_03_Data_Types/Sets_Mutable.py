"""
SETS - not ordered
CANNOT BE CHANGED BUT CAN BE EDITED...
We cannot access or change an element(like in case of list..)
we can access by using indexing and assign new value ..)
of a set using indexing or slicing. Set data type does not support it
"""


numbers = {10,20,30,40}

#print(numbers[0])  #NOT ALLOWED - indexing and slicing
#numbers[1] = 23    # assignment not allowed
#for num in numbers: #iteration not allowed as it unordered
#print (num)

print('Initial Set:', numbers)

#using add() method
numbers.add(50)

print('Updated Set:', numbers)

fruits = {'mango', 'grapes'}
veggies = ['beans', 'carrot', 'eggplant']
fruits.update(veggies)
print(fruits)

#Output: {'carrot','eggplant','grapes','mango',beans')

languages = {'c', 'java', 'python'}
print('Initial Set:', languages)

#remove 'java from a set
removedvalue = languages.discard('java')
print("set after remove():", languages)


#First Set
A = {1,3,5,7,9}

#Second set
B = {2,4,6,8,10}

#Perform union operation using |
print('Union using |:', A | B)

#Peform union operation using union()
print('Union using union():', A.union(B))

#Set
A1 = {1, 3, 5, 7, 8}
B1 = {0, 2, 4, 6, 8}

print('Intersection using &:', (A1 & B1))
print('Intersection using &:', A1.intersection(B1))
print('Difference Using - :', A1-B1)
print('Difference using &:', A1.difference(B1))