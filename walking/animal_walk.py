from datetime import date


# walking animals --------------------------------------
class Llama():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "evening")


class Giraffe():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

leonard = Giraffe("Leonard", "leaf eater", "midday")


class Snow_leopard():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

sassy = Snow_leopard("Sassy", "illusive leopard", "evening")


class Bonobo():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

beatrice = Bonobo("Beatrice", "bonobo", "midday")


class Goat():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

guthrie = Goat("Guthrie", "fainting goat", "morning")

print(guthrie.shift)