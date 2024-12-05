import random

from generate_large_prime import generate_large_prime
from naor_reingold import pick_relatively_prime,decimal_to_binary

def blum_blum_shub(m):
    """
    to generate a sequence of pseudorandom bits of length m
    :param m, integer
    """

    # to generate p and q such that p % 4 =3 and q % 4 = 3

    p,q = 2,2
    while p % 4 != 3:
        p = generate_large_prime(15)
    while q % 4 != 3:
        q = generate_large_prime(15)
    n = p*q
    # Choose a random seed in U(n)
    seed = pick_relatively_prime(n)
    bit_sequence = []
    # compute a bit sequence of length m
    for index in range(m):
        bit = seed % 2
        bit_sequence.append(bit)
        seed = seed**2 % n
    return bit_sequence
















