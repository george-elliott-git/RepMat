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

    def display_group_info(self):
        print(f"Group with elements: {self.elements}")
        print(f"Group operation: {self.operation}")
        print(f"Identity: {self.identity}")
        print(f"Inverses: {self.inverses}")

# STANDARD GROUP CLASSES [CYCLIC, SYMMETRIC, ALTERNATING,
    #DIHEDRAL all require a parameter n which is the order of the group.
    #The KLEIN-4 and QUATERNION groups are entirely preset.]

class create_Cyclic:
    def __init__(self, elements):
        self.elements = set(elements)

    def operation(self, a, b):
        return (a + b) % len(self.elements)

    def __call__(self, value):
        return value % len(self.elements)

    def __str__(self):
        return f"C{len(self.elements)}"

class create_Sym:
    def __init__(self, elements):
        self.elements = list(elements)
        # Generate all possible permutations of the set
        self.permutations = list(itertools.permutations(self.elements))

    def operation(self, perm_a, perm_b):
        # Composition of two permutations: apply perm_b first, then perm_a
        return tuple(perm_a[perm_b[i]] for i in range(len(self.elements)))

    def __call__(self, value):
        # Apply the identity permutation (no change)
        return value

    def __str__(self):
        # Represent the symmetric group as S_n, where n is the number of elements
        return f"S{len(self.elements)}"

    def apply_permutation(self, perm, element):
        # Apply a permutation to an element
        return perm[element]
    
    def get_permutations(self):
        # Return all permutations of the group
        return self.permutations

class create_Alt:
    def __init__(self, elements):
        self.n = len(elements)
        self.symmetric_group = create_Sym(n)
        self.group = [perm for perm in self.symmetric_group.group if perm.is_even()]

    def __repr__(self):
        return f"create_Alt(A_{self.n}) with {len(self.group)} elements"

    def compose(self, p1, p2):
        """Compose two permutations from the group."""
        return p1.compose(p2)

    def is_identity(self, perm):
        """Check if the permutation is the identity permutation."""
        return perm.perm == list(range(1, self.n + 1))



class create_DihedralGroup:
    def __init__(self, n):
        # n is the order of the group (number of rotations)
        self.n = n
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
        return create_Cyclic(elements)

def Sym(elements_or_order):
    if isinstance(elements_or_order, int):
        create_Sym(

                self.elements = list(range(elements_or_order))
    else:
        # Otherwise, treat the input as a custom set of elements
        self.elements = list(elements_or_n)

def Alt(elements):
    return create_Alt(elements)

def Dihe(elements):
    return create_Dihe(elements)

def K4():
    return create_K4()

def Quat():
    return create_Quat()

# DISPLAY & RECALL

def DisplayG(group):
    return display_group_info(group)
    
def GroupElements(group, i): #returns array (or ith) group element
    return group.elements

def Order(group): # returns group order
    return len(group.elements)

def Optn(group): # returns groups operation
    return group.operation

def Identity(group):# returns identity element
    return group.identity

def Inverse(group, i): # returns array (or ith) of group elements with their corresponding inverses
    return group.inverses
