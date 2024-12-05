import random

from EuclideanAlgo import euclidean
from fast_expo_modulo import fast_expo_modulo
from generate_large_prime import generate_large_prime

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
    rand_number = generate_large_prime(20)
    rand_string = decimal_to_binary(2*n,rand_number)
    # compute result_string * rand_string
    return binary_string_cross_product(rand_string,result_string)

def parameter_generator(n):
    """
    Generate 3 parameters that are needed in the naor_reingold function
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


def pick_relatively_prime(int):
    """
    randomly pick a number that is coprime to int and less than int.
    :param int: integer
    :return: a number less than in and is cooprime to int.
    """
    while True:
        rand = random.randint(1,int)
        if euclidean(rand,int) == 1:
            return rand

def decimal_to_binary(length,int):
    """

    :param n: an integer
    :param int: an integer
    :return: the binary presentation of the integer that is n bit long.
    """
    binary_string = bin(int)[2:].zfill(length)
    return binary_string

def binary_string_cross_product(binary_vector_1,binary_vector_2):
    """
    :param binary_vector_1:
    :param binary_vector_2:
    :return:
    """
    length_1 = len(binary_vector_1)
    length_2 = len(binary_vector_2)
    if length_1 != length_2:
        raise Exception("The length of the vectors are not equal")
    total = 0    # for storing the sum of product
    for index in range(length_1):
        pair_sum = int(binary_vector_1[index])*int(binary_vector_2[index])
        total += pair_sum

    return total % 2





