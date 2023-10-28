import unittest
from calculator import Calculator

class TestCalculatorMethods(unittest.TestCase):
    def setUp(self):
        """Setup the Calculator object that can be used in the tests."""
        self.calc = Calculator()

if __name__ == "__main__":
    unittest.main()