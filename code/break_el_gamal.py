from baby_step_giant_step import baby_step_giant_step
from fast_expo_modulo import fast_expo_modulo
from ExtendedEuclidean import extended_euclidean_2

def break_el_gamal(cipher_text, p,b, b_to_power_of_r,b_to_power_of_l):
    """
    a function for breaking ciphertext of El Gamal cipher
    :param cipher_text: integer
    :param p: a prime integer
    :param b: integer, primitive root of the group U(p)
    :param b_to_power_of_r: integer
    :param b_to_power_of_l: integer
    :return: integer
    """
    # to find l
    l = baby_step_giant_step(b,b_to_power_of_l,p)
    # compute (b^r)^l
    brl= fast_expo_modulo(b_to_power_of_r,l,p)
    brl_inverse = extended_euclidean_2(brl,p)[0]
    plain_text = cipher_text* brl_inverse % p
    return plain_text







