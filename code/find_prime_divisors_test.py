
from is_prime import is_prime
from find_prime_divisors import find_prime_divisors
import unittest

class MyTestClass(unittest.TestCase):
    """for testing find_prime_divisors"""

    def test1(self):
        self.assertEqual(find_prime_divisors(4), {2})
        self.assertEqual(find_prime_divisors(5),{5})
        self.assertEqual(find_prime_divisors(10), {2,5})
        self.assertEqual(find_prime_divisors(100),{2,5})
        self.assertEqual(find_prime_divisors(33), {3, 11})
        self.assertEqual(find_prime_divisors(99), {3, 11})
        self.assertEqual(find_prime_divisors(210), {2,3,5,7})
        self.assertEqual(find_prime_divisors(2100), {2, 3, 5, 7})
        self.assertEqual(find_prime_divisors(30030), {2, 3, 5, 7,11,13})