# Pakudex Python

Pakudex Python is a project designed to help students practice object-oriented programming concepts, such as classes and objects, by building a cataloguing system for creatures called "Pakuri."

Note: This project concept is a work of satire and does not promote the mistreatment or exploitation of creatures.

Overview
The project aims to provide a system for indexing and managing Pakuri, which are small magical creatures that can fit into pockets. Users can create and store different species of Pakuri in a catalog known as the Pakudex. The system allows users to perform various operations on the Pakudex, such as listing Pakuri, displaying species information, adding new Pakuri, evolving existing Pakuri, sorting Pakuri, and exiting the program.

- [`pakudex.py`](pakudex.py): This file contains the main class for managing the Pakudex (Pakuri index).
- [`pakuri_program.py`](pakuri_program.py): This file is the main entry point of the program, handling user input and output.
- [`pakuri.py`](pakuri.py): This file defines the Pakuri creature class.

## Demo

```console
What would you like to do? 1
Pakuri In Pakudex:
1. Charasaurus
2. Pikabu
3. PsyGoose

Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit

What would you like to do? 4
Enter the name of the species to evolve: Pikabu
Pikabu has evolved!

Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit

What would you like to do? 2
Enter the name of the species to display: Pikabu

Species: Pikabu
Attack: 102
Defense: 188
Speed: 147
```

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

This project requires Python 3.8 or later. You can download it from [here](https://www.python.org/downloads/).

### Installing

1. Clone the repository: `git clone https://github.com/JonCGroberg/Pakudex.git`
2. Navigate to the project directory: `cd Pakudex`
3. Run the program: `python pakuri_program.py`

## Running the tests

To run the tests, use the command: `python -m unittest`

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
