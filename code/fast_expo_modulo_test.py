import unittest

from fast_expo_modulo import fast_expo_modulo
from fast_exponentiation import fast_exponentiation
class MyTestClass(unittest.TestCase):
    """for testing fast_exponentiation function"""

    def test1(self):

        self.assertEqual(fast_exponentiation(2, 100)%5, fast_expo_modulo(2,100,5))
        self.assertEqual(fast_exponentiation(7, 9)%3,fast_expo_modulo(7,9,3))
        self.assertEqual(fast_exponentiation(2, 2)%5,fast_expo_modulo(2,2,5))
        self.assertEqual(fast_exponentiation(2, 3)%9,fast_expo_modulo(2,3,9))
        self.assertEqual(fast_exponentiation(3, 2)%100,fast_expo_modulo(3,2,100))
        self.assertEqual(fast_exponentiation(3, 5)%1,fast_expo_modulo(3,5,1))

    def test2(self):
        """test both functions with random numbers"""
        for root in range(0,20):
            for power in range (0,20):
                for modulus in range (1,20):
                    print(root, power, modulus)
                    x = fast_exponentiation(root, power) % modulus
                    y = fast_expo_modulo(root, power, modulus)
                    self.assertEqual(x, y)
                    # try:
                    #     self.assertEqual(fast_exponentiation(root, power) % modulus,fast_expo_modulo(root, power, modulus))
                    # except:
                    #     print(root,power,modulus)


