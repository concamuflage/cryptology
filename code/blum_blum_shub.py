import random
from naor_reingold import pick_relatively_prime,decimal_to_binary
from random_prime_generator import random_prime_generator
def blum_blum_shub(m):
    """
    to generate a sequence of pseudorandom bits of length m
    :param m, integer
    """

    # to generate p and q such that p % 4 =3 and q % 4 = 3
    start = 4095
    end = 8191

    p,q = 2,2
    while p % 4 != 3:
        p = random_prime_generator(start,end)
    while q % 4 != 3:
        q = random_prime_generator(start,end)
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
















