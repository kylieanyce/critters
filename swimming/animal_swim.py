from datetime import date

# swimming animals --------------------------------------

class Salmon():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

suzie = Salmon("Suzie", "pink salmon")


class Manatee():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

marceline = Manatee("Marceline", "soft and large")


class Sting_ray():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

samuel = Sting_ray("Samuel", "zebra painted")


class Eel():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

elfie = Eel("Elfie", "electric")


class Goldfish():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

nemo = Goldfish("Nemo", "domestic")