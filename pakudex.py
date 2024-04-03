from pakuri import Pakuri


class Pakudex:
    def __init__(self, capacity: int = 20):
        self.capacity = capacity
        self.species_array: list[Pakuri] = []

    def get_size(self):
        return len(self.species_array)

    def get_capacity(self):
        return self.capacity

    def get_species_array(self) -> list:
        return self.species_array

    def get_stats(self, species) -> list[int] or None:
        stats = []
        if species in self.species_array:
            return stats
        else:
            return None

    def sort_pakuri(self) -> None:
        # sort(self.species_array)
        pass
