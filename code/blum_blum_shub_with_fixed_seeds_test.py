import unittest
from blum_blum_shub_with_fixed_seeds import blum_blum_shub_with_fixed_seeds
from fast_expo_modulo import fast_expo_modulo


class MyTestClass(unittest.TestCase):

    """for testing blum_blum_shub_with_fixed_seeds function"""
    def test1(self):
        """testing length """
        p = 54959
        q = 33107
        n = p*q
        s0 = 1465162309
        s1 = fast_expo_modulo(s0,2,n)
        s2 = fast_expo_modulo(s1,2,n)
        list = [s0%2,s1%2,s2%2]
        self.assertEqual(blum_blum_shub_with_fixed_seeds(3),list)

















