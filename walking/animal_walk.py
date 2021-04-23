from datetime import date


# walking animals --------------------------------------
class Llama():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

miss_fuzz = Llama("Miss Fuzz", "domestic llama")


class Giraffe():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

leonard = Giraffe("Leonard", "leaf eater")


class Snow_leopard():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

sassy = Snow_leopard("Sassy", "illusive leopard")


class Bonobo():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

beatrice = Bonobo("Beatrice", "bonobo")


class Goat():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

guthrie = Goat("Guthrie", "fainting goat")