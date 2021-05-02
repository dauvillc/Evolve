"""
Basic tests on the Organism class.
"""
from organism import Organism
from curdl import CURDL_code
from environment import Environment


if __name__ == "__main__":
    fake_env = Environment()

    central_only = Organism(fake_env, CURDL_code())
    print("Whether the empty org survived: ", central_only.function())
    print("Empty org's resources: ", central_only.stock.get_resources())

    basic = Organism(fake_env, CURDL_code(['R', '', '', '', '', '', '']))
    print("Whether the basic org survived: ", basic.function())
    print("Basic org's resources: ", basic.stock.get_resources())