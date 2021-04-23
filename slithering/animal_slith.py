from datetime import date

# slithering animals ---------------------------------------

class Snake():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

serpentine = Snake("Serpentine", "coral snake")


class Alligator():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

arnie = Alligator("Arnie", "spikey boi")


class Dragon():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

duncan = Dragon("Duncan", "dandy boi")


class Salamander():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

sasquatch = Salamander("Sasquatch", "rainbow boi")


class Lizard():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

lucinda = Lizard("Lucinda", "chameleon")