import math
from miller_rabin import miller_rabin_2
def is_prime(num):
    """
    check if the num is prime by miller rabin algorithm
    :return: true or false
    """
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    return miller_rabin_2(50,num)

