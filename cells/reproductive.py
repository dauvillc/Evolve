"""
Defines the reproductive cell
"""
from cells.cell import Cell
from tools.probas import centered_geometric
from simulator import simulator
from curdl import CURDL_code


# For now, all reproductive cells follow a law of same density
# This implies that all organisms reproduce at the same rate
_repro_rate = 20


class ReproductiveCell(Cell):
    """
    The reproductive cell has a certain probability at each time step
    of generating a new individual whose's curld code is derived from its
    parent
    """
    def __init__(self, organism):
        super().__init__(organism)

        # Age of the next reproduction
        self.next_repro_age = centered_geometric(1 / _repro_rate, 100)

    def function(self):
        if self.age >= self.next_repro_age:
            simulator.new_organism(CURDL_code())
            self.next_repro_age = self.age + centered_geometric(1 / _repro_rate, 100)
