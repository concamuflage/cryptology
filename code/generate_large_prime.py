import random

from is_prime import is_prime

def generate_large_prime(n):
    """
    for generating an n-bit prime, based on python library function
    :param integer
    :return a n-bit prime integer
    """
    if n < 2:
        raise ValueError("n must be greater than 1")
    while True:
        decimal_number = random.getrandbits(n)
        if decimal_number % 2 == 0:
            continue
        if decimal_number.bit_length() != n:
            continue
        if is_prime(decimal_number):
            return decimal_number

