# moulinette.py

import unittest
from calculator import calculator

test = unittest.TestCase()
calculator2 = calculator()
sum = calculator2.addition(1, 1)
test.assertEqual(sum, 2)

class moulinette(unittest.TestCase):

    def setUp(self):
        self.calculator = calculator()

    def test_add_positive(self):
        sum = self.calculator.addition(5, 3)
        self.assertEqual(sum, 8)

    def test_add_negative(self):
        sum = self.calculator.addition(-5, -3)
        self.assertEqual(sum, -8)

    def test_sub_positive(self):
        sum = self.calculator.subtraction(10, 4)
        self.assertEqual(sum, 6)

    def test_subt_negative(self):
        sum = self.calculator.subtraction(4, 10)
        self.assertEqual(sum, -6)

    def test_mult_standard(self):
        sum = self.calculator.multiplicate(7, 2)
        self.assertEqual(sum, 14)

    def test_mult_zero(self):
        sum = self.calculator.multiplicate(99, 0)
        self.assertEqual(sum, 0)

    def test_div_standard(self):
        sum = self.calculator.divide(10, 2)
        self.assertEqual(sum, 5.0)

    def test_div_one(self):
        sum = self.calculator.divide(7, 1)
        self.assertEqual(sum, 7.0)

    def test_div_zero(self):
        # check error
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

# run the test
if __name__ == '__main__':
    unittest.main()

