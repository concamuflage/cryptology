import unittest,random
from ExtendedEuclidean import extended_euclidean,extended_euclidean_2
from EuclideanAlgo import euclidean

class MyTestCase(unittest.TestCase):
    """for testing extended_euclidean"""
    def test(self):
        """test both the ExtendedEuclidean function and euclidian function"""
        for i in range(3):
            random_num1 = random.randint(0,10000)
            random_num2 = random.randint(0,10000)
            result = extended_euclidean(random_num1,random_num2)
            sum = result[0]*random_num1+result[1]*random_num2
            self.assertEqual(sum,euclidean(random_num1,random_num2))
    def test(self):
        """test if num1 == num2"""
        result = extended_euclidean(50, 50)
        sum = result[0] * 50 + result[1] * 50
        self.assertEqual(sum, euclidean(50, 50))

    def test(self):
        """test if num1 < num2"""

        self.assertRaises(Exception,extended_euclidean(50, 60))

class MyTestCase(unittest.TestCase):

    """for testing extended_euclidean_2"""
    def test(self):
        """test both the ExtendedEuclidean function and euclidian function"""
        for i in range(3):
            random_num1 = random.randint(0,10000)
            random_num2 = random.randint(0,10000)
            result = extended_euclidean_2(random_num1,random_num2)
            sum = result[0]*random_num1+result[1]*random_num2
            self.assertEqual(sum,euclidean(random_num1,random_num2))
    def test(self):
        """test if num1 == num2"""
        result = extended_euclidean_2(50, 50)
        sum = result[0] * 50 + result[1] * 50
        self.assertEqual(sum, euclidean(50, 50))

    def test(self):
        """test if num1 < num2"""

        self.assertRaises(Exception,extended_euclidean_2(50, 60))

