# characters.py

# generate character table
# orthogonality of rows/columns Orth(representatation, i, j)
# inner products

import numpy as np
from tabulate import tabulate
import groups

from representations import create_Rep, is_reducible

class Character:
    def __init__(self, rep):
        self.rep = rep

    global trace
    def trace(self, rep, i):
        matrix = (self.rep, i).RepElements.representations()
        return np.trace(matrix)
    
    global character_table
    def character_table(self):
        # Identify Conjugates
        
        Conj_Class = groups.Conj_Classes(self.rep)
        #Identify Irreducible Representations
        Irreps = []
        for element in (self.rep).RepElements.representations():
            if representations.is_reducible(element) is True:
                Irreps.append(element)
            else:
                pass
    
        character_values = []
        for i in Irreps:    
            values = list(map(int, trace(i)).split())
            character_values.append(values)

        # Define the irreducible representations
        representations = [f"χ{i+1}" for i in (self.rep).RepElements.representations()]

        # Create table headers
        headers = ['Class'] + Conj_Class
            #Create Character Table
        table_data = [headers]
        for i, rep in enumerate(Irreps):
            row = [rep] + character_values[i]
            table_data.append(row)

        # Print the table
        print("\nCharacter Table:")
        print(tabulate(table_data, headers='firstrow', tablefmt='grid'))
            #Check with Orthogonality Relations
        
            
            
    

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
    char_table = character_table()
    
