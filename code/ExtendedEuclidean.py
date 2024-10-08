# Write and test code that will find a couple of integers, x0 and y0 , for given
# integers m and n , such that x0 m + y0 n will yield the smallest positive number(gcd).
# This is, of course, the Extended Euclidean Algorithm.

from EuclideanAlgo import euclidean
def extended_euclidean(int1,int2):
    """
    using brute force
    :param num1: integer
    :param num2: integer
    :return: a tuple of integers (x,y), such that x*int1+y*int2 = gcd(int1,int2)
    """

    gcd = euclidean(int1,int2)

    start = -10000
    end = -start
    for i in range(start,end):
        for j in range(start,end):
            if i* int1 +j *int2 == gcd:
                return (i,j)


def extended_euclidean_2(num1,num2):
    """
    using extended euclidean
    :param num1: integer
    :param num2: integer
    :return: a tuple of integers (x,y), such that x*int1+y*int2 = gcd(int1,int2)
    """

    if num1 >= num2:
        big_num = num1
        small_num = num2
    else:
        big_num = num2
        small_num = num1

    if small_num == 0:
        return big_num, 0,1

    remainder = big_num % small_num
    quotient = big_num // small_num

    return euclidean(remainder,quotient)


