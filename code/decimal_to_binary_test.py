import unittest

from decimal_to_binary import decimal_to_binary


class MyTestClass(unittest.TestCase):
    """testing decimal_to_binary"""
    def test1(self):
        self.assertEqual(decimal_to_binary(10, 0), "0000000000")
        self.assertEqual(decimal_to_binary(10, 1), "0000000001")
        self.assertEqual(decimal_to_binary(15, 100), "000000001100100")
        self.assertEqual(decimal_to_binary(10,5),"0000000101")
        self.assertEqual(decimal_to_binary(15, 100), "000000001100100")