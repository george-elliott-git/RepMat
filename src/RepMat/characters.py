# characters.py

# generate character table
# orthogonality of rows/columns Orth(representatation, i, j)
# inner products

import numpy as np
from tabulate import tabulate
from .representations import create_Rep, is_reducible

class Character:
    def __init__(self, rep):
        self.rep = rep

    global trace
    def trace(self, rep, i):
        matrix = (self.rep, i).RepElements.representations()
        return np.trace(matrix)
    
    global character_table
    def character_table(self):
        Conj_Classes = []
        Irreps_to_Chars = []
    
        
        
        for element in (self.rep).RepElements.representations():

            
        col_names = ["Conjugacy Class", "Class Representative"]
        #for i in ... append
        print(tabulate(data, headers=col_names, tablefmt="grid", showindex="always"))
            
            
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

def Char(rep, i):
    return trace(rep, i)

def Char_Table(rep):
    char_table = rep.character_table()
    
