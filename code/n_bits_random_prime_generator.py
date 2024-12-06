from miller_rabin import miller_rabin
from random_number_generator import random_number_generator

def random_prime_generator(n):
    """
    generate a n_bit random prime number
    :return: a prime number within in the range
    """
    candidate = random_number_generator(start,end)
    while True:
        if candidate % 2 != 0 and miller_rabin(50,candidate):
            return candidate
        candidate = random_number_generator(start, end)
    return candidate