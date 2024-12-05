from miller_rabin import miller_rabin
from random_number_generator import random_number_generator

def random_prime_generator(start,end):
    """
    generate a random prime number with in the range [start, end],including end points.
    :return: a prime number within in the range
    """
    candidate = random_number_generator(start,end)
    while True:
        if candidate % 2 != 0 and miller_rabin(50,candidate):
            return candidate
        candidate = random_number_generator(start, end)
    return candidate