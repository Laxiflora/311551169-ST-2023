import unittest
from math import sqrt, exp
from calculator import Calculator

para = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]


class ApplicationTest(unittest.TestCase):

    def test_add(self):
        for i, j in para:
            self.assertEqual(Calculator.add(i, j), i+j)
        with self.assertRaises(TypeError):
            Calculator.add(1, "2")


    def test_divide(self):
        for i, j in para:
            self.assertEqual(Calculator.divide(i, j), i/j)
        with self.assertRaises(TypeError):
            Calculator.divide(1, "2")

    def test_sqrt(self):
        for i, j in para:
            self.assertEqual(Calculator.sqrt(i), sqrt(i))
        with self.assertRaises(TypeError):
            Calculator.sqrt(1, "2")

    def test_exp(self):
        for i, j in para:
            self.assertEqual(Calculator.exp(i), exp(i))
        with self.assertRaises(TypeError):
            Calculator.exp(1, "2")


if __name__ == '__main__':
    unittest.main()
