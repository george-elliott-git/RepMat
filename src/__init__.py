#RepMat/__init__.py
from .vspaces import FiniteField, VctSp, Reals
from .groups import Group, Cyclic, Sym, Alt, Dihe, K4, Quat, DisplayG, GroupElements, Order, Optn, Identity, Inverse, create_Group
from .representations import Rep, DisplayR, create_Rep
from .characters import Character
import numpy as np #doesnt import?
import sympy

__all__ = ['Character', 'FiniteField', 'VectorSpace', 'Group', 'Cyclic', 'Display', 'Order', 'Rep']

def Display(item):
    if isinstance(item, create_Group):
        return item.display_group_info()
    if isinstance(item, create_Rep):
        return item.display_rep_info()
    else:
        pass



  

