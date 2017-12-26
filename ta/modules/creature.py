"""Contains codes about creatures"""


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
        target.stats.hp -= self.stats.dmg

    def kill(self):
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
