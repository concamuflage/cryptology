import unittest

from miller_rabin import miller_rabin, miller_rabin_2
from pollard_p_1_factorization_lecture_version import pollard_p_1_factorization_lecture_version,compute_factor_base


class MyTestClass1(unittest.TestCase):
    """testing pollard_p_1_factorization function"""
    def test1(self):
        """for testing large composite  numbers 20-21bits"""
        num = 100
        upper_bound = 1000
        while num < upper_bound +1:
            # test if the number is even
            if num % 2 == 0:
                num += 1
                continue       # if even, do nothing and try the next num
            # test if the number is composite
            result = miller_rabin_2(50, num)
            if result:
                num += 1
                continue       # if num is probably prime, do nothing
            smoothness_bound = 500
            factor_base = compute_factor_base(smoothness_bound)
            try:
                result = pollard_p_1_factorization_lecture_version(smoothness_bound, factor_base, num)
            except:
                result = pollard_p_1_factorization_lecture_version(smoothness_bound, factor_base, num)
            self.assertEqual(num % result,0)
            num += 1

    def test2(self):
        """for testing a special case"""
        num = 1038361
        smoothness_bound = 700
        factor_base = compute_factor_base(smoothness_bound)
        divisor = pollard_p_1_factorization_lecture_version(smoothness_bound, factor_base, num)
        self.assertEqual(num % divisor,0)

    def test3(self):
        """for testing some large primes"""
        # 20635128451 is 48 bit with two 24 bit primes.
        # 113111472248121 is 64 bit
        numbers = [20635128451,113111472248121]
        for element in numbers:
            num = element
            smoothness_bound = 50
            factor_base = compute_factor_base(smoothness_bound)
            divisor = pollard_p_1_factorization_lecture_version(smoothness_bound, factor_base, num)
            self.assertEqual(num % divisor,0)

    def test4(self):
        """for testing a special case"""
        num = 143
        smoothness_bound = 5
        factor_base = compute_factor_base(smoothness_bound)
        divisor = pollard_p_1_factorization_lecture_version(smoothness_bound, factor_base, num)
        self.assertEqual(num % divisor,0)

class MyTestClass2(unittest.TestCase):
    """testing compute_factor_base """
    def test1(self):
        self.assertEqual(compute_factor_base(2), [2])
        self.assertEqual(compute_factor_base(5),[2,3,5])
        self.assertEqual(compute_factor_base(8), [2, 3, 5,7])
        self.assertEqual(compute_factor_base(10), [2, 3, 5, 7])
        list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(compute_factor_base(100), list)


