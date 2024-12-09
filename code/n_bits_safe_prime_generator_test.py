import unittest

from is_prime import is_prime
from n_bits_safe_prime_generator import n_bits_safe_prime_generator

class MyTestCase(unittest.TestCase):


    def test1(self):

        for index in range(50,60):
            result =n_bits_safe_prime_generator(index)
            # test if it's length is n
            self.assertEqual(result.bit_length(),index)
            # test if it is a prime
            self.assertTrue(is_prime(result))
            # test if it is a safe prime
            q = (result-1) // 2
            self.assertTrue(is_prime(q))



