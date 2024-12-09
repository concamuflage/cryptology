import unittest,random
from EuclideanAlgo import steins, euclidean

class MyTestCase(unittest.TestCase):

    def test1(self):
        result1 = steins(3276,9829)
        result2 = euclidean(3276,9829)
        self.assertEqual(result1, result2)

    def test2(self):
        for i in range(1000):
            random_num1 = random.randint(1,100)
            random_num2 = random.randint(1,100)
            result1 = steins(random_num1, random_num2)
            result2 = euclidean(random_num1, random_num2)
            self.assertEqual(result1,result2)



    def test3(self):
    
        for i in range(10):
            random_num1 = random.randint(1,100)
            random_num2 = random.randint(1,100)
            result1 = steins(random_num1,random_num2)
            result2 = euclidean(random_num1,random_num2)
            self.assertEqual(result1,result2)

    def test4(self):

        self.assertEqual(steins(0,5),5)
        self.assertEqual(steins(5,0),5)