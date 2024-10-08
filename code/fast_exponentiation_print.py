def fast_exponentiation(root, power):
    """
    find the result of root to the power using fast exponentiation
    root:int
    power: int
    return an int
    """
    return fast_exponentiaion_helper(root, power, 1)


def fast_exponentiaion_helper(root, power, accumulator):
    print(root,power,accumulator)
    if power == 0:
        return accumulator
    if (power % 2 == 1):  # if the power is odd
        return fast_exponentiaion_helper(root, power - 1, root * accumulator)
    else:
        return fast_exponentiaion_helper(root * root, power // 2, accumulator)

fast_exponentiation(2,5)