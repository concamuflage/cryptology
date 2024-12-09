import random
from pick_relatively_prime import pick_relatively_prime
from generate_large_prime import generate_large_prime
def blum_blum_shub_with_fixed_seeds(m):
    """
    to generate a sequence of pseudorandom bits of length m
    :param m, integer
    """

    # to generate p and q such that p % 4 =3 and q % 4 = 3
    # bit_length = 13
    # p,q = 2,2
    # while p % 4 != 3:
    #     p = generate_large_prime(bit_length)
    # while q % 4 != 3:
    #     q = generate_large_prime(bit_length)

    p = 54959
    q = 33107
    n = p*q
    # Choose a random seed in U(n)
    seed = 1465162309
    bit_sequence = []
    # compute a bit sequence of length m
    for index in range(m):
        bit = seed % 2
        bit_sequence.append(bit)
        seed = seed**2 % n
    return bit_sequence

# if __name__ == "__main__":
#     print(blum_blum_shub_with_fixed_seeds(3))
















