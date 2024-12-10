import random

from fast_expo_modulo import fast_expo_modulo
from is_prime import is_prime
from ExtendedEuclidean import extended_euclidean_2
from search_only_one_primitive_root import search_only_one_primitive_root
from random_number_generator import random_number_generator

def el_gamal_sender_prepare(prime):
    """
    for sender to do precomputations
    :param prime: a prime number
    :return:
    r, a prime integer
    b, integer, an integer, which is a primitive root of group U(prime)
    b_to_power_of_r, an integer , which is b^r mod prime
    """
    # check the primality of the argument prime
    if not is_prime(prime):
        raise Exception(f"{prime} is not prime. Argument should be prime.")
    b = search_only_one_primitive_root(prime)  # b is the primitive root
    r = random_number_generator(0, prime - 2)  # generate private key r
    b_to_power_of_r = fast_expo_modulo(b, r,prime)
    return r, b, b_to_power_of_r


def el_gamal_receiver_prepare(b, b_to_power_of_r, prime):
    """
    for receiver to do precomputations
    :param b: integer, which is the primitive root of the group
    :param b_to_power_of_r: which is b^r mod p, shared by the sender.
    :param prime: a prime number
    :return:
    brl, an integer, which is (b^r)^l mod prime ;
    b_to_power_of_l, an integer, which is (b^l) mod prime ;
    brl_inverse, and integer, which is the inverse of brl in group U(prime)
    """
    # check the primality of the argument prime
    if not is_prime(prime):
        raise Exception(f"{prime} is not prime. Argument should be prime.")

    l = random_number_generator(0, prime - 2)
    # generate a private key
    b_to_power_of_l = fast_expo_modulo(b, l,prime)
    # computes (b^r)^l
    brl = fast_expo_modulo(b_to_power_of_r, l,prime)
    # computes inverse of (b^r)^l in G
    brl_inverse = extended_euclidean_2(brl,prime)[0]
    return brl, b_to_power_of_l, brl_inverse


def el_gamal_encrypt(message, b_to_power_of_l, r,prime):
    """
    for sender to encrypt the message
    :param message: an integer , which represents the message to be encrypted.
    :param b_to_power_of_l: an integer, which is provided by the receiver
    :param r: an integer, which is generated in the preparation stage of the cipher
    :param prime: a prime number
    :return: an integer
    """
    # check the primality of the argument prime
    if not is_prime(prime):
        raise Exception(f"{prime} is not prime. Argument should be prime.")

    # check if message is in U(prime)
    if message < 1 or message > prime or message == prime:
        raise Exception(f"Message not valid. Message must be in the range 1<=message <= {prime}")
    blr = fast_expo_modulo(b_to_power_of_l, r, prime)
    cipher_text = message * blr % prime
    return cipher_text

def el_gamal_decrypt(cipher_text, brl_inverse,prime):
    """
    for receiver to decrypt the ciphertex
    :param cipher_text: an integer
    :param brl_inverse: an integer
    :param prime:  a prime integer
    :return: an integer
    """
    # check the primality of the argument prime
    if not is_prime(prime):
        raise Exception(f"{prime} is not prime. Argument should be prime.")

    plain_text = cipher_text * brl_inverse % prime
    return plain_text
#
# if __name__ =="__main__":
#     # print(el_gamal_receiver_prepare(3,156229 ,839731))
#     # print(el_gamal_decrypt(638336,344169,839731))
#     print(el_gamal_encrypt(888,60090,6921,80687))