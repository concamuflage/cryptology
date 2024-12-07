import unittest,random
from ExtendedEuclidean import extended_euclidean_2
from EuclideanAlgo import euclidean

class MyTestCase2(unittest.TestCase):

    """for testing extended_euclidean_2"""
    def test1(self):
        """test both the ExtendedEuclidean function and euclidian function"""
        for i in range(100000):
            random_num1 = random.randint(0,100000000000)
            random_num2 = random.randint(0,100000000000)
            if random_num1 < random_num2:
                result = extended_euclidean_2(random_num1,random_num2)
                sum = result[0] * random_num1 + result[1] * random_num2
                self.assertEqual(sum, euclidean(random_num1, random_num2))
                self.assertTrue(result[0] < random_num2)
            else:
                result = extended_euclidean_2(random_num2,random_num1)
                sum = result[0] * random_num2 + result[1] * random_num1
                self.assertEqual(sum, euclidean(random_num1, random_num2))
                self.assertTrue(result[0] < random_num1)
    def test2(self):
        """test if num1 == num2"""
        result = extended_euclidean_2(50, 50)
        sum = result[0] * 50 + result[1] * 50
        self.assertEqual(sum, euclidean(50, 50))

    def test3(self):
        """test if num1 < num2"""

        self.assertRaises(Exception,extended_euclidean_2(50, 60))



