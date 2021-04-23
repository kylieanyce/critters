from datetime import date

# slithering animals ---------------------------------------

class Snake():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

serpentine = Snake("Serpentine", "coral snake", "reptile food")


class Alligator():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

arnie = Alligator("Arnie", "spikey boi", "reptile food")


class Dragon():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

duncan = Dragon("Duncan", "dandy boi", "reptile food")


class Salamander():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

sasquatch = Salamander("Sasquatch", "rainbow boi", "reptile food")


class Lizard():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

lucinda = Lizard("Lucinda", "chameleon", "fishfood")