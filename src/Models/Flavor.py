class Flavor:

    def __init__(self, name:str, flavor: str, price_per_scoop: float):
        self.__name = name
        self.__flavor = flavor
        self.__price_per_scoop = price_per_scoop
        pass

    @property
    def name(self):
        return self.__name

    @property
    def flavor(self):
        return self.__flavor

    @property
    def price_per_scoop(self):
        return self.__price_per_scoop
    
    @property
    def name(self):
        return self.__name

    @property
    def flavor(self):
        return self.__flavor

    @property
    def price_per_scoop(self):
        return self.__price_per_scoop
