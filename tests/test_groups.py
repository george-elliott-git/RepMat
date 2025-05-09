# test_groups.py

# Here we test some: CUSTOM GROUPS, STANDARD GROUPS, GROUP OPERATIONS


import unittest

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
import RepMat
from RepMat import groups

# CUSTOM GROUPS (example)

class test_custom_groups(unittest.TestCase):
    def setUp(self):
        self.test_custom_set = {0, 1, 2, 3}
        self.test_custom_operation = lambda a, b: (a + b) % 4

    def test_custom_creation(self):
        custom_group = groups.Group(self.test_custom_set, self.test_custom_operation)
        self.assertIsInstance(custom_group, groups.create_Group)
        self.assertEqual(custom_group.elements, self.test_custom_set)
        self.assertEqual(custom_group.operation(3, 4), 3)
        print("CUSTOM EXAMPLE MOD4")
        RepMat.groups.DisplayG(custom_group)


# STANDARD GROUPS

class test_all_standards_groups(unittest.TestCase):
    def setUp(self):
        self.test_set = [0, 1, 2, 3]

    def test_standard_creation(self):
        for i in range(1, 10):
            RepMat.Cyclic(i)
            RepMat.Sym(i)
            RepMat.Alt(i)
            RepMat.Dihe(i)

        test_cyclic = RepMat.Cyclic(self.test_set)
        print("CYCLIC EXAMPLE MOD4")
        RepMat.groups.DisplayG(test_cyclic)

        test_symmetric = RepMat.Sym(self.test_set)
        print("SYMMETRIC EXAMPLE")
        RepMat.groups.DisplayG(test_symmetric)

        test_alternate = RepMat.Alt(self.test_set)
        print("ALTERNATE EXAMPLE")
        RepMat.groups.DisplayG(test_alternate)

        test_dihedral = RepMat.Dihe(self.test_set)
        print("DIHEDRAL EXAMPLE")
        RepMat.groups.DisplayG(test_dihedral)
        
if __name__ == '__main__':
    unittest.main()