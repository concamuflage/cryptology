import random

from fast_expo_modulo import fast_expo_modulo
from fast_exponentiation import fast_exponentiation
from is_prime import is_prime
from miller_rabin import miller_rabin
from primitive_root_search import primitive_root_search
from ExtendedEuclidean import extended_euclidean_2


def el_gamal_sender_prepare(prime):
    """
    :param prime: a prime number
    :return:
    r, a prime integer
    b, integer, a primitive root of group U(prime)
    b_to_power_of_r, integer , which is b^r mod prime
    """
    # check the primality of the argument prime
    if not is_prime(prime):
        raise Exception(f"{prime} is not prime. Argument should be prime.")
    b = primitive_root_search(prime)[0]  # b is the primitive root
    r = random.randint(0, prime - 2)  # generate private key r
    b_to_power_of_r = fast_expo_modulo(b, r,prime)
    return r, b, b_to_power_of_r


def el_gamal_receiver_prepare(b, b_to_power_of_r, prime):
    """
    :param b: integer, which is the primitive root of the group
    :param b_to_power_of_r: which is b^r mod p, shared by the sender.
    :param prime: a prime number
    :return:
    brl, which (b^r)^l mod prime ;
    b_to_power_of_l, which is (b^l) mod prime ;
    brl_inverse, which is the inverse of brl in group U(prime)
    """
    # check the primality of the argument prime
    if not is_prime(prime):
        raise Exception(f"{prime} is not prime. Argument should be prime.")

    l = random.randint(0, prime - 2)  # generate a private key
    b_to_power_of_l = fast_expo_modulo(b, l,prime)
    # computes (b^r)^l
    brl = fast_expo_modulo(b_to_power_of_r, l,prime)
    # computes inverse of (b^r)^l in G
    brl_inverse = extended_euclidean_2(brl,prime)[0]
    return brl, b_to_power_of_l, brl_inverse


def el_gamal_encrypt(message, b_to_power_of_l, r,prime):
    """
    :param message: an integer , which represents the message to be encrypted.
    :param b_to_power_of_l: an integer, which is provided by the receiver
    :param r: an integer, which is generated in the preparation stage of the cipher
    :param prime: a prime number
    :return: integer
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

    :param cipher_text: integer
    :param brl_inverse: integer
    :param prime:  a prime integer
    :return: an integer
    """
    # check the primality of the argument prime
    if not is_prime(prime):
        raise Exception(f"{prime} is not prime. Argument should be prime.")

    plain_text = cipher_text * brl_inverse % prime
    return plain_text
