
from fast_expo_modulo import fast_expo_modulo
from find_prime_divisors import find_prime_divisors
from is_prime import is_prime


def primitive_root_search(prime_number):

    """
    return all primitive roots / generators in group U(prime_number)
    :param prime_number:
    :return: a list of primitives or an empty list.
    """
    if prime_number == 2:
        return [1]
    # test if the argument is prime
    if not is_prime(prime_number):
        raise Exception("Error: the number you passed in is not a prime number")

    group_order = prime_number-1
    # generates all the members of the group.

    group = []
    for int in range(1,prime_number):
        group.append(int)

    # find prime divisors of group_order
    prime_divisors = find_prime_divisors(group_order)

    # compute all possible values of group_order/p (p in prime_divisors)

    possible_exponents = []
    for number in prime_divisors:
        possible_exponents.append(group_order // number)

    # test if any value b in the group to any power x in  possible exponents meet our requirement.
    # our requirement: if for all x in possible_exponents, b^x is not congruent to 1 % p, b is rejected.
    primitive_roots = []
    for element in group:
        for power in possible_exponents:
            result = fast_expo_modulo(element, power, prime_number)
            if result == 1:
                break
        else:
            primitive_roots.append(element)

    return primitive_roots
# if __name__ =="__main__":
#     print(primitive_root_search(839731))





