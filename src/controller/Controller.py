from Models.Cone import Cone
from Models.Order import Order
from Models.Flavor import Flavor


class Controller:
    def __init__(self):
        # Simulierte Datenbank für Flavors
        self.flavors = [
            Flavor("Vanilla", "Classic vanilla flavor", 1.50),
            Flavor("Chocolate", "Rich chocolate flavor", 1.80),
            Flavor("Strawberry", "Fresh strawberry flavor", 1.70)
        ]
        self.current_cone = None
        self.orders = []

    def get_flavors(self):
        """Gibt die Liste der verfügbaren Flavors zurück."""
        return self.flavors

    def add_flavor(self, name, description, price):
        """Fügt einen neuen Flavor hinzu."""
        new_flavor = Flavor(name, description, price)
        self.flavors.append(new_flavor)

    def create_cone(self):
        """Erstellt eine neue Eistüte."""
        self.current_cone = Cone()
        return self.current_cone

    def get_current_cone(self):
        """Gibt die aktuelle Eistüte zurück."""
        return self.current_cone

    def add_flavor_to_cone(self, flavor):
        """Fügt einen Flavor zur aktuellen Eistüte hinzu."""
        if self.current_cone:
            self.current_cone.add_flavor(flavor)

    def create_order(self):
        """Erstellt eine neue Bestellung."""
        if self.current_cone:
            order = Order()
            order.add_item(self.current_cone)
            self.orders.append(order)
            self.current_cone = None  # Reset cone after adding to order
            return order
        else:
            raise ValueError("No cone to add to the order.")

    def get_orders(self):
        """Gibt alle Bestellungen zurück."""
        return self.orders
