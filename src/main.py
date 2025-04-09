from Views.Userinterface import Userinterface
from controller.Controller import Controller

def main():
    controller = Controller()
    ui = Userinterface(controller)

    while True:
        print("\nCommands:")
        print("1. Show available flavors")
        print("2. Add a new flavor")
        print("3. Create a new cone")
        print("4. Add flavor to cone")
        print("5. Add cone to order")
        print("6. Show all orders")
        print("7. Exit")

        user_input = ui.get_user_input("Enter a command: ")
        if user_input == "1":
            flavors = controller.get_flavors()
            ui.display_flavors(flavors)
        elif user_input == "2":
            flavor_name = ui.get_user_input("Enter flavor name: ")
            flavor_description = ui.get_user_input("Enter flavor description: ")
            price = float(ui.get_user_input("Enter price per scoop: "))
            controller.add_flavor(flavor_name, flavor_description, price)
        elif user_input == "3":
            cone = controller.create_cone()
            ui.display_output("New cone created.")
        elif user_input == "4":
            cone = controller.get_current_cone()
            if not cone:
                ui.display_output("No cone created. Create a cone first.")
                continue
            flavors = controller.get_flavors()
            selected_flavor = ui.ask_for_flavor(flavors)
            controller.add_flavor_to_cone(selected_flavor)
            ui.display_output(f"Added {selected_flavor.name} to the cone.")
        elif user_input == "5":
            try:
                order = controller.create_order()
                ui.display_output("Cone added to order.")
            except ValueError as e:
                ui.display_output(str(e))
        elif user_input == "6":
            orders = controller.get_orders()
            ui.display_orders(orders)
        elif user_input == "7":
            ui.display_output("Goodbye!")
            break
        else:
            ui.display_output("Invalid command. Please try again.")

if __name__ == "__main__":
    main()