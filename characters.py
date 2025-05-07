# characters.py

# character tables, trace, inner product


# character of a representation Char(representation, i)
# generate character table
# orthogonality of rows/columns Orth(representatation, i, j)
# inner products

import numpy as np

class Character:
    def __init__(self, rep):
        self.rep = rep

    def trace(self, element):
        matrix = (self.rep).RepElements.representations()
        return np.trace(matrix)
    
    def character_table(self):
        # Calculate the character table (trace for each group element)
        table = {}
        for element in (self.rep).RepElements.representations()
            table[element] = self.trace(element)
        return table

    def inner_product(self, other_character):
        # Assuming group G is finite and we have the size of the group |G|
        G = self.representation.group_elements
        inner_prod = 0
        for g in G:
            inner_prod += self.trace(g) * np.conj(other_character.trace(g))
        return inner_prod / len(G)


# DISPLAY & RECALL


def Char_Table(character):
    char_table = character.character_table()
    for elem, value in char_table.items():
        print(f"Character for element {elem}: {value}")
        
def Decomp(decomposition):
    for irrep, multiplicity in decomposition.items():
        print(f"Multiplicity of {irrep}: {multiplicity}")