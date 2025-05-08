#groups.py

import itertools

# RepMat allows the user to create custom or 'standard' groups.

# CUSTOM GROUP CLASS

class create_Group:
    def __init__(self, elements, operation):
        # By definition of a group, we require an identity, an inverse, and group associativity
        self.elements = set(elements)
        self.operation = operation

        # Check if closure holds
        self.check_closure()
        
        # Check for identity and inverses
        self.identity = self.find_identity()
        self.inverses = self.find_inverses()

    # Here we define the constituent functions which form the group_check() function.

    def check_closure(self):
        for x in self.elements:
            for y in self.elements:
                if self.operation(x, y) not in self.elements:
                    raise ValueError("Closure property does not hold!")

    def find_identity(self):
        for e in self.elements:
            if all(self.operation(e, x) == x and self.operation(x, e) == x for x in self.elements):
                return e
        raise ValueError("No identity element found!")

    def find_inverses(self):
        inverses = {}
        for x in self.elements:
            for y in self.elements:
                if self.operation(x, y) == self.identity and self.operation(y, x) == self.identity:
                    inverses[x] = y
                    break
            else:
                raise ValueError(f"No inverse found for value {x}")
        return inverses

    # The group_check() function is vital for ensuring custom groups satisfies the group axioms.
    
    def group_check(self): 
        return bool(self.identity) and len(self.inverses) == len(self.elements)

    # DISPLAY FUNCTION

    global display_group_info
    def display_group_info(self):
        if isinstance(self, create_Group):
            print(f"Group with elements: {self.elements}")
            print(f"Group operation: {self.operation}")
            print(f"Identity: {self.identity}")
            print(f"Inverses: {self.inverses}")
        elif isinstance(self, create_Cyclic or create_Sym):
            print(f"Group of class: {isinstance.__class__.__base__}")
            print(f"Group with elements: {self.elements}")
            print(f"Group operation: {self.operation}")

# STANDARD GROUP CLASSES [CYCLIC, SYMMETRIC, ALTERNATING,
    #DIHEDRAL all require a parameter n which is the order of the group.
    #The KLEIN-4 and QUATERNION groups are entirely preset.]

# CYCLIC GROUPS

class create_Cyclic:
    def __init__(self, elements):
        self.elements = set(elements)

    def operation(self, a, b):
        return (a + b) % len(self.elements)

    def __call__(self, value):
        return value % len(self.elements)

    def __str__(self):
       return f"C{len(self.elements)}"

# SYMMETRIC GROUPS

class create_Sym:
    def __init__(self, elements):
        # Convert the elements to a sorted list if they are a set, to ensure consistent ordering
        self.elements = list(sorted(elements)) if isinstance(elements, set) else list(elements)
        # Generate all permutations of the elements
        self.permutations = list(itertools.permutations(self.elements))

    def operation(self, perm_a, perm_b):
        # Ensure the permutations are valid (of the same length as self.elements)
        if len(perm_a) != len(self.elements) or len(perm_b) != len(self.elements):
            raise ValueError("Permutations must have the same length as the number of elements")
        
        # Perform the operation: perm_a applied on perm_b
        return tuple(perm_a[perm_b[i]] for i in range(len(self.elements)))

    def __str__(self):
        # String representation of the symmetric group based on its size
        return f"S{len(self.elements)}"

    def apply_permutation(self, perm, element):
        # Apply the permutation to a specific element (indexing into the permutation)
        return perm[element]
    
    def get_permutations(self):
        # Return the list of all permutations
        return self.permutations

# ALTERNATING GROUPS

class create_Alt(create_Sym):  # Inherit from create_Sym
    def __init__(self, elements):
        # Initialize the symmetric group first
        super().__init__(elements)
        # Filter even permutations for the alternating group
        self.alt_permutations = [perm for perm in self.permutations if self.is_even(perm)]

    def is_even(self, perm):
        """Check if a permutation is even by counting inversions."""
        inversions = sum(1 for i in range(len(perm)) for j in range(i + 1, len(perm)) if perm[i] > perm[j])
        return inversions % 2 == 0

    def get_permutations(self):
        """Return only the even permutations (alternating group)."""
        return self.alt_permutations

    def __str__(self):
        """String representation of the alternating group."""
        return f"A{len(self.elements)}"

# DIHEDRAL GROUPS

class create_Dihe:
    def __init__(self, n):
        self.n = len(n)
        self.elements = self.generate_elements()
        
    def generate_elements(self):
        # Generate the elements of the Dihedral group D_n
        elements = ['e']  # Identity element
        # Generate rotations r, r^2, ..., r^(n-1)
        for i in range(1, self.n):
            elements.append(f"r^{i}")
        # Generate reflections s, sr, sr^2, ..., sr^(n-1)
        for i in range(self.n):
            elements.append(f"s * r^{i}")
        return elements
    
    def operation(self, a, b):
        # Define the multiplication rules for D_n
        if a == 'e':
            return b
        if b == 'e':
            return a
        
        # Handle rotation products: r^i * r^j = r^(i + j) (mod n)
        if a.startswith('r') and b.startswith('r'):
            i = int(a[2:])
            j = int(b[2:])
            return f"r^{(i + j) % self.n}"
        
        # Handle the reflection products: s * r^i * s = r^(-i)
        if a.startswith('s') and b.startswith('r'):
            i = int(b[4:])
            return f"s * r^{(self.n - i) % self.n}"
        
        if a.startswith('r') and b.startswith('s'):
            i = int(a[2:])
            return f"s * r^{(self.n - i) % self.n}"
        
        # Handle the reflection product: s * s = e
        if a.startswith('s') and b.startswith('s'):
            return 'e'

    def __call__(self, value):
        # Apply identity to any value
        if value == 'e':
            return 'e'
        return value

    def __str__(self):
        # Represent the group as D_n (Dihedral Group)
        return f"Dihedral Group D_{self.n} with elements: {', '.join(self.elements)}"

    def get_elements(self):
        return self.elements

