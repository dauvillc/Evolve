"""
Defines the CURDL code class and functions to manipulate it.
"""


class CURDL_code:
    """
    A CURDL code is the sequence of cells that constitute an organism.
    It is defined as a list of cells such that:
    - The first 4 cells are the neighbours of the central unit
    - After those 4 cells, each sequence of 3 consecutive cells are the neighbours of the cell
      except its parent. The children are considered in the order UP, RIGHT, DOWN, LEFT.
    For example, ABCD EFG means the following organism:

                    E
                  G A F
                  D 0 B
                    C

    Where 0 is the central unit. Here we know that G is on the left side of A since its down side is already
    occupied by its parent cell, 0.
    """
    def __init__(self, list=[]):
        """
        --list: If not empty, will be used as an initial code.
        """
        self.list = list