"""
Defines the Simulator class.
"""
from environment import Environment
from organism import Organism
from curdl import CURDL_code


class Simulator:
    """
    The Simulator is the objects which handles all of the simulation. It has a global overview and access
    to the environment as well as organisms.
    """
    def __init__(self):
        # Current time of simulation
        self.time = 0
        self.env = Environment()

        self.organisms = []

    def update(self):
        """
        Simulates a single timestep of the simulation.
        """
        self.time += 1
        event_occured = False

        dead_orgs = []
        for i, org in enumerate(self.organisms):
            if not org.function():
                dead_orgs.append(org)
                event_occured = True

        # Forget about dead organisms
        for org in dead_orgs:
            self.organisms.remove(org)
            print("T=", self.time, " | Death: ", org, " at age ", org.age)

        # Only print simulation information if something happened
        if event_occured:
            print("T=", self.time, " - Number of organsisms: ", len(self.organisms))

    def add_organism(self, code):
        """
        Adds a new organism with the given code. The code should be written
        as a list.
        """
        self.organisms.append(Organism(self.env, CURDL_code(code)))

    def print_state(self):
        """
        Prints general information about the current state of the simulation.
        """
        print("Current time: ", self.time)
        print("Number of organisms: ", len(self.organisms))