import math


def is_prime(num):
    """
    check if the num is prime by brute force
    :return: true or false
    """
    if num == 2:
        return True
    num2 = math.ceil(math.sqrt(num))
    for i in range(2,num2+1):
        if num % i == 0:
            return False

    return True


