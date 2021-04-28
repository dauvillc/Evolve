"""
Defines the Organism class.
"""
from curdl import CURDL_code
from resources import ResourcesStock
from cells.cell import CentralCell
from cells.cell_types import _cell_types


class Organism:
    """
    An organism is a set of cells organised in a 2D grid by its CURDL code, and capable of
    gathering and spending resources.
    """
    def __init__(self, curdl_code=None):
        """
        -- curdl_code: Defines the CURDL code of the organism. Defaults to a single central unit.
        """
        self.curdl_code = CURDL_code(['', '', '', ''])
        if curdl_code is not None:
            self.curdl_code = curdl_code

        self.stock = ResourcesStock()

    def function(self):
        """
        Updates the organism by activating all of its cells sequentially.
        Returns True iff the organism survives.
        """
        # Resets all temporary resources to zero
        self.stock.clear()

        # Sequentially activates all cells
        for cell_code in self.curdl_code.cell_codes():
            cell = _cell_types[cell_code]()
            cell.function(self)

        # Checks if some resources are missing. If so, the organism dies
        for amount in self.stock.get_resources().values():
            if amount < 0:
                return False
        return True

    def add_resource(self, resource_name, amount):
        """
        Adds a resource to the organism.
        --resource_name: codename of the resource such as 'O2' for dioxygen
        --amount: Amount of the said resource to add to the organism's stock. Can be negative,
                  but in this case prefer to use remove_resource for semantic.
        Returns the amount of the said resource AFTER it was added.
        """
        return self.stock.add(resource_name, amount)

    def remove_resource(self, resource_name, amount):
        """
        Removes a resource from the organism's stock.
        Returns the amount of the said resource AFTER it was removed.
        """
        return self.stock.remove(resource_name, amount)

    def number_of_cells(self):
        """
        Returns the amount of cells of the organism, central cell included.
        """
        return 1 + self.curdl_code.number_of_cells()
