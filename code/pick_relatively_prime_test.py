import unittest

from EuclideanAlgo import euclidean
from pick_relatively_prime import pick_relatively_prime


class MyTestClass(unittest.TestCase):
    """testing pick_relatively prime"""
    def test1(self):
        self.assertEqual(euclidean(pick_relatively_prime(30),30),1)
        self.assertEqual(euclidean(pick_relatively_prime(300),300), 1)
        self.assertEqual(euclidean(pick_relatively_prime(300000),300000), 1)