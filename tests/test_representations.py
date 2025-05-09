# test_representations.py

# Here we test: CUSTOM REPRESENTATIONS, REP. HOMOMORPHISMS, REP. IRREDUCIBILITY/DECOMPOSABILITY

import unittest
import numpy as np

import RepMat
from RepMat import groups, representations, vspaces
from RepMat import groups, create_Group, Cyclic, Sym, Alt, Dihe, Optn

class test_custom_groups(unittest.TestCase):
    def setUp(self):
        self.test_custom_set = {0, 1, 2, 3}
        self.test_custom_operation = lambda a, b: (a + b) % 4

    def test_custom_reps(self):
        custom_group = groups.Group(self.test_custom_set, self.test_custom_operation)
        test_matrices = [np.array([[1, 0], [0, 1]]), np.array([[0, -1], [1, 0]]), np.array([[-1, 0], [0, -1]]), np.array([[0, 1], [-1, 0]])]  # 270-degree rotation matrix
        vspace = vspaces.R(1)
        custom_rep = representations.Rep(custom_group, test_matrices, vspace)
        
if __name__ == '__main__':
    unittest.main()