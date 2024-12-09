from EuclideanAlgo import euclidean
from baby_step_giant_step import baby_step_giant_step
from fast_expo_modulo import fast_expo_modulo
from is_prime import is_prime
from search_only_one_primitive_root import search_only_one_primitive_root

import unittest

class MyTestClass(unittest.TestCase):
    """for testing baby_step_giant_step"""

    def test1(self):
        """using the example from the text book"""
        prime = 29
        root = search_only_one_primitive_root(5)

        target = 3
        discrete_logarithm = baby_step_giant_step(root,target,prime)
        restored_target = fast_expo_modulo(root,discrete_logarithm,prime)
        self.assertEqual(target,restored_target)

    def test2(self):
        """using the example from the text book"""
        prime = 3
        root = 2
        target = 2
        discrete_logarithm = baby_step_giant_step(root,target,prime)
        restored_target = fast_expo_modulo(root,discrete_logarithm,prime)
        self.assertEqual(target,restored_target)

    def test3(self):
        """using the example from the text book"""
        prime = 23
        root = 5
        target = 14
        discrete_logarithm = baby_step_giant_step(root, target, prime)
        restored_target = fast_expo_modulo(root, discrete_logarithm, prime)
        self.assertEqual(target, restored_target)

    def test4(self):
        """reiteratively test some random values"""
        for num in range(1000):
            if is_prime(num):
                prime = num
                root = search_only_one_primitive_root(num)
                for element in range(num):
                    # if element is in the group(element must be coprime to num)
                    if euclidean(element,num) == 1:
                        target = element

                        discrete_logarithm = baby_step_giant_step(root,target,prime)
                        restored_target = fast_expo_modulo(root,discrete_logarithm,prime)
                        self.assertEqual(target,restored_target)


