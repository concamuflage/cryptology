import unittest

from miller_rabin import miller_rabin
from random_prime_generator import random_prime_generator


class MyTestCase(unittest.TestCase):

    def test(self):
        """
        testing random_prime_generator
        """
        start = 100000000000000000000000
        end = 100000000000000000000000000
        for index in range(100):
            result = random_prime_generator(start,end)
            # test if the number is in the desired range
            self.assertTrue(start < result < end or result == start or result == end )
            # test if it is a prime
            self.assertTrue(miller_rabin(50,result))
            print(result)

