from is_prime import is_prime
from n_bits_random_number_generator import n_bits_random_number_generator
from n_bits_random_prime_generator import n_bits_random_prime_generator
from random_number_generator import random_number_generator


def n_bits_safe_prime_generator(n):
    """
    generate a n_bit random prime number
    :return: a prime number within in the range
    """
    while True:
        q = n_bits_random_prime_generator(n)
        p = 2*q+1
        if is_prime(p):
            return p
