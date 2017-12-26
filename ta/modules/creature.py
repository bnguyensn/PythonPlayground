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
        if self.dungeon.is_xy_inbound(dest_x, dest_y):
            # Remove current content from current cell
            self.dungeon.get_cell_from_xy(self.pos_x, self.pos_y).content = None
            # Move self to new destination
            self.pos_x = dest_x
            self.pos_y = dest_y
            self.dungeon.get_cell_from_xy(dest_x, dest_y).content = self

            print('Moved to new destination at ({}, {})'.format(dest_x, dest_y))
        else:
            print('Target destination is out of bound.')

    def attack(self, target):
        # Roll a die to determine damage!
        dmg = randint(self.stats['dmg_min'], self.stats['dmg_max'])
        target.stats['hp'] -= dmg

        print('{} attacks {} for {} damage!'.format(self.name, target.name, dmg))

        # Check if target is dead
        if target.stats['hp'] <= 0:
            target.self_destruct()

    def drop_loot(self):
        pass

    def self_destruct(self):
        # Drop some loot
        self.drop_loot()
        # Remove self from dungeon
        self.dungeon.get_cell_from_xy(self.pos_x, self.pos_y).content = None
        # Move self to graveyard
        self.pos_x, self.pos_y = 0, 0

        print('{} has been destroyed.'.format(self.name))


"""PLAYER"""


class Player(Creature):

    def __init__(self, dungeon, pos_x, pos_y):
        super().__init__(dungeon,
                         'Player',
                         'Player',
                         {
                             'hp': 100,
                             'dmg_min': 4,
                             'dmg_max': 6,
                             'armor': 0
                         },
                         [0],
                         pos_x, pos_y)


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
