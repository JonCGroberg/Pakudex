from pakuri import Pakuri


class Pakudex:
    def __init__(self, capacity: int = 20) -> None:
        self.capacity = capacity
        self.pakuri_array: list[Pakuri] = []

    def get_size(self) -> int:
        return len(self.pakuri_array)

    def get_capacity(self) -> int:
        return self.capacity

    def get_species_array(self) -> list[str]:
        return [pakuri.species for pakuri in self.pakuri_array]

    # get the stats for a certain species or return none if DNE
    def get_stats(self, species) -> list[int] | None:
        index = self.__private_index_of_species(species)

        if index is not None:
            pakuri = self.pakuri_array[index]
            return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        else:
            return None

    def sort_pakuri(self) -> None:
        # sort(self.species_array)
        pass

    def add_pakuri(self, species: str) -> bool:
        if self.__private_index_of_species(species) is not None:
            return False
        else:
            self.pakuri_array.append(Pakuri(species))
            return True

    def evolve_species(self, species):
        index = self.__private_index_of_species(species)
        if index is not None:
            self.pakuri_array[index].evolve()
            return True
        else:
            return False

    # returns the s
    def __private_index_of_species(self, species: str) -> int | None:
        # check each pakuris name and return index if we find it, else None
        for index, pakuri in enumerate(self.pakuri_array):
            if species == pakuri.get_species():
                return index
        return None

    # nice looking string
    def __str__(self):
        return "\n".join([str(x) for x in self.pakuri_array])
