import unittest

from miller_rabin import miller_rabin, miller_rabin_2
from pollard_rho_factorization import pollard_rho_factorization

#
class MyTestClass(unittest.TestCase):
    """testing binary_string_cross_product function"""
    def test1(self):
        """for testing large composite  numbers 20-21bits"""
        for num in range(4,10000):
            # test if the number is even
            if num % 2 == 0:
                continue       # if even, do nothing and try the next num
            # test if the number is composite
            result = miller_rabin_2(50, num)
            if result:
                continue       # if num is probably prime, do nothing
            result = pollard_rho_factorization(num)
            self.assertTrue(miller_rabin(50,result))
            self.assertEqual(num % result,0)

    def test2(self):
        """for testing a special case"""
        num = 4
        divisor = pollard_rho_factorization(num)
        self.assertTrue(miller_rabin(50,divisor))
        self.assertEqual(num % divisor,0)

    def test3(self):
        """for testing some large primes"""
        # 20635128451 is 48 bit with two 24 bit primes.
        # 113111472248121 is 64 bit
        numbers = [20635128451,113111472248121]
        for element in numbers:
            num = element
            divisor = pollard_rho_factorization(num)
            self.assertTrue(miller_rabin(50,divisor))
            self.assertEqual(num % divisor,0)

