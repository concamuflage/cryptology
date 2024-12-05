import math

from fast_exponentiation import fast_exponentiation


def euclidean(num1 , num2):
    """
    this function uses Euclidean algorithms to compute gcd of two given numbers.
    :param num1: integer
    :param num2: integer
    :return: gcd of num1 and num 2
    """
    if num1 >= num2:
        big_num = num1
        small_num = num2
    else:
        big_num = num2
        small_num = num1

    if small_num == 0:
        return big_num

    quotient = big_num // small_num
    remainder = big_num % small_num
    return euclidean(small_num,remainder)

def steins(num1,num2):
    """
    use stein's method
    :param num1: int
    :param num2: int
    :return: gcd
    """
    if num1 == num2:
        return num1
    # cover a special case that causes an infinite recursion since neither number is never reduced.

    if num1 == 0:
        return num2
    if num2 == 0:
        return num1


    if num1 >= num2:
        return steins(num1-num2,num2)
    else:
        return steins(num1,num2-num1)


if __name__ == "__main__":
    print("result",euclidean(5417,5588))







