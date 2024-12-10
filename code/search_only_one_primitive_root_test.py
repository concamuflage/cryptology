from find_prime_divisors import find_prime_divisors
from is_prime import is_prime
from n_bits_safe_prime_generator import n_bits_safe_prime_generator
from primitive_root_search import primitive_root_search
from search_only_one_primitive_root import search_only_one_primitive_root
from fast_expo_modulo import fast_expo_modulo
import unittest

class MyTestClass(unittest.TestCase):
    """for testing primitive_root_search"""

    def test1(self):
        self.assertTrue(search_only_one_primitive_root(2) in primitive_root_search(2))
        self.assertTrue(search_only_one_primitive_root(5) in primitive_root_search(5))
        self.assertTrue(3  in primitive_root_search(839731))


    def test2(self):

        """test if the found primitive root  is  actually primitive root"""
        for number in range(4,1000):
            if is_prime(number):
                group_order = number -1
                root = search_only_one_primitive_root(number)
                # find prime divisors of group_order
                prime_divisors = find_prime_divisors(group_order)

                # compute all possible values of group_order/p (p in prime_divisors)
                possible_exponents = []
                for element in prime_divisors:
                    possible_exponents.append(group_order // element)

                for power in possible_exponents:
                    result = fast_expo_modulo(root, power, number)
                    # print("-----------------------------")
                    # print(number, root)
                    # print(prime_divisors)
                    # print(possible_exponents)
                    # print(root,power,number)
                    self.assertNotEqual(result, 1)


    def test3(self):

        """testing large safe prime numbers"""

        for index in range(50,70):
            number = n_bits_safe_prime_generator(index)

            if is_prime(number):
                group_order = number-1
                root = search_only_one_primitive_root(number)

                # find prime divisors of group_order
                prime_divisors = find_prime_divisors(group_order)

                # compute all possible values of group_order/p (p in prime_divisors)
                possible_exponents = []
                for element in prime_divisors:
                    possible_exponents.append(group_order // element)

                for power in possible_exponents:
                    result = fast_expo_modulo(root, power, number)
                    # print("-----------------------------")
                    # print(number, root)
                    # print(prime_divisors)
                    # print(possible_exponents)
                    # print(root,power,number)
                    self.assertNotEqual(result,1)
