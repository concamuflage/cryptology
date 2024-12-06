from EuclideanAlgo import euclidean
from naor_reingold import binary_string_cross_product, decimal_to_binary, pick_relatively_prime, parameter_generator, \
    naor_reingold
import unittest

class MyTestClass(unittest.TestCase):
    """testing binary_string_cross_product function"""
    def test1(self):
        "testing vectors with length 1"
        self.assertEqual(binary_string_cross_product("0","1"),0)
        self.assertEqual(binary_string_cross_product("0", "0"), 0)
        self.assertEqual(binary_string_cross_product("1", "1"), 1)
        self.assertEqual(binary_string_cross_product("1", "0"), 0)

    def test2(self):
        "testing vectors with length 2"
        self.assertEqual(binary_string_cross_product("01","11"),1)
        self.assertEqual(binary_string_cross_product("10", "01"), 0)
        self.assertEqual(binary_string_cross_product("11", "10"), 1)
        self.assertEqual(binary_string_cross_product("10", "01"), 0)

    def test3(self):
        "testing vectors with length 2"
        self.assertEqual(binary_string_cross_product("111","111"),1)
        self.assertEqual(binary_string_cross_product("110", "101"), 1)
        self.assertEqual(binary_string_cross_product("110", "100"), 1)
        self.assertEqual(binary_string_cross_product("110", "011"), 1)
    def test4(self):
        "testing vectors with different length"
        self.assertRaises(Exception,binary_string_cross_product,"1111","111")


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

