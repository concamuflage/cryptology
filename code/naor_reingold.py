import random

from binary_string_cross_product import binary_string_cross_product
from decimal_to_binary import decimal_to_binary
from fast_expo_modulo import fast_expo_modulo
from random_prime_generator import random_prime_generator
from generate_large_prime import generate_large_prime
from pick_relatively_prime import pick_relatively_prime



def naor_reingold(big_n,a_pairs,g,n,x):
    """
    converts a n-bit decimal x into 1 or 0
    :param big_n: an integer
    :param a_pairs: a list of lists.
    :param g: a quare in group U(big_n)
    :param x: a n-bit decimal integer
    :param n: the bit length of decimal x.
    :return: 1 or 0
    """
    start = 4095
    end = 8191

    # generate string representation of x.

    x_string = decimal_to_binary(n,x)
    if len(x_string) > n:
        raise Exception("x should be at most n-bit long")

    # choose an a from each pair of a_pairs and sum them
    total = 0
    for index in range(n):
        y = int(x_string[index])
        total += a_pairs[index][y]
    # compute g^total/big_n
    result = fast_expo_modulo(g,total,big_n)
    # expand the result from a decimal to a binary of length 2n
    result_string = decimal_to_binary(2*n,result)
    # randomly generate a string of 2n length.
    rand_number = random_prime_generator(start,end)
    rand_string = decimal_to_binary(2*n,rand_number)
    # compute result_string * rand_string
    return binary_string_cross_product(rand_string,result_string)

def parameter_generator(n):
    """
    Generate the 3 parameters that are needed in the naor_reingold function
    :param n:
    :return:
    big_n, which is an integer ;
    a_pairs, which is a list of lists ;
    g, which is an integer;
    """
    # generate two n bit long primes q and q.
    p = generate_large_prime(n)
    q = generate_large_prime(n)
    big_n = p*q
    # randomly choose 2n integers from 1 to N and group them in pairs.
    a_pairs = []
    for count in range(n):
        a = random.randint(1, big_n)
        b = random.randint(1,big_n)
        a_pairs.append([a,b])
    # randomly choose g in U(big_n) and g is a square in U(big_n)
    big_n_coprime = pick_relatively_prime(big_n)
    g = big_n_coprime**2 % big_n

    return big_n,a_pairs,g







