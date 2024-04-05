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
        print("Pakuri In Pakudex" if pakudex.get_size() > 0 else "No Pakuri in Pakudex yet!")

        for index, species in enumerate(pakudex.get_species_array()):
            print(f"{index + 1}. {species}")
    elif choice == "2":

    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
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
