
from naor_reingold import parameter_generator, naor_reingold
import unittest

class MyTestClass(unittest.TestCase):
    """testing the parameter_generator function"""
    def test1(self):
        big_n, a_pairs, g = parameter_generator(15)
        self.assertEqual(len(a_pairs),15)  # check if the length of list is correct

class MyTestClass(unittest.TestCase):
    """testing the naor_reingold function"""
    def test1(self):
        big_n, a_pairs, g = parameter_generator(15)
        list = []
        for number in range(43):
            result = naor_reingold(big_n,a_pairs,g,15,number)
            list.append(result)
            # with 0 or 1, the test will pass.
            self.assertTrue(result == 1 or result == 0)
        print(list)

