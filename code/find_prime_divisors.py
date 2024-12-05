
from is_prime import is_prime
def find_prime_divisors(int_num):
    """
    using brute force approach
    :param int_num: an int
    :return: a list of prime divisors of int_num
    """
    prime_divisors = []
    for int in range(2, int_num+1):
        if int_num % int == 0 and is_prime(int): # if int divides int_num and int is also prime
            prime_divisors.append(int)
    return prime_divisors
if __name__ == "__main__":
    print(find_prime_divisors(20635128451))