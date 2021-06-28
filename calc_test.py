# Import unittest and pytest as these are your dependencies to create
# our tests
import unittest
import pytest
from simple_calc import SimpleCalc


class Calctest(unittest.TestCase):
    calc = SimpleCalc()

    # assertions to write our test cases
    # we will use our basic calc example to write the tests first then the code

    def test_add(self):
        # Naming conventions is essential to have test in the name of our method
        self.assertEqual(self.calc.add(3, 2), 5)  # if True test will pass
        # return num1 + num2

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
