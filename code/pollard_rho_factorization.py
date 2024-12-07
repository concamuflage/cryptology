from EuclideanAlgo import euclidean
from is_prime import is_prime

def pollard_rho_factorization(n):
    """
    for finding a non-trivial prime factor of a composite number n
    :param n: a composite number that is larger than 4
    :return: a prime factor of the composite number
    """
    # test if the argument is bigger than 3,leaving the trivial cases.
    if n < 4:
        raise Exception("The argument should be equal to or larger than 4")
    # test if the argument is composite
    if n % 2 == 0:
        return 2
    result = is_prime(n)
    if result:
        raise Exception("The argument is not composite")
    # try to factor it if it is composite
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
            if not is_prime(g):      # if the number is composite
                return pollard_rho_factorization(g)
            return g

if __name__ == "__main__":
    print(pollard_rho_factorization(210757))





