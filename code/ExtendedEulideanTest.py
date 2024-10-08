import unittest,random
from ExtendedEuclidean import extended_euclidean
from EuclideanAlgo import euclidean

class MyTestCase(unittest.TestCase):

    def test(self):
        """test both the extended_euclidean and euclidian"""
        for i in range(3):
            random_num1 = random.randint(0,10000)
            random_num2 = random.randint(0,10000)
            result = extended_euclidean(random_num1,random_num2)
            sum = result[0]*random_num1+result[1]*random_num2
            self.assertEqual(sum,euclidean(random_num1,random_num2)) 

