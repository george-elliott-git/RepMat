# representation.py

import numpy as np

class GroupRepresentation:
    def __init__(self, group, dimension):
        self.group = group
        self.dimension = dimension
        self.representation = {}

    def add_representation(self, element, matrix):
        if element not in self.group.elements:
            raise ValueError(f"Element {element} is not part of the group")
        self.representation[element] = matrix

    def get_representation(self, element):
        """Get the matrix representation of a group element."""
        return self.representation.get(element, None)

    def check_homomorphism(self):
        """Check if the representation satisfies the homomorphism property."""
        for g1 in self.group.elements:
            for g2 in self.group.elements:
                lhs = np.dot(self.representation[g1], self.representation[g2])
                rhs = self.representation[self.group.operation(g1, g2)]
                if not np.allclose(lhs, rhs):
                    return False
        return True
