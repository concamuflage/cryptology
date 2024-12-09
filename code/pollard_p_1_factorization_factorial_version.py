import math
from sympy import gcd

import math
import random

from EuclideanAlgo import euclidean
from fast_expo_modulo import fast_expo_modulo
from fast_exponentiation import fast_exponentiation
from is_prime import is_prime
def pollard_p_1_factorization_factorial_version(smoothness_bound,n):
    """
    for factoring n with Pollard's p-1 method with T= B!; B is the smoothness_bound of p-1.
    The disadvantage of this approach is that the B! grows so fast ; soon it will break our fast exponentiation method.
    :param smoothness_bound:
    :param n: a composite number
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
    # if the chosen b is not relatively prime to a prime factor of n
    # then gcd() operation will not help us reveal a non-trivial factor of n.from
    # we don't know p yet, so we keep guessing

    b = random.randint(1,n-1)
    g = euclidean(b,n)  # to test of the chosen b is a desired b.
    # a desired b should be relatively prime to n so that b is relatively prime to all prime factors of n.
    # with such a b, we can apply the fermat's little theorem with confidence.

    if g == n:       # means b is multiple of n.
        # this is a very bad b because it is a multiple of any prime factor of n.
        # meaning that gcd(b,p) = p, meaning
        return pollard_p_1_factorization_factorial_version(smoothness_bound,n)
    if 1 < g < n:
        return g
    if g == 1:
        # b and n are relatively prime,
        # then, b is relatively prime to all prime factors of n.
        # this is a quite good b, but it may not work. We'll see why later.
        right_most_num_of_factorial = 3
        old_factorial = 1*2
        while right_most_num_of_factorial < smoothness_bound +1:
            new_factorial = old_factorial*right_most_num_of_factorial
            old_factorial = new_factorial
            right_most_num_of_factorial += 1
            try:
                result = fast_expo_modulo(b,new_factorial,n)
            except:
                print("debugging",b,new_factorial,n)
            g = euclidean(result-1,n)
            if g == n:  # meaning result-1 is a multiple of n. we need to restart so another b might be generated.
                # because if n | b^(c!)-1, then n | (b ^ (c+1)!)
                # if we keep the b and loop again, we'll still get g = n.
                # you can try this by removing the following state and replacing it with pass.
                # then, you might not be able to find a factor for n = 9 and smoothness bound = 50
                return pollard_p_1_factorization_factorial_version(smoothness_bound,n)
            if 1 < g < n:
                return g
            if g == 1: # for example, when b = 539704, n = 1000189, in all loops, gcd continues to be 1 until the loop is broken.
                # to avoid this case, we need to change b as well.
                # but there is no a general rule such that if gcd(b^(c!)-1, n)= 1, then gcd(b^(c+1!)-1, n)= 1
                return pollard_p_1_factorization_factorial_version(smoothness_bound, n)

        raise Exception(f"failed to find a factor of {n}")










