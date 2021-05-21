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

        # List of newly created organisms during the current update
        self._new_organisms_ = []

    def update(self):
        """
        Simulates a single timestep of the simulation.
        """
        self.time += 1
        event_occured = False

        dead_orgs = []
        self._new_organisms_ = []
        for i, org in enumerate(self.organisms):
            if not org.function():
                dead_orgs.append(org)
                event_occured = True

        # Forget about dead organisms
        for org in dead_orgs:
            self.organisms.remove(org)
            print("T=", self.time, " | Death: ", org, " at age ", org.age)

        # Create the new organisms
        for code in self._new_organisms_:
            self.add_organism(code)
            print("T={} | Birth: {}".format(self.time, code))

        # Only print simulation information if something happened
        if event_occured:
            print("T=", self.time, " - Number of organsisms: ", len(self.organisms))

    def add_organism(self, code):
        """
        Adds a new organism with the given code. The code should be written
        as a list. Should not be used during the simulation phases and updating
        of the organisms.
        """
        self.organisms.append(Organism(self.env, CURDL_code(code)))

    def new_organism(self, code):
        """
        Creates a new organism, which will not be updated before the next global update.
        --code: CURDL code of the new organism
        """
        self._new_organisms_.append(code)

    def print_state(self):
        """
        Prints general information about the current state of the simulation.
        """
        print("Current time: ", self.time)
        print("Number of organisms: ", len(self.organisms))


# Global simulation variable
simulator = Simulator()