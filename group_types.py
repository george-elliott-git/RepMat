import sympy

# group types
#cyclic, symmetric, alternating, dihedral, modulo n, klein-four, quaternion

# defining cyclic group class

class create_Perm_Group:
    self.no_of_elements = no_of_elements
    

def perm_group(no_of_element):
    if no_of_elements.is_digit() and no_of_elements > 0:
        return create_Perm_Group(no_of_element)
    else:
        print("Not a valid number of elements!")
    
