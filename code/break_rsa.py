import random
from ExtendedEuclidean import extended_euclidean_2
from generate_large_prime import generate_large_prime
from pollard_p_1_factorization_factorial_version import pollard_p_1_factorization_factorial_version
from pollard_p_1_factorization_lecture_version import pollard_p_1_factorization_lecture_version,compute_factor_base
from pollard_rho_factorization import pollard_rho_factorization
from rsa_without_padding import *

def break_rsa_with_p_1_factorial(public_key,ciphertext):

    # factor n
    p = pollard_p_1_factorization_factorial_version(6,public_key[0])
    q = public_key[0] // p
    # find inverse of e in U(phi_of_n)
    phi_of_n = (p-1)*(q-1)
    e_inverse = extended_euclidean_2(public_key[1],phi_of_n)[0]
    private_key = (public_key[0],e_inverse)
    plaintext = rsa_decrypt(private_key,ciphertext)
    return plaintext


def break_rsa_with_pollard_rho(public_key, ciphertext):
    # factor n
    p = pollard_rho_factorization(public_key[0])
    q = public_key[0] // p
    # find inverse of e in U(phi_of_n)
    phi_of_n = (p - 1) * (q - 1)
    e_inverse = extended_euclidean_2(public_key[1], phi_of_n)[0]
    private_key = (public_key[0], e_inverse)
    plaintext = rsa_decrypt(private_key, ciphertext)
    return plaintext

def break_rsa_with_p_1_lecture_version(public_key, ciphertext):
    # factor n
    smoothness_bound = 200
    p = pollard_p_1_factorization_lecture_version(smoothness_bound,compute_factor_base(smoothness_bound),public_key[0])
    q = public_key[0] // p
    # find inverse of e in U(phi_of_n)
    phi_of_n = (p - 1) * (q - 1)
    e_inverse = extended_euclidean_2(public_key[1], phi_of_n)[0]
    private_key = (public_key[0], e_inverse)
    plaintext = rsa_decrypt(private_key, ciphertext)
    return plaintext

