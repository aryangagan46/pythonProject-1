"""
case1. even_numbers[5] - gives index error
case2. even_numbers[3] - 8/0 zero division error
"""

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
