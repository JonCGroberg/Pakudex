from pakudex import Pakudex

main_menu = ("Padudex Main Menu"
             "\n-----------------"
             "\n1. List Pakuri"
             "\n2. Show Pakuri"
             "\n3. Add Pakuri"
             "\n4. Evolve Pakuri"
             "\n5. Sort Pakuri"
             "\n6. Exit"
             "")


def handle_user_choice(choice: str, pakudex: Pakudex) -> None:
    if choice == "1":
        print("Pakuri In Pakudex:" if pakudex.get_size() > 0 else "No Pakuri in Pakudex yet!\n")

        for index, species in enumerate(pakudex.get_species_array()):
            print(f"{index + 1}. {species}")
    elif choice == "2":
        species = input("Enter the name of the species to display: ")
        stats = pakudex.get_stats(species)

        if stats is not None:
            print(f"\nSpecies: {species}\n"
                  f"Attack: {stats[0]}\n"
                  f"Defense: {stats[1]}\n"
                  f"Speed: {stats[2]}")
        else:
            print("Error: no such Pakuri!\n")

    elif choice == "3":
        species = input("Enter name of the species to add: ")
        print(f"Pakuri species {species} successfully added!" if pakudex.add_pakuri(species) else "Error: ")

    elif choice == "4":
        species = input("Enter name of the species to evolve: ")
        print(f"{species} has Evolved!" if pakudex.evolve_species(species) else "Error: no such Pakuri!")
    elif choice == "5":
        pakudex.sort_pakuri()
        print("Pakuri\thave\tbeen\tsorted!")
    elif choice == "6":
        print("Thanks for using Pakudex! Bye!")
        exit()
    else:
        print("Unrecognized menu selection!")


def prompt_capacity() -> int:
    capacity = 0
    while capacity == 0:
        user_input = input("Enter max capacity of the Pakudex ")

        try:
            if int(user_input) > 0:
                capacity = user_input
                print(f"The pakudex can hold {capacity} species of Pakuri.\n")
            else:
                print("Please enter a valid size")
        except ValueError:
            print("Please enter a valid size")
            continue

    return capacity


def main() -> None:
    print("Welcome to Pakudex: Tracker Extraordinaire! ")
    pakudex_capacity = prompt_capacity()
    pakudex = Pakudex(pakudex_capacity)

    # run the menu loop
    while True:
        print(main_menu)
        choice = input("\nWhat would you like to do? ")
        handle_user_choice(choice, pakudex)


if __name__ == '__main__':
    main()
