import random

from miller_rabin import miller_rabin

def generate_large_prime(n):
    """for generating a n-bit prime """
    if n < 2:
        raise ValueError("n must be greater than 1")
    while True:
        decimal_number = random.getrandbits(n)
        if decimal_number % 2 == 0:
            continue
        if decimal_number.bit_length() != n:
            continue
        if miller_rabin(50,decimal_number):
            return decimal_number

