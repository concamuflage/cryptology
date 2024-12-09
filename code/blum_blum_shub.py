import random
from pick_relatively_prime import pick_relatively_prime
from generate_large_prime import generate_large_prime
def blum_blum_shub(m):
    """
    to generate a sequence of pseudorandom bits of length m
    :param m, integer
    :return a list of 1's and 0's
    """

    # to generate p and q such that p % 4 =3 and q % 4 = 3
    bit_length = 13
    p,q = 2,2
    while p % 4 != 3:
        p = generate_large_prime(bit_length)
    while q % 4 != 3:
        q = generate_large_prime(bit_length)
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
















