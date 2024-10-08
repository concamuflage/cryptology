import unittest,random
from EuclideanAlgo import steins, euclidean

class MyTestCase(unittest.TestCase):

    # def test(self):
    #     result1 = steins(3276,9829)
    #     result2 = euclidian(3276,9829)
    #     self.assertEqual(result1, result2)

    def test(self):
        for i in range(1000):
            random_num1 = random.randint(1,100)
            random_num2 = random.randint(1,100)

            try:
                result1 = steins(random_num1, random_num2)
            except:
                print("steins",random_num1,random_num2)
                return

            try:
                result2 = euclidean(random_num1, random_num2)
            except:
                print("euclidean",random_num1,random_num2)
                return

            self.assertEqual(result1,result2)



    def test(self):
    
        for i in range(10):
            random_num1 = random.randint(1,100)
            random_num2 = random.randint(1,100)
        MyTestCase.assertEqual(steins(random_num1,random_num2),euclidean(random_num1,random_num2))