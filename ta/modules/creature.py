"""Contains codes about creatures"""

from random import randint


class Creature:
    
    def __init__(self, dungeon, name, cls, stats, inv, pos_x, pos_y):
        self.dungeon = dungeon
        self.name = name
        self.cls = cls
        self.stats = stats
        self.inv = inv
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def move(self, dest_x, dest_y):
        self.pos_x = dest_x
        self.pos_y = dest_y

    def attack(self, target):
        # Roll a die to determine damage!
        dmg = randint(self.stats.dmg_min, self.stats.dmg_max)
        target.stats.hp -= dmg

        print('{} attacks {} for {} damage!'.format(self.name, target.name, dmg))

        # Check if target is dead
        if target.stats.hp <= 0:
            target.self_destruct()

    def self_destruct(self):
        # Remove self from dungeon
        self.dungeon.get_cell_from_xy(self.pos_x, self.pos_y).contains = None
        # Move self to graveyard
        self.pos_x, self.pos_y = 0, 0

        print('{} has been destroyed.'.format(self.name))


class Player(Creature):
    pass


"""MONSTERS"""


class Skeleton(Creature):

    def __init__(self, dungeon, pos_x, pos_y):
        super().__init__(dungeon,
                         'Skeleton Warrior',
                         'Monster',
                         {
                             'hp': 10,
                             'dmg_min': 1,
                             'dmg_max': 3,
                             'armor': 0
                         },
                         [5],
                         pos_x, pos_y)
