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
