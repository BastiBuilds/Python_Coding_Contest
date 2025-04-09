from Models.Cone import Cone
from Models.Order import Order
from Models.Flavor import Flavor


class Controller:
    def __init__(self):
        # Simulated database for flavors
        self.flavors = [
            Flavor("Vanilla", "Classic vanilla flavor", 1.50),
            Flavor("Chocolate", "Rich chocolate flavor", 1.80),
            Flavor("Strawberry", "Fresh strawberry flavor", 1.70)
        ]
        self.current_cone = None
        self.orders = []

    def get_flavors(self):
        """Returns the list of available flavors."""
        return self.flavors

    def add_flavor(self, name, description, price):
        """Adds a new flavor to the list."""
        new_flavor = Flavor(name, description, price)
        self.flavors.append(new_flavor)

    def create_cone(self):
        """Creates a new cone."""
        self.current_cone = Cone()
        return self.current_cone

    def get_current_cone(self):
        """Returns the current cone."""
        return self.current_cone

    def add_flavor_to_cone(self, flavor):
        """Adds a flavor to the current cone."""
        if self.current_cone:
            self.current_cone.add_flavor(flavor)
        else:
            raise ValueError("No cone created. Create a cone first.")

    def create_order(self):
        """Creates a new order."""
        if self.current_cone:
            order = Order()
            order.add_item(self.current_cone)
            self.orders.append(order)
            self.current_cone = None  # Reset the cone after adding it to the order
            return order
        else:
            raise ValueError("No cone to add to the order. Create a cone first.")

    def get_orders(self):
        """Returns all orders."""
        return self.orders
