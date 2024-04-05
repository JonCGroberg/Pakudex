class Pakuri:
    """A class used to represent a Pakuri

    Stats
    -----
    - attack
    - defense
    - speed

    """

    def __init__(self, species: str):
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    def get_species(self) -> str:
        return self.species

    def get_attack(self) -> int:
        return self.attack

    def get_speed(self) -> int:
        return self.speed

    def get_defense(self) -> int:
        return self.defense

    def set_attack(self, new_attack: int) -> None:
        self.attack = new_attack

    def evolve(self) -> None:
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3

    def __str__(self) -> str:
        return f"{self.species}: attack: {self.attack} defense: {self.defense} speed: {self.speed}"

    def __lt__(self, other) -> bool:
        return self.species < other.species
