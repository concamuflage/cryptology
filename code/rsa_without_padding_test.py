import unittest

from ExtendedEuclidean import extended_euclidean_2
from fast_expo_modulo import fast_expo_modulo
from pollard_rho_factorization import pollard_rho_factorization
from rsa_without_padding import rsa_enrypt, rsa_decrypt,rsa_private_key_generator

class MyTestCase(unittest.TestCase):

    def test(self):
        """testing rsa_enrypt """
        public_key = (210757,3)
        message = 12345
        ciphertext = rsa_enrypt(public_key,message)
        ciphertext_2 = fast_expo_modulo(message,public_key[1],public_key[0])
        self.assertEqual(ciphertext,ciphertext_2)
    def test2 (self):
        """
        testing rsa_decrypt
        """
        public_key = (210757, 3)
        message = 12345
        ciphertext = rsa_enrypt(public_key, message)
        # factor n
        p = pollard_rho_factorization(public_key[0])
        q = public_key[0] // p
        # find inverse of e in U(phi_of_n)
        phi_of_n = (p - 1) * (q - 1)
        e_inverse = extended_euclidean_2(public_key[1], phi_of_n)[0]
        private_key = (public_key[0], e_inverse)
        plaintext = rsa_decrypt(private_key,ciphertext)
        self.assertEqual(message,plaintext)
    def test3(self):
        """
        testing rsa_private_key_generator
        """
        p = 419
        q = 503
        public_key = (210757, 3)
        private_key = rsa_private_key_generator(public_key,p,q)
        phi_of_n = (p-1)*(q-1)
        product = public_key[1]*private_key[1]
        self.assertEqual( product % phi_of_n,1)

    def test4(self):
        """
        testing exceptions
        """
        public_key = (11,2)
        plaintext = 1
        self.assertRaises(Exception,rsa_enrypt,public_key,plaintext)
















    
    
    
