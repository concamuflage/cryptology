import unittest

from binary_string_cross_product import binary_string_cross_product

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
