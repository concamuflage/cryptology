import random
from sympy import nextprime


def generate_large_prime(num_of_bits):
    """generate a randomly large prime of length specified by the argument; the prime % 4 = 3
    :param num_of_bits: integer
    """
    random_bits = random.getrandbits(num_of_bits)
    prime = nextprime(random_bits)
    while prime % 4 != 3:
        prime = nextprime(prime)
    return prime




