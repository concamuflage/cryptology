import unittest
from rsa_without_padding import rsa_enrypt,rsa_decrypt_without_private_key,rsa_private_key_generate_given_only_n,rsa_decrypt
from fast_expo_modulo import fast_expo_modulo

class MyTestCase(unittest.TestCase):

    def test(self):
        public_key = (210757,3)
        message = 12345
        ciphertext = rsa_enrypt(public_key,message)
        self.assertEqual(rsa_decrypt_without_private_key(public_key,ciphertext),message)
    def test(self):
        public_key = (15943, 3)
        private_key = rsa_private_key_generate_given_only_n(public_key)
        # test if the the private_key can decrypt a ciphertext.
        plaintext = 88
        ciphertext = rsa_enrypt(public_key,plaintext)
        recovered_plaintext = rsa_decrypt(private_key,ciphertext)
        self.assertEqual(plaintext,recovered_plaintext)

    def test(self):
        public_key = (12091,3)
        ciphertext = 9812
        plaintext = rsa_decrypt_without_private_key(public_key,ciphertext)
        new_ciphertext = rsa_enrypt(public_key,plaintext)
        self.assertEqual(ciphertext,new_ciphertext)










    
    
    
