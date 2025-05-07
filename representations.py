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

    def get_Rep(self, element):
            #Get the matrix representation of a group element.
            return self.reps.get(element, None)

        
    
    # verifying custom choices fit the formal definition of a representation

    def check_homomorphism(self):
            for g1 in self.group.elements:
                for g2 in self.group.elements:
                    lhs = np.dot(self.reps[g1], self.reps[g2])
                    rhs = self.reps[self.group.operation(g1, g2)]
                    if not np.allclose(lhs, rhs):
                        return False
            return True


# Here we define the utility functions that come with representations.py

#CREATION

def Rep(group, matrices, vspace):
    return create_Rep(group, matrices, vspace)

# DISPLAY & RECALL

def DisplayR(rep):
    return display_rep_info(rep)
