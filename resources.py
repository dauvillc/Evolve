"""
Defines the list of resources that exist in the environment, as
well as structures to store them (used in the organisms).
"""


_resources_list_ = ['O2']


class ResourcesStock:
    """
    A ResourcesStock .. stocks resources (I know, right ?). It associates to any
    resource an amount.
    """
    def __init__(self):
        self.map = dict()

    def add(self, resource_name, amount):
        """
        Adds a certain amount of a given resource to the stock.
        :param resource_name: Name of the resource as written in the resource list.
        :param amount: Amount. Watchout, the units for the resource vary.
        :return: The current amount of the said resource in the stock after the addition.
        """
        if resource_name in self.map:
            self.map[resource_name] += amount
        else:
            self.map[resource_name] = amount
        return self.map[resource_name]

    def remove(self, resource_name, amount):
        """
        Removes a certain amount of a given resource from the stock.
        :return: the amount of the said resource AFTER it was removed from the stock.
        """
        return self.add(resource_name, -amount)
