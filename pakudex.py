from pakuri import Pakuri


class Pakudex:
    """A class used to represent a Pakudex, a device for storing and managing Pakuri.

    Attributes:
        _capacity (int): The maximum number of Pakuri the Pakudex can hold.
        _pakuri_array (list[Pakuri]): The list of Pakuri objects stored in the Pakudex.
    """

    def __init__(self, capacity: int = 20) -> None:
        """
        Initializes a new Pakudex object.

        Args:
            capacity (int, optional): The maximum capacity of the Pakudex. Defaults to 20.
        """

        self._capacity: int = capacity
        self._pakuri_array: list[Pakuri] = []

    def get_size(self) -> int:
        """
        Returns the number of Pakuri currently stored in the Pakudex.

        Returns:
            int: The number of Pakuri in the Pakudex.
        """

        return int(len(self._pakuri_array))

    def get_capacity(self) -> int:
        """
        Returns the maximum capacity of the Pakudex.

        Returns:
            int: The maximum number of Pakuri the Pakudex can hold.
        """

        return int(self._capacity)

    def get_species_array(self) -> list[str] | None:
        """
        Returns a list of species names for all Pakuri in the Pakudex, or None if empty.

        Returns:
            list[str] | None: A list of species names or None if there are no Pakuri.
        """

        if self.get_size() > 0:
            return [pakuri._species for pakuri in self._pakuri_array]
        else:
            return None

    def get_stats(self, species: str) -> list[int] | None:
        """
        Returns a list of attack, defense, and speed stats for a specified Pakuri species,
        or None if the Pakuri doesn't exist.

        Args:
            species (str): The name of the Pakuri species to get stats for.

        Returns:
            list[int] | None: A list of [attack, defense, speed] stats or None if not found.
        """

        index = self.__private_index_of_species(species)

        if index is not None:
            pakuri = self._pakuri_array[index]
            return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        else:
            return None

    def sort_pakuri(self) -> None:
        """
        Sorts the Pakuri in the Pakudex by species name.
        """

        self._pakuri_array.sort()

    def add_pakuri(self, species: str) -> bool:
        """
        Adds a new Pakuri to the Pakudex if there's space and the species doesn't already exist.

        Args:
            species (str): The name of the Pakuri species to add.

        Returns:
            bool: True if the Pakuri was added successfully, False otherwise.
        """
        if self.__private_index_of_species(species) is not None:
            return False
        else:
            self._pakuri_array.append(Pakuri(species))
            return True

    def evolve_species(self, species: str) -> bool:
        """
        Evolves a Pakuri in the Pakudex by increasing its stats, if the species exists.

        Args:
            species (str): The name of the Pakuri species to evolve.

        Returns:
            bool: True if the Pakuri was evolved successfully, False otherwise.
        """

        index = self.__private_index_of_species(species)
        if index is not None:
            self._pakuri_array[index].evolve()
            return True
        else:
            return False

    # returns the s
    def __private_index_of_species(self, species: str) -> int | None:
        # check each pakuri's name and return index if we find it, else None
        for index, pakuri in enumerate(self._pakuri_array):
            if species == pakuri.get_species():
                return index
        return None

    # nice looking string
    def __str__(self):
        return "\n".join([str(x) for x in self._pakuri_array])
