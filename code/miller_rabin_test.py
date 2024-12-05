from miller_rabin import convert, miller_rabin, miller_rabin_2
import unittest

class MyTestClass(unittest.TestCase):

    """for testing convert function"""
    def test1(self):
        """testing even numbers"""
        self.assertEqual(convert(8),(3,1))
        self.assertEqual(convert(10), (1, 5))
        self.assertEqual(convert(20), (2, 5))
        self.assertEqual(convert(26), (1, 13))
        self.assertEqual(convert(30), (1, 15))
        self.assertEqual(convert(100), (2, 25))
    def test2(self):
        """testing odd numbers"""
        self.assertRaises(Exception,convert,3)


class MyTestClass(unittest.TestCase):

    """testing convert miller_rabin function"""

    def test0(self):
        """
        testing edge cases.
        """
        self.assertTrue(miller_rabin(50,2))
        self.assertTrue(miller_rabin(50,3))

    def test1(self):
        """testing odd and prime numbers"""
        self.assertTrue(miller_rabin(50,11))
        self.assertTrue(miller_rabin(50,24738041398529))
        self.assertTrue(miller_rabin(50,994449669889999496698999))

    def test2(self):
        """testing odd and composite numbers"""
        self.assertFalse(miller_rabin(50, 1))
        self.assertFalse(miller_rabin(50,9))
        self.assertFalse(miller_rabin(50,27))
        self.assertFalse(miller_rabin(50,33))
        self.assertFalse(miller_rabin(50, 100127))

    def test3(self):
        """testing if both versions produce the same result"""
        self.assertEqual(miller_rabin(50, 5), miller_rabin_2(50, 5))
        self.assertEqual(miller_rabin(50,11),miller_rabin_2(50,11))
        self.assertEqual(miller_rabin(50, 1281), miller_rabin_2(50, 1281))
        self.assertEqual(miller_rabin(50, 1729), miller_rabin_2(50, 1729))
        self.assertEqual(miller_rabin(50,24738041398529), miller_rabin_2(50,24738041398529))
        self.assertEqual(miller_rabin(50,994449669889999496698999), miller_rabin_2(50,994449669889999496698999))


