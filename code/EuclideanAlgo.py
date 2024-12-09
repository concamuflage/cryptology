import math

from fast_exponentiation import fast_exponentiation

# steins function implementation is provided by Chatgpt

def euclidean(num1 , num2):
    """
    this function uses Euclidean algorithms to compute gcd of two given numbers.
    :param num1: an integer
    :param num2: an integer
    :return: an integer, which is the gcd of num1 and num 2
    """
    if num1 >= num2:
        big_num = num1
        small_num = num2
    else:
        big_num = num2
        small_num = num1

    if small_num == 0:
        return big_num

    remainder = big_num % small_num
    return euclidean(small_num,remainder)

def steins(num1,num2):
    """
    use stein's method

    :param num1: int
    :param num2: int
    :return: gcd
    """
    # Base cases
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1

    # Find the greatest power of 2 dividing both numbers
    k = 0
    while ((num1 | num2) & 1) == 0:  # Both num1 and num2 are even
        num1 >>= 1
        num2 >>= 1
        k += 1

    # Make num1 odd
    while (num1 & 1) == 0:
        num1 >>= 1

    while num2 != 0:
        # Make num2 odd
        while (num2 & 1) == 0:
            num2 >>= 1

        # Swap if necessary to ensure num1 <= num2
        if num1 > num2:
            num1, num2 = num2, num1

        # Subtract smaller from larger
        num2 -= num1

    # Restore the common factor of 2
    return num1 << k


# if __name__ == "__main__":
#     print("result",euclidean(5417,5588))







