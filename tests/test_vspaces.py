# test_vspaces.py

import unittest

# Here we test some: CUSTOM FINITE FIELDS, INFINITE FIELDS, CUSTOM & STANDARD VSPACES

import RepMat

# CUSTOM FINITE FIELDS

class test_finite_fields(unittest.TestCase):
    def setUp(self):
        self.test_set = [3, 5, 7, 11]

    def test_ffields(self):
        vspace = RepMat.vspaces.Z(j)
        for j in range(1, 10):
            for i in self.test_set: 
                RepMat.VctSp(RepMat.FiniteField(i), vspace)
            
if __name__ == '__main__':
    unittest.main()

