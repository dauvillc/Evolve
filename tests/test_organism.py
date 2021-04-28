"""
Basic tests on the Organism class.
"""
from organism import Organism
from curdl import CURDL_code


if __name__ == "__main__":
    central_only = Organism(CURDL_code())
    central_only.function()
    print("Empty org's resources: ", central_only.stock.get_resources())

    basic = Organism(CURDL_code(['R', '', '', '', '', '', '']))
    basic.function()
    print("Basic org's resources: ", basic.stock.get_resources())