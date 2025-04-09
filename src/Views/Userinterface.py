from Models.Flavor import Flavor
from Models.Cone import Cone
from Models.Order import Order


class Userinterface:
    def __init__(self, controller):
        self.controller = controller

    def get_user_input(self, message):
        """Asks the user for input."""
        return input(message)

    def display_output(self, message):
        """Displays a message in the terminal."""
        print(message)

    def display_flavors(self, flavors):
        """Displays the list of available flavors."""
        print("\nAvailable Flavors:")
        for i, flavor in enumerate(flavors):
            print(f"{i+1}. {flavor.name} - {flavor.flavor} - {flavor.price_per_scoop:.2f} CHF")

    def ask_for_flavor(self, flavors):
        """Asks the user to select a flavor from the list."""
        self.display_flavors(flavors)
        while True:
            try:
                choice = int(input("Choose a flavor by number: "))
                if 1 <= choice <= len(flavors):
                    return flavors[choice - 1]
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number.")

    def display_orders(self, orders):
        """Displays all orders."""
        print("\nOrders:")
        if not orders:
            print("No orders available.")
            return
        for i, order in enumerate(orders):
            print(f"Order {i+1}:")
            for cone in order.cones:
                print("  Cone:")
                for scoop in cone.scoops:
                    print(f"    - {scoop.name} ({scoop.flavor}) - {scoop.price_per_scoop:.2f} CHF")
