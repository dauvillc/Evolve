"""
Defines the Organism class.
"""
from curdl import CURDL_code
from resources import ResourcesStock


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
