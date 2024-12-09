import math
import random

from EuclideanAlgo import euclidean
from fast_expo_modulo import fast_expo_modulo
from fast_exponentiation import fast_exponentiation
from is_prime import is_prime
from random_prime_generator import random_prime_generator


def pollard_p_1_factorization_lecture_version(smoothness_bound,factor_base,n):
    """
    :param n: a composite number
    :factor_base: a list of all the prime numbers that are less than or equal to smoothness bound
    :return: a factor for n; the factor could be prime.
    """
    index = 0  # for iterating over the factor base.
    # test if the argument is bigger than 4
    if n < 4:
        raise Exception("The argument should be equal to or larger than 4")
    # test if the argument is composite
    result = is_prime(n)
    if result:
        raise Exception("The argument is not composite")
    # choose a random b, with 1<b< n-1
    b = random_prime_generator(1,n-1)
    g = euclidean(b,n)
    if g == n:       # there is no need to increase b^x as this gcd (b^x,n) = n as well. need to change b.
        return pollard_p_1_factorization_lecture_version(smoothness_bound,factor_base,n)
    if 1 < g < n:    # found a divisor
        return g
    if g == 1:      # b is relative to n.
        p = factor_base[index]
        while index < len(factor_base):
            l = math.floor(math.log(n,p))
            # b = b**(p**l)%n
            power = fast_exponentiation(p,l)
            b = fast_expo_modulo(b,power,n)
            g = euclidean(b-1,n)
            if g == n:
                return pollard_p_1_factorization_lecture_version(smoothness_bound,factor_base,n)
            if 1 < g < n:
                return g
            if g == 1:
                # try the next p in
                index +=1
                if index == len(factor_base): # check if the index is out of bound
                    break
                p = factor_base[index]
        raise Exception(f"failed to find a factor of {n}")

def compute_factor_base(n):
    """
    :param n: an integer
    :return: a list of all the prime numbers that are less than or equal to smoothness bound
    """
    if n < 2:
        raise Exception("The argument should be greater than or equal to 2")
    factor_base = []
    for i in range(2,n+1):
        if is_prime(i):
            factor_base.append(i)
    return factor_base









