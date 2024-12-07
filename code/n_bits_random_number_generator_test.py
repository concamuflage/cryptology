from n_bits_random_number_generator import n_bits_random_number_generator
import unittest

class MyTestCase(unittest.TestCase):

    def test(self):
        """
        testing n_bitsrandom_number_generator function
        """
        for index in range(100):
            result = n_bits_random_number_generator(index)
            self.assertTrue(result.bit_length() == index)

    def test(self):
        """
        testing n_bitsrandom_number_generator function
        """
        index = 5
        result = n_bits_random_number_generator(index)
        self.assertTrue(result.bit_length() == index)