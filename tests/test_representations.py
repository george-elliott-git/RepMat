# test_representations.py

# Here we test: CUSTOM REPRESENTATIONS, REP. HOMOMORPHISMS, REP. IRREDUCIBILITY, WE ALSO TEST ALL THE FUNCTIONALITY IN CHARCTERS, HENCE THE ABSENCE OF THE TEST_CHARACTERS.PY

import unittest
import numpy as np

import RepMat
from RepMat import groups, representations, vspaces
from RepMat import groups, create_Group, Cyclic, Sym, Alt, Dihe, Optn
from RepMat import characters, Character, Char_Table

class test_custom_groups(unittest.TestCase):
    def setUp(self):
        self.test_custom_set = {0, 1, 2, 3}
        self.test_custom_operation = lambda a, b: (a + b) % 4

    def test_custom_reps(self):
        custom_group = groups.Group(self.test_custom_set, self.test_custom_operation)
        test_matrices = [np.array([[1, 0], [0, 1]]), np.array([[0, -1], [1, 0]]), np.array([[-1, 0], [0, -1]]), np.array([[0, 1], [-1, 0]])]  # 270-degree rotation matrix
        vspace = vspaces.R(1)
        global custom_rep
        custom_rep = representations.Rep(custom_group, test_matrices, vspace)
        
    def test_character_table(self):
        characters.Char(custom_rep)
        Char_Table(custom_rep)
        
if __name__ == '__main__':
    unittest.main()