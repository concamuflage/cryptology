import random

from blum_blum_shub import blum_blum_shub

def random_number_generator(start,end):
    """
    for generating a pseudorandom number in the range (start,end), including end points, with blum_blum_shub,
    :param n, an integer
    :return: an n-bit random decimal number
    """
    if start > end:
        raise ValueError("start should not be greater than end.")
    decimal_number = 0
    while decimal_number < start or decimal_number > end:
        bit_length = end.bit_length()
        bit_sequence = blum_blum_shub(bit_length)
        binary_string = ''.join(map(str, bit_sequence))
        decimal_number = int(binary_string, 2)
    return decimal_number

# if __name__ = "__main__":
#     print(result = random_number_generator(2,125638))
