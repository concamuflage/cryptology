from is_prime import is_prime
from random_number_generator import random_number_generator

def random_prime_generator(n):
    """
    generate a n_bit random prime number
    :return: a prime number within in the range
    """
    candidate = random_number_generator(start,end)
    while True:
        if candidate % 2 != 0 and is_prime(candidate):
            return candidate
        candidate = random_number_generator(start, end)
    return candidate