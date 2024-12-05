from EuclideanAlgo import euclidean
from miller_rabin import miller_rabin_2

def pollard_rho_factorization(n):
    """
    :param n: a composite number that is larger than 4
    :return: a prime factor of the composite number or None
    """
    # test if the argument is bigger than 4,leaving the trivial cases.
    if n < 4:
        raise Exception("The argument should be equal to or larger than 4")
    # test if the argument is composite
    result = miller_rabin_2(50,n)
    if result:
        raise Exception("The argument is not composite")
    seed = 2
    x = seed
    y = x**2+1
    while True:
        g = euclidean(abs(y-x),n)
        if g == n:
            seed += 1 # reinitialize by changing x
            x = seed
            y = x**2+1
            continue
        if g == 1:              # check the next pair of (x,y)
            x = (x**2 +1) % n
            y = ((y**2 +1)**2 + 1)% n
            continue
        if 1 < g or g < n:    # g is a divisor
            if g % 2 == 0:    # test if g is even because miller_rabin_2 can only analyse odd numbers
                return 2      # if g is even, we found a prime factor 2.
            if not miller_rabin_2(50,g):      # if the number is composite
                return pollard_rho_factorization(g)
            return g





