import sympy
import random
import unittest


from ExtendedEuclidean import extended_euclidean_2
from break_rsa import break_rsa_with_p_1_factorial, break_rsa_with_pollard_rho, break_rsa_with_p_1_lecture_version
from fast_expo_modulo import fast_expo_modulo
from n_bits_random_prime_generator import n_bits_random_prime_generator
from rsa_without_padding import *


class MyTestCase(unittest.TestCase):

    prime_length = 13 # only break_rsa_with_pollard_rho() can break when p and q are about 45 bits.
    def test1(self):
        """break_rsa_with_p_1_factorial"""
        # generate p and q
        p = n_bits_random_prime_generator(MyTestCase.prime_length)
        q = n_bits_random_prime_generator(MyTestCase.prime_length)
        # receiver generates public key
        n = p * q
        phi_of_n = (p - 1)*(q - 1)
        e = 2
        while phi_of_n % e == 0:  # that is,  gcd(e,phi_of_n) = 1
            e = sympy.randprime(2, phi_of_n - 1)
        public_key = (n, e)
        # receiver generates private key
        private_key = rsa_private_key_generator(public_key, p, q)
        # sender generates the message
        message = random.randint(2, n - 1)  # 1<x<n
        while euclidean(message, n) != 1:
            message = random.randint(2, n - 1)
        # sender encrypt the message
        ciphertext = fast_expo_modulo(message,e,n)
        # receiver decrypt the message
        plaintext_1 = rsa_decrypt(private_key,ciphertext)
        # attacker decrypt the message
        plaintext_2 = break_rsa_with_p_1_factorial(public_key,ciphertext)
        self.assertEqual(plaintext_1,plaintext_2)

    def test2(self):
        """
        test break_rsa_with_pollard_rho() function
        """
        # generate p and q
        p = n_bits_random_prime_generator(MyTestCase.prime_length)
        q = n_bits_random_prime_generator(MyTestCase.prime_length)
        # receiver generates public key
        n = p * q
        phi_of_n = (p - 1) * (q - 1)
        e = 2
        while phi_of_n % e == 0:  # that is,  gcd(e,phi_of_n) = 1
            e = sympy.randprime(2, phi_of_n - 1)
        public_key = (n, e)
        # receiver generates private key
        private_key = rsa_private_key_generator(public_key, p, q)
        # sender generates the message
        message = random.randint(2, n - 1)  # 1<x<n
        while euclidean(message, n) != 1:
            message = random.randint(2, n - 1)
        # sender encrypt the message
        ciphertext = fast_expo_modulo(message, e, n)
        # receiver decrypt the message
        plaintext_1 = rsa_decrypt(private_key, ciphertext)
        plaintext_2 = break_rsa_with_pollard_rho(public_key, ciphertext)
        self.assertEqual(plaintext_1, plaintext_2)

    def test3(self):
        """
        test pollard_p_1_factorization_lecture_version function
        """
        # generate p and q
        p = n_bits_random_prime_generator(MyTestCase.prime_length)
        q = n_bits_random_prime_generator(MyTestCase.prime_length)
        # receiver generates public key
        n = p * q
        phi_of_n = (p - 1) * (q - 1)
        e = 2
        while phi_of_n % e == 0:  # that is,  gcd(e,phi_of_n) = 1
            e = sympy.randprime(2, phi_of_n - 1)
        public_key = (n, e)
        # receiver generates private key
        private_key = rsa_private_key_generator(public_key, p, q)
        # sender generates the message
        message = random.randint(2, n - 1)  # 1<x<n
        while euclidean(message, n) != 1:
            message = random.randint(2, n - 1)
        # sender encrypt the message
        ciphertext = fast_expo_modulo(message, e, n)
        # receiver decrypt the message
        plaintext_1 = rsa_decrypt(private_key, ciphertext)
        plaintext_2 = break_rsa_with_p_1_lecture_version(public_key, ciphertext)
        self.assertEqual(plaintext_1, plaintext_2)

