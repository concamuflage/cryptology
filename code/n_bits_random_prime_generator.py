from is_prime import is_prime
from n_bits_random_number_generator import n_bits_random_number_generator
from random_number_generator import random_number_generator

def n_bits_random_prime_generator(n):
    """
    for generating a n_bit long random prime number
    :param n: an integer
    :return: an n-bit long prime number
    """
    if n < 2:
        raise ValueError("n must be equal to or greater than 2. You cannot generate a prime with only 1 bit")
    candidate = n_bits_random_number_generator(n)
    while not is_prime(candidate):
        candidate = n_bits_random_number_generator(n)
    return candidate