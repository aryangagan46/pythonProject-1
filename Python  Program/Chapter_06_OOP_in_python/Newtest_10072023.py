

class Calculator():
    def __init__(self):
        print()
        print("First method to execute:") # init method is the first method to execute upon creating object
        self.a = 5  # we can initialize variables inside class itself
        self.b = 5  # or we can get it from some other files or we can get it while creating objects

    def add_2_numbers(self):
        """
        this method is to add two numbers
        :return:
        """
        print()
        print("This is method to add 2 numbers")
        c = self.a + self.b
        print(c)

    def substraction_of_two_numbers(self):
        """
        this method is to substract two numbers
        :return:
        """
        print()
        print("this is method to substract 2 numbers")
        c = self.a - self.b
        print(c)

    def multiplication_of_two_numbers(self):
        """
        this method is to multiply two numbers
        :return:
        """

        print()
        print("this is method to multiply 2 numbers")
        c = self.a * self.b
        print(c)

obj1 = Calculator()
obj1.add_2_numbers()
obj1.substraction_of_two_numbers()
obj1.multiplication_of_two_numbers()


