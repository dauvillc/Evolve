"""
Defines all types of cells.
"""
from cells.cell import Cell, CentralCell
from cells.respiratory import RespiratoryCell


# Dictionary mapping the codenames of cell types to their constructors
_cell_types = {'C': CentralCell,
               'R': RespiratoryCell}

# Lifetime of all cell types
_cell_lifetimes = {'C': 1000,
                   'R': 20}
