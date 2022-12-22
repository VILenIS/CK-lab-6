import unittest
from file_reader import *
class Unit_tests(unittest.TestCase):
    def test_1(self):
        res = cal([1,'+',8])
        self.assertEqual(9,9)
    def test_2(self):
        res = cal([10,'*',8])
        self.assertEqual(80,80)
    def test_3(self):
        res = cal([1,'/',8])
        self.assertEqual(0.125,0.125)

    def test_4(self):
        res = cal([1, '+', 8, '-', 4])
        self.assertEqual(1+8-4, 1+8-4)