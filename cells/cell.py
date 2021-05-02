"""
Defines the generic Cell class.
"""


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

    def update(self):
        """
        Updates the cell. This is different from function() as this method in common between
        all cells.
        """
        self.age += 1

    def function(self):
        """
        Function that should be called in the subclasses during the organism's functioning / update.
        This function can have any effect on the cell's organism, such as adding or removing resources,
        reproduction, movement, etc...
        """
        pass


class CentralCell(Cell):
    """
    The Central cell is unique in each organism.
    -- It consumes N where N is the amount of cells in the organism.
    """
    def function(self):
        self.organism.remove_resource('O2', self.organism.number_of_cells())


