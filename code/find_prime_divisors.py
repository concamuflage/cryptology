
from is_prime import is_prime
from pollard_rho_factorization import pollard_rho_factorization


def find_prime_divisors_helper(int_num):
    """
    for finding all the prime divisors of int_num using Pollard's rho method
    :param int_num: an int
    :return: a list of prime divisors of int_num
    """

    prime_divisor = pollard_rho_factorization(int_num)
    factor = int_num // prime_divisor
    if is_prime(factor):
        return [prime_divisor,factor]
    else:
        return find_prime_divisors_helper(factor) + [prime_divisor]

def find_prime_divisors(int_num):
    """
    for finding all the prime divisors of int_num using Pollard's rho method
    :param int_num: an int
    :return: a list of prime divisors of int_num
    """
    # if the argument is prime
    if is_prime(int_num):
        return {int_num}
    # if the argument is not a prime, try to find a prime divisor
    result = find_prime_divisors_helper(int_num)
    result_set = set(result)
    return result_set



# if __name__ == "__main__":
#     print(find_prime_divisors(516114709710473))