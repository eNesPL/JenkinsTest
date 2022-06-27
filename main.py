import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((2, 2, 2)), 6, "Should be 6")

    def test_fibo(self):
        from functions import fibo
        self.assertEqual(fibo(0), 0, "Should be 0")
        self.assertEqual(fibo(1), 1, "Should be 1")
        self.assertEqual(fibo(2), 1, "Should be 1")
        self.assertEqual(fibo(3), 2, "Should be 2")
        self.assertEqual(fibo(4), 3, "Should be 3")
        self.assertEqual(fibo(5), 5, "Should be 5")
        self.assertEqual(fibo(6), 8, "Should be 8")
        self.assertEqual(fibo(7), 13, "Should be 13")
        self.assertEqual(fibo(8), 21, "Should be 21")
if __name__ == '__main__':
    unittest.main()