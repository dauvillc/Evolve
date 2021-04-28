"""
Defines all types of cells.
"""
from cells.cell import Cell, CentralCell
from cells.respiratory import RespiratoryCell


# Dictionary mapping the codenames of cell types to their constructors
_cell_types = {'C': CentralCell,
               'R': RespiratoryCell}
