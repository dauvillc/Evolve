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

    def __init__(self, initial_code=['', '', '', '']):
        """
        --initial_code: If not empty, will be used as an initial code.
        """
        self.code = initial_code

    def cell_codes(self):
        """
        Iterates over all cells in the code.
        """
        for cell in self.code:
            if cell != '':
                yield cell

    def check_validity(self):
        """
        Checks that the CURDL code is valid, i.e:
        - For every cell, another sequence of 3 children is added. This is is equivalent to
          len(code) = 4 + 3 * ne    where ne is the number of non-empty cells (excluding the central unit)
        :return: True iff the code checks all rules
        """
        return len(self.code) == 4 + 3 * len([cell for cell in self.code if cell != ''])

    def number_of_cells(self):
        """
        Returns the number of cells in the curdl code.
        """
        return len([cell for cell in self.code if cell != ''])
