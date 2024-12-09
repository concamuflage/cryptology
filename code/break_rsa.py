import random
from ExtendedEuclidean import extended_euclidean_2
from pollard_p_1_factorization_factorial_version import pollard_p_1_factorization_factorial_version
from pollard_p_1_factorization_lecture_version import pollard_p_1_factorization_lecture_version,compute_factor_base
from pollard_rho_factorization import pollard_rho_factorization
from rsa_without_padding import *

def break_rsa_with_pollard_rho(public_key, ciphertext):
    """
    break rsa ciphertext with Pollard's rho method.
    :param public_key: a tuple of integers, that is, (n,e)
    :param ciphertext: an integer
    :return: an integer
    """
    # factor n
    p = pollard_rho_factorization(public_key[0])
    q = public_key[0] // p
    # find inverse of e in U(phi_of_n)
    phi_of_n = (p - 1) * (q - 1)
    e_inverse = extended_euclidean_2(public_key[1], phi_of_n)[0]
    private_key = (public_key[0], e_inverse)
    plaintext = rsa_decrypt(private_key, ciphertext)
    return plaintext

def break_rsa_with_p_1_factorial(public_key,ciphertext):
    """
    break rsa ciphertext with Pollard's p-1 method(B! version).
    :param public_key: a tuple of integers, that is, (n,e)
    :param ciphertext: an integer
    :return: an integer
    """
    # factor n
    p = pollard_p_1_factorization_factorial_version(6,public_key[0])
    q = public_key[0] // p
    # find inverse of e in U(phi_of_n)
    phi_of_n = (p-1)*(q-1)
    e_inverse = extended_euclidean_2(public_key[1],phi_of_n)[0]
    private_key = (public_key[0],e_inverse)
    plaintext = rsa_decrypt(private_key,ciphertext)
    return plaintext


def break_rsa_with_p_1_lecture_version(public_key, ciphertext):

    """
    break rsa ciphertext with Pollard's p-1 method(textbook version).
    :param public_key: a tuple of integers, that is, (n,e)
    :param ciphertext: an integer
    :return: an integer
    """


    # factor n
    smoothness_bound = 1000
    p = pollard_p_1_factorization_lecture_version(smoothness_bound,compute_factor_base(smoothness_bound),public_key[0])
    q = public_key[0] // p
    # find inverse of e in U(phi_of_n)
    phi_of_n = (p - 1) * (q - 1)
    e_inverse = extended_euclidean_2(public_key[1], phi_of_n)[0]
    private_key = (public_key[0], e_inverse)
    plaintext = rsa_decrypt(private_key, ciphertext)
    return plaintext

if __name__=="__main__":
    print(break_rsa_with_pollard_rho((6759017329, 65537),1837778071))
