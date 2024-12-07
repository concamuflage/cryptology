import unittest

from is_prime import is_prime
from safe_prime_generator import safe_prime_generator


class MyTestCase(unittest.TestCase):

    def test(self):
        """
        testing random_prime_generator
        """
        start = 100000000000000000000000
        end = 100000000000000000000000000
        for index in range(2):
            result =safe_prime_generator(start,end)
            # test if the number is in the desired range
            self.assertTrue(start <= result <=end )
            # test if it is a prime
            self.assertTrue(is_prime(result))
            # test if it is a safe prime
            q = (result-1) // 2
            self.assertTrue(is_prime(q))