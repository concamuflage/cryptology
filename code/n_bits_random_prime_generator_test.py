from n_bits_random_prime_generator import n_bits_random_prime_generator
import unittest
from is_prime import is_prime

class MyTestCase(unittest.TestCase):
    """
    testing n_bits random_prime_generator function
    """
    def test1(self):
        for index in range(2,70):
            result = n_bits_random_prime_generator(index)
            self.assertTrue(result.bit_length() == index)
            self.assertTrue(is_prime(result))

    def test2(self):

        index = 5
        result = n_bits_random_prime_generator(index)
        self.assertTrue(result.bit_length() == index)
        self.assertTrue(is_prime(result))

    def test3(self):
        self.assertRaises(Exception,n_bits_random_prime_generator,1)