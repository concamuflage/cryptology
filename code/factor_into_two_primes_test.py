
import unittest
from factor_into_two_primes import factor_into_two_primes

class MyTestClass(unittest.TestCase):

    def test1(self):
        self.assertEqual(factor_into_two_primes(10403),[101,103])
        self.assertEqual(factor_into_two_primes(27221),[163,167])
        self.assertEqual(factor_into_two_primes(33), [3, 11])







