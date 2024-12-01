from primitive_root_search import primitive_root_search
from is_prime import is_prime
from fast_expo_modulo import fast_expo_modulo
import unittest

class MyTestClass(unittest.TestCase):
    """for testing primitive_root_search"""

    def test1(self):
        self.assertEqual(primitive_root_search(5),[2,3])
        self.assertEqual(primitive_root_search(3), [2])

    def test2(self):

        """test if the found primitive roots are actually primitive roots"""
        for number in range(1000):
            if is_prime(number):
                primitive_roots = primitive_root_search(number)
                print(number, primitive_roots)
                for root in primitive_roots:
                    # if it is a primitive root, then |root| = number - 1 and root ^ (number -1) % number = 1
                    # by Fermat's theorem
                    self.assertEqual(fast_expo_modulo(root, number-1, number),1)