import numpy as np
from sympy import S

# fields

# we allow the user to either choose from custom finite fields, or preset infinite fields

#We implement the predefined infinite fields: N, Z, Q, R, and C

global Naturals, Integers, Rationals, Reals, Complexes
Naturals = S.Naturals
Integers = S.Integers
Rationals = S.Rationals
Reals = S.Reals
Complexes = S.Complexes


#Of course, the user could just implement these fields from Sympy directly; they're just defined here anyways to illustrate RepMat's functionality.

# Here we define the class finite fields

class create_Finite_Field:
    def __init__(self, prime_number):
        if not self.is_prime(prime_number):
            raise ValueError("p must be prime to form a finite field.")
        self.p = prime_number

    def add(self, a, b):
        return (a + b) % self.p

    def mul(self, a, b):
        return (a * b) % self.p

    def zero(self):
        return 0

    def one(self):
        return 1

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    global display_cfield_info
    def display_cfield_info(self):
        print(f"Group with elements: {self.elements}")
        print(f"Group operation: {self.operation}")
        print(f"Identity: {self.identity}")
        print(f"Inverses: {self.inverses}")



# custom vector spaces

class create_VSpace:
    def __init__(self, field, basis_vectors):
        self.field = field
        self.basis_vectors = [np.array(v) for v in basis_vectors]

    def __repr__(self):
        return f"VSpace({self.basis_vectors})"
    
    def __iter__(self):
        return iter(self.basis_vectors)


    # checks for linear independence, vspace axioms and whether it is in the field
    
    def linear_indepedence_check(self):
        matrix = np.vstack(self.basis_vectors)
        if not np.linalg.det(matrix) == 0:
            raise ValueError("Basis vectors aren't linearly independent!")

    def dim(self):
        return len(self.basis_vectors)

    global display_vspace_info
    def display_vspace_info(self):
        if isinstance(self, VctSp):
            print(f"Vector space with bases: {self.basis_vectors} over the field {self.field}")
        else:
            raise ValueError("Input must be a valid vector space.")
        


# CREATION

def FiniteField(prime_number):
    return create_Finite_Field(prime_number)

def VctSp(field, basis_vectors):
    return create_VSpace(field, basis_vectors)

def Z(n):
    integer_bases = np.eye(n, dtype=int)
    return create_VSpace(Integers, integer_bases)

def R(n):
    real_bases = np.eye(n)
    return create_VSpace(Reals, real_bases)
def C(n):
    complex_bases = np.eye(n, dtype=complex)
    return create_VSpace(Complexes, complex_bases)


# DISPLAY & RECALL

def DisplayF(field):
    if isinstance(field, create_Finite_Field):
        return display_cfield_info(field)
    elif field == Naturals or Integers or Rationals or Reals or Complexes:
        print(f"Standard Field")
    else:
        raise ValueError("Input must be a valid field.")

def DisplayV(vspace):
    return display_vspace_info(vspace)

def dim(vspace):
    return dim(vspace)
