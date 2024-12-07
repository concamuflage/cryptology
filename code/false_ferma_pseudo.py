from fast_expo_modulo import fast_expo_modulo
from is_prime import is_prime


def false_fermat_pseudo(b, n):
    """
    test if a number is false fermat pseudoprime base b
    b: integer
    n: integer
    """

    if fast_expo_modulo(b,n-1,n) == 1: # if the number is a Fermat pseudoprime base b.
        if not is_prime(n): # but the number is not actually a prime number.
            return True
        return False
    return "Not a Fermat pseudo at all"

result = []
for n in range(2,10000):
    if false_fermat_pseudo(3,n):
        result.append(n)
# print(result)




