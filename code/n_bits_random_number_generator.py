from blum_blum_shub import blum_blum_shub

def n_bits_random_number_generator(n):
    """
    for generating an n_bit long random number, with n > 0
    :param n, an integer
    :return: an n-bit random decimal number
    """
    if n <= 0:
        raise ValueError("n must not be less than 1")
    bit_sequence = blum_blum_shub(n)
    while bit_sequence[0] !=1:
        bit_sequence = blum_blum_shub(n)
    binary_string = ''.join(map(str, bit_sequence))
    decimal_number = int(binary_string, 2)
    return decimal_number

