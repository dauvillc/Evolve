"""
Basic tests of the Simulator class
"""
from simulator import Simulator


if __name__ == "__main__":
    simulator = Simulator()
    simulator.add_organism(['', '', '', ''])
    simulator.add_organism(['R', '', '', '', '', '', ''])
    simulator.update()
    simulator.update()

    print("-" * 60 + "\nSimulation until death:")
    while simulator.organisms:
       simulator.update()
