def fast_expo_modulo(base, power, modulus):
    """
    calculates base^power%modulus using fast exponentiation
    :param base: a positive int
    :param power: a positive int
    :param modulus: a positive int
    :return: an int
    """
    if power < 0:
        raise Exception("Error: power must be positive")
    # handle special case where power is already 0. No matter what the modulus is, the remainder is always 1:
    if power == 0:
        return 1 % modulus
    return fast_expo_modulo_helper(base,power,1,modulus)

def fast_expo_modulo_helper(base,power,accumulator, modulus):

    """
    This is a helper function to recursively calculate base^power%modulus
    :param base: int
    :param power: int
    :param accumulator: int
    :param modulus: int
    :return: base^power%modulus
    """

    if power == 0:
        return accumulator
    if power % 2 == 1:  # the power is odd
        return fast_expo_modulo_helper(base % modulus , power - 1 , base*accumulator % modulus,modulus)
    else:
        return fast_expo_modulo_helper(base*base % modulus , power // 2, accumulator,modulus)
if __name__ == "__main__":
    print(fast_expo_modulo(2,1729))

