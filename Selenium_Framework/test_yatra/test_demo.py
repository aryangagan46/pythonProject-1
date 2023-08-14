import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print("start the test  suite")
        super(TestStringMethods, self).setUp()


    def test1_upper111(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test1_isupper222(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test2_split333(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def tearDown(self):
        print("all tests done")
        pass