try:

    "Input"
    even_numbers = [2, 4, 6, 8]

    """print the index value"""
    print(even_numbers[2])

    "change the denominator value"
    result = even_numbers[2] / 0

except ZeroDivisionError:
    print("Denominator cannot be 0. ")

except IndexError:
    print("Index out of Bound.")

finally:
    print()
    try:
        result = even_numbers[3] / 0
    except:
        print("print except if try condition fails")
    print()
    print(even_numbers)
    print()
    print("program ran successfullyyyyyyyyy")


try

    "input"
    Vehicals = "Bike : 20","Car : 10", "Bus : 5", "SUV : 2"

