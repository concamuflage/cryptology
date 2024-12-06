
from miller_rabin import miller_rabin
from random_prime_generator import random_prime_generator


def safe_prime_generator(start, end):
    """
    for generating a safe prime within the given range [start,end] including end points.
    :return: a safe prime p such that p = 2q +1 ,with q being prime and start <=b <= end
    """
    while True:
        q = random_prime_generator(start,end)
        p = 2*q+1
        if start <= p <= end and p % 2 != 0 and miller_rabin(50,p):
            return p

