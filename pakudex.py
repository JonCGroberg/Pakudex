from pakuri import Pakuri


class Pakudex:
    def __init__(self, capacity: int = 20) -> None:
        self.capacity = capacity
        self.pakuri_array: list[Pakuri] = []

    def get_size(self) -> int:
        return len(self.pakuri_array)

    def get_capacity(self) -> int:
        return self.capacity

    def get_species_array(self) -> str:
        return " ".join([pakuri.species for pakuri in self.pakuri_array])

    # get the stats for a certain species or return none if DNE
    def get_stats(self, species) -> list[int] or None:
        if species in self.pakuri_array:
            return [species.get_attack, species.get_defense, species.get_speed]
        else:
            return None

    def sort_pakuri(self) -> None:
        # sort(self.species_array)
        pass

    def add_pakuri(self, species: str) -> bool:
        if self.__private_index_of_species(species):
            return False
        else:
            self.pakuri_array.append(Pakuri(species))
            return True

    def evolve_species(self, species):
        if self.__private_index_of_species(species):
            species.evolve()
            return True
        else:
            return False

    # returns the s
    def __private_index_of_species(self, species: str) -> int | None:
        # check each pakuris name and return true if we find it, else false
        for pakuri, index in self.pakuri_array:
            if species == pakuri.get_species():
                return index
        return None

    # nice looking string
    def __str__(self):
        return "\n".join([str(x) for x in self.pakuri_array])
