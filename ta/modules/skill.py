"""Contains codes about skills"""

from random import randint


class Skill:

    def __init__(self, name, ctg, vis, cost, data):
        self.name = name
        self.type = ctg  # Category
        self.vis = vis  # Visuals (icons, arts, etc.)
        self.cost = cost
        self.data = data

    def cast(self, caster, target):
        print('{} is being casted on {}'.format(self.name, target))     