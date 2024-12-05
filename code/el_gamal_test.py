import random
import unittest
from el_gamal import el_gamal_decrypt, el_gamal_encrypt, el_gamal_sender_prepare, el_gamal_receiver_prepare
from generate_large_prime import generate_large_prime


class MyTestCase(unittest.TestCase):
    """
    testing all functions used in el gamal
    """

    def test1(self):
        """
        testing if encryption works as expected.
        """

        prime_length = 20  #  for 15 runs, fast, for 20, runs 30 seconds.
        prime = generate_large_prime(prime_length) # the prime agreed upon

        for index in range(1):
            # sender prepare and send publish b and b^r
            r,b,b_to_power_of_r =el_gamal_sender_prepare(prime)

            # receiver prepare and compute b^l and the inverse of (b^r)^l in group U(prime)
            brl, b_to_power_of_l, brl_inverse = el_gamal_receiver_prepare(b,b_to_power_of_r,prime)

            # generate a plain text in U(prime)
            message = random.randint(1,prime-1)
            cipher_text = el_gamal_encrypt(message,b_to_power_of_l,r,prime)
            plain_text = el_gamal_decrypt(cipher_text,brl_inverse,prime)
            self.assertEqual(message,plain_text)

    # def test2(self):
    #     """
    #     testing specific cases
    #     """
    #     prime_length = 20  # 20 bit runs well.
    #     prime = generate_large_prime(prime_length)  # the prime agreed upon
    #
    #     # sender prepare and send publish b and b^r
    #     r,b,b_to_power_of_r =el_gamal_sender_prepare(prime)
    #
    #     # receiver prepare and compute b^l and the inverse of (b^r)^l in group U(prime)
    #
    #     brl,b_to_power_of_l, brl_inverse = el_gamal_receiver_prepare(b,b_to_power_of_r,prime)
    #     # generate a plain text in U(prime)
    #     message = random.randint(1, prime - 1)
    #     cipher_text = el_gamal_encrypt(message,b_to_power_of_l,r,prime)
    #     plain_text = el_gamal_decrypt(cipher_text,brl_inverse,prime)
    #     self.assertEqual(message,plain_text)






















    
    
    
