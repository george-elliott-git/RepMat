import numpy as np
import sys
sys.path.append(r'D:\RepMatProject')
from .vspaces import dim
from .groups import GroupElements


# representation.py

# allows the user to create representations for standard or custom groups

#checks whether custom matrices fit the definition of a representation on the group

class create_Rep:
    def __init__(self, group, matrices, vspace):
        self.group = group
        self.elements = GroupElements(group)
        self.vspace = vspace
        self.matrices = matrices
        self.reps = {}
        self.em_dictionary = zip(self.elements, self.matrices)
        self.display_list = list(zip(self.elements, self.matrices))

        if len(self.matrices) != len(self.elements):
            raise ValueError("Number of matrices must match number of group elements.")

        
        for element, matrix in self.em_dictionary:
                if matrix.shape != (vspace.dim(), vspace.dim()):
                    raise ValueError(f"Matrix for '{element}' must be of shape ({vspace.dim()}, {vspace.dim()})")
                self.reps[element] = matrix


    #DISPLAY & RECALL FUNCTIONS

    def display_rep_info(self):
            print(f"Representation has dict: {self.display_list}") #include more/neaten up

    def get_RepElements(self, rep, i):
            print self.display_list[i]



    def check_homomorphism(self): #fix
            for g1 in self.group.elements:
                for g2 in self.group.elements:
                    lhs = np.dot(self.reps[g1], self.reps[g2])
                    rhs = self.reps[self.group.operation(g1, g2)]
                    if not np.allclose(lhs, rhs):
                        return False
            return True

    class IrreducibleRepresentation(Representation):
    def __init__(self, group_elements, matrix_representation):
        super().__init__(group_elements, matrix_representation)
        
    # Add methods specific to irreducible representations (if needed)

class Decomposition:
    def __init__(self, representation, irreps):
        self.representation = representation
        self.irreps = irreps
    
    def compute_decomposition(self):
        decomposition = {}
        for irrep in self.irreps:
            char_irrep = Character(irrep)
            decomposition[irrep] = 0
            for element in self.representation.group_elements:
                decomposition[irrep] += self.trace(element) * np.conj(char_irrep.trace(element))
            decomposition[irrep] /= len(self.representation.group_elements)
        return decomposition



# Here we define the utility functions that come with representations.py

#CREATION

def Rep(group, matrices, vspace):
    return create_Rep(group, matrices, vspace)

# DISPLAY & RECALL

def DisplayR(rep):
    return display_rep_info(rep)

def RepElements(rep, i):
    return get_RepElements(rep, i)
    
def is_homomorphism(rep_a, rep_b):
    return check_homomorphism()

def is_isomorphism(rep_a, rep_b):

def is_reducible(rep):
    # The approach here can vary; one simple method is checking for invariant subspaces
    for matrix in rep:
        eigenvalues, _ = np.linalg.eig(matrix)
        if np.allclose(eigenvalues, eigenvalues[0]):  # Simplified check for a reducible matrix
            return True
    return False

def is_decomposable(rep):
    # This would require more sophisticated checks based on splitting the space into direct sums
    # A simple approach could be to try checking for invariant subspaces.
    for matrix in rep_matrix:
        if np.linalg.matrix_rank(matrix) < matrix.shape[0]:  # Check if matrix has non-trivial kernel
            return True
    return False
