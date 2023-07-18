#***********************************************************
# x = [i for i in range(5)]
# print(x)

# x = [for i in range(5)]
#

#***********************************************************
# a = lambda x, y : x*y
# print(a(7, 19))

#***********************************************************
# def square(num):
#     # return num*num
#     print(num*num)
#
# a = 20
# square(a)

#***********************************************************

# a = 5
# b = 7
#
# result  = a%b
# print(result)
#***********************************************************
"""find the maximum Age for 3 inputs"""

# a = input("Enter the 1st Age for:", )
# b = input("Enter the 2nd Age for:", )
# c = input("Enter the 3rd Age for:", )
#
# max = c
# if max < a :
#     max = a
# if max < b :
#     max = b
# print("Maximum age is :", max)

#***********************************************************
"""swap two numbers using third variable"""
# a = 100
# b = 200
# k = a
# a = b
# b = k
#
# print("Value of a is :", a)
# print("value of b is :", b)
#***********************************************************
"""Convert Celsius to Faranite"""

# Celsius = float(input("Enter the value of Celsius:" ))
#
# Farahnite = (Celsius * 1.8) +32
#
# print("Celsius to Farahnite conversion is :", Farahnite)
#***********************************************************
"""Write a program that will give you the sum of 3 digits"""

num = int(input("Enter the three digit number:" ))

a = num % 10

num = num // 10
b = num % 10

c = num // 10

sum = (a + b + c)

print(sum)

#***********************************************************
#
def find_even_num(num1):
    Even_num = []


    for num2 in num1:
        if num2 % 2 == 0:
            Even_num.append(num2)
    return Even_num

num1 = [1,2,3,4,5,6,7,8,9]

Even_numbers = find_even_num(num1)
print("Even numbers are:", Even_numbers)
'***********************************************'

def find_even_numbers(numbers_list):
    even_numbers = []
    for num in numbers_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = find_even_numbers(numbers)
print("Even numbers:", even_numbers)