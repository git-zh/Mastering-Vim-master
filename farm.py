"""A farm for holding animals."""

class Farm(object):

    def __init__(slef):
        self.animals = set()

    def add_animal(self, animal):
        self.animals.add(animal)

    def print_contents(self):
        print(', '.join(self.animals)+'.')