# KLEIN-4 GROUPS

class create_K4:
    def __init__(self):
        # Define the elements of the Klein Four group V_4
        self.elements = ['e', 'a', 'b', 'ab']

    def operation(self, a, b):
        # Define the multiplication rules for V_4 based on the group properties
        if a == 'e':
            return b
        if b == 'e':
            return a
        if a == b:
            return 'e'  # a^2 = e and b^2 = e
        if a == 'a' and b == 'b' or a == 'b' and b == 'a':
            return 'ab'  # ab = ba

    def __call__(self, value):
        # If you want to apply the identity operation (or any specific operation)
        if value == 'e':
            return 'e'
        return value

    def __str__(self):
        # Represent the group as V_4 (Klein Four Group)
        return f"Klein Four Group V_4 with elements: {', '.join(self.elements)}"

    def get_elements(self):
        return self.elements

# QUARTERNION GROUPS

class create_Quat:
    def __init__(self):
        self.generators = ['i', 'j', 'k']
        self.elements = self.generate_elements()

    def generate_elements(self):
        elements = {'1', '-1'}
        
        # Generate the elements based on powers of i, j, k and their negatives
        for gen in self.generators:
            elements.add(gen)  # Add positive generators
            elements.add('-' + gen)  # Add negative generators

        # Now add products of generators
        for a in self.generators:
            for b in self.generators:
                if a != b:
                    elements.add(self.operation(a, b))

        return elements

    def operation(self, a, b):
        # Define how the generators combine based on their known rules
        if a == 'i' and b == 'j':
            return 'k'
        elif a == 'i' and b == 'k':
            return '-j'
        elif a == 'j' and b == 'i':
            return '-k'
        elif a == 'j' and b == 'k':
            return 'i'
        elif a == 'k' and b == 'i':
            return 'j'
        elif a == 'k' and b == 'j':
            return '-i'

        # Handle powers of i, j, k
        if a == b:
            return '-1'
        
        return None

    def __str__(self):
        return f"Quaternion Group Q_8 with elements: {', '.join(sorted(self.elements))}"

    def get_elements(self):
        return sorted(self.elements)


# Here we define the utility functions that come with groups.py


# CREATION

def Group(elements, operation):
    return create_Group(elements, operation)

def Cyclic(elements_or_order):
    if isinstance(elements_or_order, int):
        return create_Cyclic(range(elements_or_order))
    else:
        return create_Cyclic(elements_or_order)

def Sym(elements_or_order):
    if isinstance(elements_or_order, int) and elements_or_order >= 0:
        return create_Sym(list(range(elements_or_order + 1)))
    elif isinstance(elements_or_order, list):
        return create_Sym(elements_or_order)
    else:
        raise ValueError("Input must be a non-negative integer or list of custom objects.")

def Alt(elements_or_order):
    if isinstance(elements_or_order, int) and elements_or_order >= 0:
        return create_Alt(list(range(elements_or_order)))
    elif isinstance(elements_or_order, list):
        return create_Alt(elements_or_order)
    else:
        raise ValueError("Input must be a non-negative integer or list of custom objects.")


def Dihe(elements_or_order):
    if isinstance(elements_or_order, int) and elements_or_order >= 0:
        return create_Dihe(list(range(elements_or_order + 1)))
    elif isinstance(elements_or_order, list):
        return create_Dihe(elements_or_order)
    else:
        raise ValueError("Input must be a non-negative integer or list of custom objects.")

    
def K4():
    return create_K4()

def Quat():
    return create_Quat()

# DISPLAY & RECALL

def DisplayG(group):
    return display_group_info(group)
    
def GroupElements(group, i=None): #returns array (or ith) group element
    if i is None:
        return group.elements  # Return the entire list
    else:
        try:
            return group.elements[i]  # Return the element at index i
        except IndexError:
            return None  # Return None if index is out of range
    return group.elements

def Order(group): # returns group order
    return len(group.elements)

def Optn(group, a, b): # returns groups operation * s.t. a * b
    return group.operation(a, b)

def Identity(group):# returns identity element
    return group.identity

def Inverse(group, i): # returns array (or ith) of group elements with their corresponding inverses
    return group.inverses

def Conj_Class(group):
    conj_classes = []
    used_conj = set()  
    for g in GroupElements(group):
        conj_class = []  
        if g not in used_conjugates: 
            for h in GroupElements(group):
                conj = group.Optn(group, group.Optn(h, g), group.Inverse(h))
                conj_class.append(conj)
                used_conj.append(conj) 
            conj_classes.append(conj_class)  
    return conj_classes
