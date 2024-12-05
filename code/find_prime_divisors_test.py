
from is_prime import is_prime
from find_prime_divisors import find_prime_divisors
import unittest

class MyTestClass(unittest.TestCase):
    """for testing find_prime_divisors"""

    def test1(self):
        self.assertEqual(find_prime_divisors(0), [])
        self.assertEqual(find_prime_divisors(1),[])
        self.assertEqual(find_prime_divisors(2), [2])
        self.assertEqual(find_prime_divisors(3), [3])
        self.assertEqual(find_prime_divisors(5),[5])
        self.assertEqual(find_prime_divisors(10), [2,5])
        self.assertEqual(find_prime_divisors(100), [2,5])
        self.assertEqual(find_prime_divisors(33), [3, 11])
        self.assertEqual(find_prime_divisors(99), [3, 11])