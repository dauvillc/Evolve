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
    def __init__(self, env, curdl_code=None):
        """
        -- env: simulation Environment object
        -- curdl_code: Defines the CURDL code of the organism. Defaults to a single central unit.
        """
        self.curdl_code = CURDL_code(['', '', '', ''])
        if curdl_code is not None:
            self.curdl_code = curdl_code
        if not self.curdl_code.check_validity():
            print("ERROR: invalid code: ", self.curdl_code)
            exit(-1)

        # Declare the Cells() objects
        self.cells = self.build_cells()

        self.stock = ResourcesStock()
        self.env = env

    def build_cells(self):
        """
        Builds the cells list from the curdl code.
        """
        # For each cell code in the CURDL code, create the corresponding Cell object
        return [CentralCell(self)] +\
               [_cell_types[cell_code](self) for cell_code in self.curdl_code if cell_code != '']

    def function(self):
        """
        Updates the organism by activating all of its cells sequentially.
        Returns True iff the organism survives.
        -- env: simulation Environment object
        """
        # Resets all temporary resources to zero
        self.stock.clear()

        # Sequentially activates all cells
        for cell in self.cells:
            cell.update()
            cell.function()

        # Checks if some resources are missing. If so, the organism dies
        while self.cells and not self.missing_resources():
            # Death of cells: The younger cells die until there are enough resources.
            # If the central cell dies, the organism is dead
            self.curdl_code.suppress_last_cell()
            del self.cells[-1]

        return self.cells == []

    def missing_resources(self):
        """
        Returns the list of resources that the organism is missing
        """
        missing = []
        for resource, amount in self.stock.get_resources().items():
            if amount < 0:
                missing.append(resource)
        return missing

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

    def __repr__(self):
        return str(self.curdl_code)
