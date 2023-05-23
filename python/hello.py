#!/usr/bin/env python3
import unittest
def hello_world():
    #return ('hello world')
    pass
def calculate(a,b):
    pass
    #return a+b

#tests
class myTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')
    def test_another(self):
        self.assertEqual(calculate(5,7), 12)

if __name__ == '__main__':
    unittest.main()
