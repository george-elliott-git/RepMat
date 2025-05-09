from .vspaces import dim, R
from .groups import GroupElements, create_Cyclic
import numpy as np

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

    global display_rep_info
    def display_rep_info(self):
            print(f"Representation has dict: {self.display_list}") #include more/neaten up

    global get_RepElements
    def get_RepElements(self, rep, i):
            return self.display_list[i]

    global check_homomorphism
    def check_homomorphism(self): #fix
            for g1 in self.group.elements:
                for g2 in self.group.elements:
                    lhs = np.dot(self.reps[g1], self.reps[g2])
                    rhs = self.reps[self.group.operation(g1, g2)]
                    if not np.allclose(lhs, rhs):
                        return False
            return True

    class IrreducibleRepresentation:
        def __init__(self, group_elements, matrix_representation):
            super().__init__(group_elements, matrix_representation)




# Here we define the utility functions that come with representations.py

#CREATION

def Rep(group, matrices, vspace):
    if isinstance(group, create_Cyclic):
        rep_matrices = []
        for k in range(group.n):
            angle = 2 * np.pi * k / group.n
            matrix = np.array([
                [np.cos(angle), -np.sin(angle)],
                [np.sin(angle),  np.cos(angle)]
            ])
        rep_matrices.append(matrix)
        return create_Rep(group, rep_matrices, R(1))

    else:
        return create_Rep(group, matrices, vspace)

# DISPLAY & RECALL

def DisplayR(rep):
    return display_rep_info(rep)

def RepElements(rep, i):
    return get_RepElements(rep, i)
    
def is_homomorphism(rep_a, rep_b):
    return check_homomorphism()

def is_reducible(rep):
    for matrix in rep:
        eigenvalues, _ = np.linalg.eig(matrix)
        if np.allclose(eigenvalues, eigenvalues[0]): 
            return True
    return False



