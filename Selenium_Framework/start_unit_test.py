#
# import unittest
#
# def run1():
#
#     print ("starting main")
#     loader = unittest.TestLoader()
#
#     script_pattern = 'test_*.py'
#     tests = loader.discover(r'C:\Users\Demo1\test_yatra',pattern=script_pattern)
#
#     print("tests",tests)
#
#     runner = unittest.TextTestRunner(verbosity=2)
#     result = runner.run(tests)
#
#     print("result------------.......", result)
#
#     run = result.testsRun
#     failures = len(result.failures)
#     successfully_run = run - failures
#     print("successfull",successfully_run)
#
# run1()

# importing "array" for array creations
import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])
print(type(a))
for i in a:
    print(i, end=" ")