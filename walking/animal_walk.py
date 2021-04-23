from datetime import date


# walking animals --------------------------------------
class Llama():
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


miss_fuzz = Llama("Miss Fuzz", "domestic llama", "evening", "hamburger")


class Giraffe():
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

leonard = Giraffe("Leonard", "leaf eater", "midday", "hamburger")


class Snow_leopard():
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

sassy = Snow_leopard("Sassy", "illusive leopard", "evening", "hamburger")


class Bonobo():
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

beatrice = Bonobo("Beatrice", "bonobo", "midday", "hamburger")


class Goat():
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()
        self.food = food
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

guthrie = Goat("Guthrie", "fainting goat", "morning", "hamburger")

print(guthrie.shift)