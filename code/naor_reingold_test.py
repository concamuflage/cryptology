
from naor_reingold import parameter_generator, naor_reingold
import unittest

class MyTestClass(unittest.TestCase):

    def test1(self):
        """testing the parameter_generator function"""
        big_n, a_pairs, g = parameter_generator(15)
        self.assertEqual(len(a_pairs),15)  # check if the length of list is correct

    def test2(self):
        """testing the naor_reingold function"""

        big_n, a_pairs, g = parameter_generator(15)
        list = []
        for number in range(43):
            result = naor_reingold(big_n,a_pairs,g,15,number)
            list.append(result)
            # with 0 or 1, the test will pass.
            self.assertTrue(result == 1 or result == 0)

# if __name__ == "__main__":
#     test = MyTestClass()
#     test.test1()
#     test.test2()
