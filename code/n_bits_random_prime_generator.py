from is_prime import is_prime
from n_bits_random_number_generator import n_bits_random_number_generator
from random_number_generator import random_number_generator

def n_bits_random_prime_generator(n):
    """
    generate a n_bit random prime number
    :return: a prime number within in the range
    """
    candidate = n_bits_random_number_generator(n)
    while True:
        if is_prime(candidate):
            return candidate
        candidate = n_bits_random_number_generator(n)