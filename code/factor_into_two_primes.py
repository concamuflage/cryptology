

import math
from is_prime import is_prime


def factor_into_two_primes(num):

    """
    :param num: an integer
    :return: two prime numbers p and q such that num = pq or [] if there is no way to factor the number into two primes.
    """
    result = []
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if is_prime(i) and num % i == 0 : # if i is prime and i divides num
            # print(i)
            if is_prime(num // i ):
                result.append(i)
                result.append(num // i)
    if len(result) == 0:
        raise Exception("Error: this number cannot be factored into two primes.")
    return result





