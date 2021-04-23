from datetime import date

# swimming animals --------------------------------------

class Salmon():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

suzie = Salmon("Suzie", "pink salmon", "fish food")


class Manatee():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

marceline = Manatee("Marceline", "soft and large", "fish food")


class Sting_ray():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

samuel = Sting_ray("Samuel", "zebra painted", "fish food")


class Eel():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

elfie = Eel("Elfie", "electric", "fish food")


class Goldfish():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

nemo = Goldfish("Nemo", "domestic", "fish food")