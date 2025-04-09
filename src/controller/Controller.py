class Controller:
    def ask_for_flavor(flavors:list[Flavor]):
        """
        Prompt the user to select an ice cream flavor from a list.

        Displays a numbered list of available flavors, including the name,
        flavor description, and price per scoop. The user is then prompted
        to enter the number corresponding to their desired flavor. The input
        is validated to ensure it corresponds to one of the options.

        Parameters:
            flavors (list[Flavor]): A list of flavor objects, each with properties
                                    `name`, `flavor`, and `price_per_scoop`.

        Returns:
            object: The selected flavor object from the list.
        """
        for i, flavor in enumerate(flavors):
            print(f"{i+1}. {flavor.name:<15}{flavor.flavor:<15}{flavor.price_per_scoop:>5.2f} CHF")
        
        while True:
            u_input = input(f"Choose from the list above:")
            try:
                x = int(u_input)
                if 1 <= x <= len(flavors):
                    return flavors[x - 1]
                else:
                    raise ValueError
            except Exception:
                print(f"Select from the list between 1 and {len(flavors)}.")


    def ask_for_yes_no(message: str):
        """
        Prompt the user with a yes/no question and return their response as a boolean.

        Displays the given message followed by "(y/n):" and waits for the user to
        enter 'y' or 'n'. The input is not case-sensitive and will re-prompt the user
        until a valid response is provided.

        Parameters:
            message (str): The question or prompt to display to the user.

        Returns:
            bool: True if the user enters 'y', False if the user enters 'n'.
        """
        while True:
            u_input = input(f"{message} (y/n):").lower()
            if u_input == "y" or u_input == "n":
                return True if u_input == "y" else False
            else:
                print("Please enter 'y' or 'n'.")