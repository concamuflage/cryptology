from is_prime import is_prime
from n_bits_random_number_generator import n_bits_random_number_generator
from n_bits_random_prime_generator import n_bits_random_prime_generator
from random_number_generator import random_number_generator


def n_bits_safe_prime_generator(n):
    """
    generate a n_bit long  random prime number
    :param n: an integer
    :return: a n_bit long  random prime number
    """
    if n < 3:
        raise ValueError("n must be bigger than or equal to 3. The smallest safe prime is 5 and we need 3 bits to present it")
    # while True:
    #     p = n_bits_random_prime_generator(n)
    #     q = (p - 1) // 2
    #     if is_prime(q):
    #         return p

    while True:
        q = n_bits_random_prime_generator(n - 1)
        p = 2*q +1
        if is_prime(p) and p.bit_length() == n :
            return p
