#groups.py

# allows the user to create custom or 'standard' groups

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

    def group_check(self):
        return bool(self.identity) and len(self.inverses) == len(self.elements)

    # DISPLAY FUNCTION

    def display_group_info(self):
        print(f"Group with elements: {self.elements}")
        print(f"Group operation: {self.operation}")
        print(f"Identity: {self.identity}")
        print(f"Inverses: {self.inverses}")



#standard groups
#cyclic, symmetric, alternating, dihedral, modulo n, klein-four, quaternion


class create_Cyclic:
    def __init__(self, elements):
        self.elements = set(elements)


    def operation(self, a, b):
        return (a + b) % len(self.elements)

    def __call__(self, value):
        return value % len(self.elements)

    def __str__(self):
        return f"C{len(self.elements)}"


class create_Perm:
    def __init__(self, no_of_elements):
        self.no_of_elements = no_of_elements
    

def Perm(no_of_element):
    if no_of_elements.is_digit() and no_of_elements > 0:
        return create_Perm_Group(no_of_element)
    else:
        print("Not a valid number of elements!")


# Here we define the utility functions that come with groups.py


# CREATION

def Group(elements, operation):
    return create_Group(elements, operation)

def Cyclic(elements):
    return create_Cyclic(elements)

# DISPLAY & RECALL

def DisplayG(group):
    return display_group_info(group)
    

def GroupElements(group):
    return group.elements

def Order(group): # returns group order
    return len(group.elements)

def Optn(group): # returns groups operation
    return group.operation

def Identity(group):# returns identity element
    return group.identity

def Inverse(group): # returns array of group elements with their corresponding inverses
    return group.inverses


