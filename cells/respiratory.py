"""
Defines the respiratory cell
"""
from cells.cell import Cell


class RespiratoryCell(Cell):
    """
    The respiratory cell brings to its organism 3.5 dioxygen units per unit of time.
    """
    def function(self, organism):
        organism.add_resource("O2", 3.5)
