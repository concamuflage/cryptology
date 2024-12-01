from is_prime import is_prime
import unittest

class MyTestClass(unittest.TestCase):
    """for testing is_prime function"""

    def test1(self):

        self.assertEqual(is_prime(2),True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(11), True)
        self.assertEqual(is_prime(13), True)
        self.assertEqual(is_prime(131), True)
        self.assertEqual(is_prime(199), True)


    def test2(self):
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(6), False)
        self.assertEqual(is_prime(100), False)
        self.assertEqual(is_prime(1849), False)
