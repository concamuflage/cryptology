import unittest

from miller_rabin import miller_rabin
from generate_large_prime import generate_large_prime


class MyTestCase(unittest.TestCase):

    def test(self):
        """
        testing generate_large_prime
        """
        for index in range(2,40):
            result = generate_large_prime(index)
            # test if the number is of correct length
            self.assertEqual(result.bit_length(),index)
            # test if it is a prime
            self.assertTrue(miller_rabin(50,result))

    def test1(self):
        index = 30
        result = generate_large_prime(index)
        # test if the number is of correct length
        self.assertEqual(result.bit_length(),index)
        # test if it is a prime
        self.assertTrue(miller_rabin(50,result))
    def test2(self):
        self.assertRaises(Exception,generate_large_prime,1)