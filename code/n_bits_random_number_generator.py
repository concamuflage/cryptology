

from blum_blum_shub import blum_blum_shub

def n_bits_random_number_generator(n):
    """
    for generating a n_bit random number
    :param n, integer
    :return: a n-bit random decimal number
    """
    decimal_number = 1
    while decimal_number.bit_length() !=n:
        bit_sequence = blum_blum_shub(n)
        binary_string = ''.join(map(str, bit_sequence))
        decimal_number = int(binary_string, 2)
    return decimal_number

