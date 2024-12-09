import random
from fast_expo_modulo import fast_expo_modulo
from fast_exponentiation import fast_exponentiation


def miller_rabin(number_of_tests, odd_integer):
    """
    test if int is a prime number with the miller_rabin test.
    :param int: an odd integer
    :param int: an integer, representing the number of witnesses.
    :return: True if the integer is probably a prime;
            False if the integer is not a prime.
    """
    if odd_integer == 1:
        return False
    if odd_integer == 2:
        return True
    if odd_integer == 3:
        return True

    # ensure int is odd first.
    if odd_integer % 2 == 0:
        raise Exception("the argument should be an odd integer")
    # convert odd_integer-1 into the forma (2^r)*m
    r,m = convert(odd_integer-1)

    # test k randomly chosen integers b.
    # if any b fails the following test, then n is not a prime.
    # else odd_integer is a prime with probability 1 - (1/4)^k
    for int in range(number_of_tests):
        rand_int = random.randint(2,odd_integer-2)
        # check if 2^m = 1 mod n
        result = fast_expo_modulo(rand_int,m,odd_integer)
        if result == (1 % odd_integer): # if equal, b is a witness, check the next b.
            continue
        else:
            # test if  (b^m)^(2^i) = -1 mod n , with 0<=i< r-1
            # if there is any i such that the test passes, b is a witness. Continue to check the next b.
            # else, try the next i.
            target = -1 % odd_integer
            for index in range(r):
                exponent = fast_exponentiation(2,index)
                result2 = fast_expo_modulo(result, exponent,odd_integer)
                if result2 == target:
                    break
            else: # if none of the i works, then b is a witness to the compositeness of odd_integer.
                return False
    return True

def miller_rabin_2(number_of_tests, odd_integer):
    """
    test if int is a prime number with the miller_rabin test.
    the logic is slightly modified from the above one to increase computation inefficiency
    :param int: an odd integer
    :param int: an integer, representing the number of witnesses.
    :return: True if the integer is probably a prime;
            False if the integer is not a prime.
    """
    if odd_integer == 1:
        return False
    if odd_integer == 2:
        return True
    if odd_integer == 3:
        return True

    # ensure int is odd first.
    if odd_integer % 2 == 0:
        raise Exception("the argument should be an odd integer")
    # convert odd_integer-1 into the forma (2^r)*m
    r,m = convert(odd_integer-1)

    # test k randomly chosen integers b.
    # if any b fails the following test, then n is not a prime.
    # else odd_integer is a prime with probability 1 - (1/4)^k
    for int in range(number_of_tests):
        rand_int = random.randint(2,odd_integer-2)
        # check if 2^m = 1 mod n
        result = fast_expo_modulo(rand_int,m,odd_integer)
        if result == 1 % odd_integer: # if equal, b is a witness, check the next b.
            continue
        else:
            # test if  (b^m)^(2^i) = -1 mod n , with 0<=i< r-1
            # if there is any i such that the test passes, b is a witness. Continue to check the next b.
            # else, try the next i.
            target = -1 % odd_integer
            # the logic here is different from the first function.
            for index in range(r):
                if result == target:
                    break
                result = (result ** 2 ) % odd_integer
            else: # if none of the i works, then b is a witness to the compositeness of odd_integer.
                return False
    return True


def convert(even_int):
    """
    convert the even integer into the forma (2^r)*m, m is an odd number
    :param even_int: an even integer
    :return:a tuple of integers, that is, (r,m)
    """
    if even_int % 2 == 1:
        raise Exception("The argument should be an even number")
    r = 0
    while even_int % 2 == 0:
        r += 1
        even_int = even_int // 2
    m = even_int
    return (r,m)

# if __name__ == "__main__":
#     print(convert(1728))





