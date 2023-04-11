#################
#    Imports    #
#################

import unittest
from fibonacci import fibonacci

#################
#   Testing     #
#################

class Test_W_Count(unittest.TestCase):
    
    def test_0(self):
        self.assertEqual(0, fibonacci(0))

    def test_0(self):
        self.assertEqual(1, fibonacci(1))

    def test_0(self):
        self.assertEqual(1, fibonacci(2))

    def test_0(self):
        self.assertEqual(2, fibonacci(3))

    def test_0(self):
        self.assertEqual(3, fibonacci(4))

    def test_0(self):
        self.assertEqual(5, fibonacci(5))

    def test_0(self):
        self.assertEqual(8, fibonacci(6))

    def test_0(self):
        self.assertEqual(13, fibonacci(7))

    def test_0(self):
        self.assertEqual(21, fibonacci(8))

    def test_0(self):
        self.assertEqual(34, fibonacci(9))

    def test_0(self):
        self.assertEqual(55, fibonacci(10))

    def test_0(self):
        self.assertEqual(89, fibonacci(11))

    def test_0(self):
        self.assertEqual(144, fibonacci(12))

    def test_0(self):
        self.assertEqual(233, fibonacci(13))

    def test_0(self):
        self.assertEqual(377, fibonacci(14))

    def test_0(self):
        self.assertEqual(610, fibonacci(15))

    def test_0(self):
        self.assertEqual(987, fibonacci(16))

if __name__ == '__main__':
    unittest.main()