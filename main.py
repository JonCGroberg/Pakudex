main_menu = ("Padudex Main Menu"
             "-----------------"
             "1. List Pakuri"
             "2. Show Pakuri"
             "3. Add Pakuri"
             "4. Evolve Pakuri"
             "5. Sort Pakuri"
             "6. Exit"
             "")


def handle_user_choice(choice: str) -> None:
    if choice == "1":
        pass
    if choice == "2":
        pass
    if choice == "3":
        pass
    if choice == "4":
        pass
    if choice == "5":
        pass
    if choice == "6":
        exit()


def main() -> None:
    print("Welcome to Pakudex: Tracker Extraordinaire! ")
    pakudex_capacity = input("Enter max capacity of the Pakudex")
    print(f"The pakudex can hold {pakudex_capacity} species of Pakuri.")

    # run the menu loop
    while True:
        print(main_menu)
        choice = input("What would you like to do? ")
        handle_user_choice(choice)


if __name__ == '__main__':
    main()
