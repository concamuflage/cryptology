from EuclideanAlgo import euclidean
from baby_step_giant_step import baby_step_giant_step
from fast_expo_modulo import fast_expo_modulo
from miller_rabin import miller_rabin_2
from primitive_root_search import primitive_root_search

import unittest

class MyTestClass(unittest.TestCase):
    """for testing baby_step_giant_step"""

    def test1(self):
        """using the example from the text book"""
        prime = 29
        root = primitive_root_search(5)[0]
        target = 3
        discrete_logarithm = baby_step_giant_step(root,target,prime)
        restored_target = fast_expo_modulo(root,discrete_logarithm,prime)
        self.assertEqual(target,restored_target)

    def test1(self):
        """using the example from the text book"""
        prime = 3
        root = 2
        target = 2
        discrete_logarithm = baby_step_giant_step(root,target,prime)
        restored_target = fast_expo_modulo(root,discrete_logarithm,prime)
        self.assertEqual(target,restored_target)

    def test1(self):
        """using the example from the text book"""
        prime = 23
        root = 5
        target = 14
        discrete_logarithm = baby_step_giant_step(root, target, prime)
        restored_target = fast_expo_modulo(root, discrete_logarithm, prime)
        self.assertEqual(target, restored_target)

    def test1(self):
        """reiteratively test some random values"""
        for num in range(1000):
            if num % 2 == 1 and miller_rabin_2(50,num):
                prime = num
                root = primitive_root_search(num)[0]
                for element in range(num):
                    # if element is in the group(element must be coprime to num)
                    if euclidean(element,num) == 1:
                        target = element

                        discrete_logarithm = baby_step_giant_step(root,target,prime)
                        restored_target = fast_expo_modulo(root,discrete_logarithm,prime)
                        self.assertEqual(target,restored_target)


