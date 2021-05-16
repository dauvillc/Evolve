"""
Defines the generic Cell class.
"""
from numpy.random import geometric


# Lifetime of all cell types
_cell_lifetimes = {'C': 1000,
                   'R': 20}


class Cell:
    """
    A Cell is the basic brick of any organism.
    There exist multiple types of cells. For each type, a subclass is created.
    """
    def __init__(self, organism):
        """
        -- organism: Organism containing this cell
        """
        self.organism = organism
        self.age = 0
        # The cell has a life expectancy L that depends on its type
        # defined in cell_types.py
        # The age at which the cell dies follows a geometric law of parameter
        # p = 1/L
        self.death_age = geometric(1 / _cell_lifetimes[self.get_typecode()])

    def update(self):
        """
        Updates the cell. This is different from function() as this method in common between
        all cells.
        Returns True iff the cell dies.
        """
        self.age += 1
        return self.age == self.death_age

    def function(self):
        """
        Function that should be called in the subclasses during the organism's functioning / update.
        This function can have any effect on the cell's organism, such as adding or removing resources,
        reproduction, movement, etc...
        """
        pass

    def get_typecode(self):
        """
        Returns the cell's type code as written in the CURDL code. For example, returns
        'R' for a respiratory cell.
        """
        return None


class CentralCell(Cell):
    """
    The Central cell is unique in each organism.
    -- It consumes N where N is the amount of cells in the organism.
    """
    def function(self):
        self.organism.remove_resource('O2', self.organism.number_of_cells())

    def get_typecode(self):
        return 'C'
