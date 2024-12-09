from is_prime import is_prime
from n_bits_safe_prime_generator import n_bits_safe_prime_generator
from primitive_root_search import primitive_root_search
from miller_rabin import miller_rabin_2
from fast_expo_modulo import fast_expo_modulo
import unittest

class MyTestClass(unittest.TestCase):
    """for testing primitive_root_search"""

    def test1(self):
        self.assertEqual(primitive_root_search(2),[1])
        self.assertEqual(primitive_root_search(5),[2,3])
        self.assertEqual(primitive_root_search(3), [2])
        self.assertRaises(Exception,primitive_root_search,6)


    def test2(self):

        """test if the found primitive roots are actually primitive roots"""
        for number in range(4,1000):
            if is_prime(number):
                primitive_roots = primitive_root_search(number)

                for root in primitive_roots:
                    # if it is a primitive root, then |root| = number - 1 and root ^ (number -1) % number = 1
                    # by Fermat's theorem
                    self.assertEqual(fast_expo_modulo(root, number-1, number),1)

    def test3(self):

        """testing large safe prime numbers"""

        for index in range(20,21):
            number = n_bits_safe_prime_generator(index)
            if is_prime(number):
                primitive_roots = primitive_root_search(number)
                for root in primitive_roots:
                    # if it is a primitive root, then |root| = number - 1 and root ^ (number -1) % number = 1
                    # by Fermat's theorem
                    self.assertEqual(fast_expo_modulo(root, number-1, number),1)