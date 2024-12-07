import math

from fast_exponentiation import fast_exponentiation

a = 539704
n = 1000189

for b in range(20):
    val = fast_exponentiation(539704,math.factorial(b)) - 1
    gcd_val = math.gcd(val, n)
    # print(f"b = {b}: gcd(a^{b}! - 1, n) = {gcd_val}")