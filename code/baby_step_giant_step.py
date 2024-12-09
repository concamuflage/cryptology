import math

from primitive_root_search import primitive_root_search
from fast_expo_modulo import fast_expo_modulo
def baby_step_giant_step(base, target, prime_modulus):
    """
    Let r be a primitive root for  prime_modulus
    This function returns an x such that r^x = target % prime_modulus
    :return: an integer
    """

    primitive_root = base

    # compute some initial values
    group_order = prime_modulus-1
    m = math.ceil(math.sqrt(group_order))
    # compute primitive_root^-m mod prime_modulus
    # in practice, we compute primitive_root^(-m+group_order) mod prime_modulus)
    # (you can ask chatgpt to prove the equality. Mainly, the equality is proved using Euler's theorem
    #  and definition of an inverse)
    # because the following function accepts only positive exponent
    positive_power = group_order -m
    c = fast_expo_modulo(primitive_root,positive_power,prime_modulus) # c = b^(-m) mod p

    # baby step
    baby_results = {}
    for j in range(m):
        result = fast_expo_modulo(primitive_root,j,prime_modulus)
        baby_results[j] = result

    # giant step, this step can be integrated into the previous loop.
    # for logic clarity, we use a separate loop here.

    x = target
    for i in range(m):
        if x in baby_results.values():
            for key,value in baby_results.items(): # there is a match. let's find the corresponding j in the baby step.
                if value == x:
                    j = key
                    result = m * i + j
                    return result
        else:
            x = (x*c) % prime_modulus





