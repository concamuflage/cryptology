import unittest
from blum_blum_shub import blum_blum_shub
class MyTestClass(unittest.TestCase):

    """for testing blum_blum_shub function"""
    def test1(self):
        """testing length """
        for index in range(100):
            result = blum_blum_shub(index)
            self.assertEqual(len(result), index)
            print(result)
