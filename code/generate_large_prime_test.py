

import unittest

from generate_large_prime import generate_large_prime
from is_prime import is_prime


class MyTestClass(unittest.TestCase):
    """for testing generate_large_primes"""

    def test1(self):
        """test if the bit length is correct"""
        self.assertEqual(generate_large_prime(15).bit_length(),15)
        self.assertEqual(generate_large_prime(10).bit_length(), 10)
        self.assertEqual(generate_large_prime(5).bit_length(), 5)
        self.assertEqual(generate_large_prime(2).bit_length(), 2)

    def test1(self):
        """test if the prime % 4 == 3"""
        self.assertEqual(generate_large_prime(15)% 4, 3)
        self.assertEqual(generate_large_prime(10) % 4, 3)
        self.assertEqual(generate_large_prime(5) % 4, 3)
        self.assertEqual(generate_large_prime(2) % 4, 3)

    def test1(self):
        """test if the number is prime indeed"""
        self.assertTrue(is_prime(generate_large_prime(15)))
        self.assertTrue(is_prime(generate_large_prime(10)))
        self.assertTrue(is_prime(generate_large_prime(5)))
        self.assertTrue(is_prime(generate_large_prime(2)))







