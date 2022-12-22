import unittest
from Calculator import cal
class Unit_tests(unittest.TestCase):
    def test_1(self):
        res = cal([1,'+',8])
        self.assertEqual(res,9)
    def test_2(self):
        res = cal([10,'*',8])
        self.assertEqual(res,80)
    def test_3(self):
        res = cal([1,'/',8])
        self.assertEqual(res,0.125)
        res = cal([40, '/', 8])
        self.assertEqual(res, 40/8)
        res = cal([4, '/', 2])
        self.assertEqual(res, 2)

    def test_4(self):
        res = cal([1, '+', 8, '-', 4])
        self.assertEqual(res, 1+8-4)
        res = cal([1, '+', 3, '+', 4])
        self.assertEqual(res, 1+3+4)
        res = cal([1, '+', 8, '-', 40])
        self.assertEqual(res, 1 + 8 - 40)
        res = cal([1, '+', 81, '-', 4])
        self.assertEqual(res, 1 + 81 - 4)