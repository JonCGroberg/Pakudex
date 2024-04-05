class Pakuri:
    """A class used to represent a Pakuri, a fictional creature in the Pakudex world.

    Attributes:
        _species (str): The name of the Pakuri species.
        _attack (int): The Pakuri's attack stat.
        _defense (int): The Pakuri's defense stat.
        _speed (int): The Pakuri's speed stat.
    """

    def __init__(self, species: str):
        """
        Initializes a new Pakuri object.

        Args:
            species (str): The name of the Pakuri species.
        """

        self._species = species
        self._attack = (len(species) * 7) + 9  # Calculate attack based on species name length
        self._defense = (len(species) * 5) + 17  # Calculate defense based on species name length
        self._speed = (len(species) * 6) + 13  # Calculate speed based on species name length

    def get_species(self) -> str:
        """Returns the Pakuri's species name.

        Returns:
            str: The Pakuri's species name.
        """

        return self._species

    def get_attack(self) -> int:
        """Returns the Pakuri's attack stat.

        Returns:
            int: The Pakuri's attack stat.
        """

        return self._attack

    def get_speed(self) -> int:
        """Returns the Pakuri's speed stat.

        Returns:
            int: The Pakuri's speed stat.
        """

        return self._speed

    def get_defense(self) -> int:
        """Returns the Pakuri's defense stat.

        Returns:
            int: The Pakuri's defense stat.
        """

        return self._defense

    def set_attack(self, new_attack: int) -> None:
        """Sets the Pakuri's attack stat.

        Args:
            new_attack (int): The new attack stat value.
        """

        self._attack = new_attack

    def evolve(self) -> None:
        """Doubles the Pakuri's attack, quadruples its defense, and triples its speed.

        This method simulates the evolution of a Pakuri, significantly increasing its stats.
        """

        self._attack *= 2
        self._defense *= 4
        self._speed *= 3

    def __str__(self) -> str:
        """Returns a string representation of the Pakuri object in the format:
        "species: attack: defense: speed"

        Returns:
            str: A string representation of the Pakuri object.
        """

        return f"{self._species}: attack: {self._attack} defense: {self._defense} speed: {self._speed}"

    def __lt__(self, other) -> bool:
        """Compares two Pakuri objects by their species names for sorting purposes.

        Args:
            other (Pakuri): The other Pakuri object to compare with.

        Returns:
            bool: True if the current Pakuri's species name is less than the other Pakuri's,
                  False otherwise.
        """

        return self._species < other._species
