import unittest
from calculation import add, subtract, multiply, divide


class TestCalculation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 26), 31)
        self.assertEqual(add(-5, 5), 0)

    def test_subtract(self):
        self.assertEqual(subtract(7, 5), 2)
        self.assertEqual(subtract(-9, 6), -15)

    def test_multiply(self):
        self.assertEqual(multiply(5, 5), 25)
        self.assertEqual(multiply(-4, 2), -8)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises(ZeroDivisionError, divide, 11, 0)


if __name__ == '__main__':
    unittest.main()