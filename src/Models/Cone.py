from Models.Flavor import Flavor

class Cone:
    def __init__(self):
        self._scoops = []

    @property
    def scoops(self):
        return self._scoops

    def add_flavor(self, flavor: Flavor):
        if not hasattr(self, '_scoops'):
            self._scoops = []
        if len(self._scoops) < 3:
            self._scoops.append(flavor)
        else:
            raise ValueError("Cannot add more than 3 scoops to the cone.")