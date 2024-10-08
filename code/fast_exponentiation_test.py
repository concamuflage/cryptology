import unittest
from fast_exponentiation import fast_exponentiation

class MyTestClass(unittest.TestCase):
    """for testing fast_exponentiation function"""

    def test1(self):
        self.assertEqual(fast_exponentiation(2,100),1267650600228229401496703205376)
        self.assertEqual(fast_exponentiation(7,9),40353607)
        self.assertEqual(fast_exponentiation(2, 2), 4)
        self.assertEqual(fast_exponentiation(2, 3), 8)
        self.assertEqual(fast_exponentiation(3, 2), 9)
        self.assertEqual(fast_exponentiation(3, 5), 243)
        self.assertEqual(fast_exponentiation(0, 0), 1)

