from datetime import datetime
from Models.Cone import Cone

class Order:
    def __init__(self):
        self.__created_at = datetime.now()
        self.__cones = []
        @property
        def created_at(self):
            return self.__created_at

        @property
        def cones(self):
            return self.__cones

    def add_item(self, item: Cone):
        if not isinstance(item, Cone):
            raise TypeError("item must be an instance of Cone")
        self.__cones.append(item)