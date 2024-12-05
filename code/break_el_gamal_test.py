import unittest
import random

from break_el_gamal import break_el_gamal
from el_gamal import el_gamal_receiver_prepare, el_gamal_sender_prepare, el_gamal_encrypt, el_gamal_decrypt
from generate_large_prime import generate_large_prime


class MyTestClass(unittest.TestCase):
    """test break_el_gamal function"""

    def test1(self):
        """for specific case"""
        prime = 739351
        primitive_root = 7
        message = 534601
        cipher_text = 109922
        b_to_power_of_r = 142437
        b_to_power_of_l = 433568
        plain_text = break_el_gamal(cipher_text,prime,primitive_root,b_to_power_of_r,b_to_power_of_l)
        self.assertEqual(plain_text,message)

    def test(self):
        """for general cases"""

        prime_length = 30
        #  for 15 runs fast
        #  for 20, runs 30 seconds,
        #  for 25 bits, runs several minutes for a single loop.
        prime = generate_large_prime(prime_length) # the prime agreed upon

        for index in range(1):
            # sender prepare and send publish b and b^r
            r,b,b_to_power_of_r =el_gamal_sender_prepare(prime)

            # receiver prepare and compute b^l and the inverse of (b^r)^l in group U(prime)
            brl, b_to_power_of_l, brl_inverse = el_gamal_receiver_prepare(b,b_to_power_of_r,prime)

            # generate a plain text in U(prime)
            message = random.randint(1,prime-1)
            cipher_text = el_gamal_encrypt(message,b_to_power_of_l,r,prime)
            plain_text_1 = el_gamal_decrypt(cipher_text,brl_inverse,prime)
            plain_text_2 = break_el_gamal(cipher_text,prime,b,b_to_power_of_r,b_to_power_of_l)
            self.assertEqual(plain_text_1,plain_text_2)


