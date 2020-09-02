import unittest
from exec_sum import Sum


class TestSum(unittest.TestCase):
    def test_Sum(self):
        a = 1
        b = 3
        expect = a + b
        actual = Sum(a, b)
        self.assertEqual(actual, expect)


if __name__ == "__main__":
    unittest.main()
