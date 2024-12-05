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
    using extended euclidean to find (x,y), with x > 0, such that x*int1+y*int2 = gcd(int1,int2) and

    :param num1: integer, num1 must be smaller than num2
    :param num2: integer
    :return: a tuple of integers (x,y), such that x*int1+y*int2 = gcd(int1,int2)
    """

    if num1 > num2:
        raise Exception("num1 must be smaller than num2")

    result = extended_euclidean_2_helper(num1,num2)
    # if inverse is negative, convert it into a positive.
    if result[1] < 0:
        result[1] += num2
        result[2] -= num1
    return (result[1],result[2])

def extended_euclidean_2_helper(num1,num2):

    """using Diophantine equation to
    :param num1: integer, must be smaller than num2
    :param num2: integer
    :return: a tuple of integers (x,y), such that x*int1+y*int2 = gcd(int1,int2)
    """
    if num1 == 0:
        return num2, 0, 1

    gcd, x1, y1 = extended_euclidean_2_helper(num2%num1,num1)

    # the following formulas are from Diophantine equations
    # for detailed explanation, please check README or check out Diophantine equations.

    x = y1 - (num2//num1)*x1
    y = x1

    list = [gcd,x,y]
    return list

if __name__ == "__main__":
    print(extended_euclidean_2(5417,5588))





