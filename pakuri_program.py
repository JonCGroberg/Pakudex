from pakudex import Pakudex

main_menu = ("Pakudex Main Menu"
             "\n-----------------"
             "\n1. List Pakuri"
             "\n2. Show Pakuri"
             "\n3. Add Pakuri"
             "\n4. Evolve Pakuri"
             "\n5. Sort Pakuri"
             "\n6. Exit"
             "")


def handle_user_choice(choice: str, pakudex: Pakudex) -> None:
    """Handles user menu choices and interacts with the Pakudex object.

      Args:
          choice: The user's menu choice as a string.
          pakudex: The Pakudex object used for managing Pakuri.
      """
    # Handle user menu choices
    if choice == "1":
        print("Pakuri In Pakudex:" if pakudex.get_size() > 0 else "No Pakuri in Pakudex yet!\n")
        arr = pakudex.get_species_array()
        # If there are Pakuri, display them with an index
        if arr is not None:
            for index, species in enumerate(arr):
                print(f"{index + 1}. {species}")
        print("")  # Print an empty line after listing Pakuri
    elif choice == "2":
        species = input("Enter the name of the species to display: ")
        stats = pakudex.get_stats(species)
        # If stats exist, display them
        if stats is not None:
            print(f"\nSpecies: {species}\n"
                  f"Attack: {stats[0]}\n"
                  f"Defense: {stats[1]}\n"
                  f"Speed: {stats[2]}")
        else:
            print("Error: No such Pakuri!\n")
    elif choice == "3":
        # Check if the Pakudex is full
        if pakudex.get_size() >= pakudex.get_capacity():
            print("Error: Pakudex is full!")
        else:
            species = input("Enter the name of the species to add: ")
            # Try to add the Pakuri and display a success or failure message
            if pakudex.add_pakuri(species):
                print(f"Pakuri species {species} successfully added!")
            else:
                print("Error: Pakudex already contains this species!")
    elif choice == "4":
        species = input("Enter the name of the species to evolve: ")
        # Try to evolve the Pakuri and display a success or failure message
        print(f"{species} has evolved!" if pakudex.evolve_species(species) else "Error: No such Pakuri!\n")
    elif choice == "5":
        # Sort the Pakuri in the Pakudex
        pakudex.sort_pakuri()
        print("Pakuri\thave\tbeen\tsorted!")
    elif choice == "6":
        # Handle invalid user input
        print("Thanks for using Pakudex! Bye!")
        exit()
    else:
        # Handle invalid user input\
        print("Unrecognized menu selection!")


def prompt_capacity() -> int:
    """Prompts the user for a valid maximum capacity for the Pakudex.

       Returns:
           The integer value entered by the user as the Pakudex capacity.
       """
    # runs until we get a valid capacity
    capacity = 0
    while capacity == 0:
        user_input = input("Enter max capacity of the Pakudex: ")
        try:
            if int(user_input) > 0:
                capacity = user_input
                print(f"The Pakudex can hold {capacity} species of Pakuri.\n")
            else:
                print("Please enter a valid size.")
        except ValueError:
            print("Please enter a valid size.")
            continue
    return capacity


def main() -> None:
    """Prompts the user for a valid maximum capacity for the Pakudex.

       Returns:
           The integer value entered by the user as the Pakudex capacity.
       """
    print("Welcome to Pakudex: Tracker Extraordinaire! ")
    pakudex_capacity = prompt_capacity()
    pakudex = Pakudex(pakudex_capacity)
    # run the menu loop
    while True:
        print(main_menu)
        choice = input("\nWhat would you like to do? ")
        handle_user_choice(choice.strip(), pakudex)


if __name__ == '__main__':
    main()
