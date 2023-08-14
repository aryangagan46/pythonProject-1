
import unittest

def run1():

    print ("starting main")
    loader = unittest.TestLoader()

    script_pattern = 'test_*.py'
    tests = loader.discover(r'C:\Users\Demo1\test_yatra',pattern=script_pattern)

    print("tests",tests)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(tests)

    print("result------------.......", result)

    run = result.testsRun
    failures = len(result.failures)
    successfully_run = run - failures
    print("successfull",successfully_run)

run1()

