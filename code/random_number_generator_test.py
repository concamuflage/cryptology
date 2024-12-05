from random_number_generator import random_number_generator
import unittest

class MyTestCase(unittest.TestCase):

    def test(self):
        """
        testing random_number_generator
        """
        for index in range(100):
            start = 10000
            end = 100000000
            result = random_number_generator(start,end)
            self.assertTrue(start < result < end or result == start or result == end )


