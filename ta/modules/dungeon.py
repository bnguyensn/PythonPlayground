"""Contain codes related to setting up a dungeon"""

from random import random

"""CLASSES"""


class Dungeon:

    def __init__(self, max_x, max_y, cell_list):
        self.max_x = max_x
        self.max_y = max_y
        self.cell_list = cell_list


class Cell:

    def __init__(self, number):
        self.number = number

    def get_pos(self, dungeon):
        # Since the cell number goes from bottom left to top right
        # it does not matter what max_y is.
        # max_y information is already contained in the cell number.
        return [self.number // dungeon.max_x,
                self.number % dungeon.max_x]


class BlankCell(Cell):

    def __init__(self, number):
        super().__init__(number)
        self.description = 'nothing interesting'


class WallCell(Cell):

    def __init__(self, number):
        super().__init__(number)
        self.description = 'impassable terrain'


class MonsterCell(Cell):

    def __init__(self, number):
        super().__init__(number)
        self.description = 'something sinister'


class TreasureCell(Cell):

    def __init__(self, number):
        super().__init__(number)
        self.description = 'shiny treasures'


"""GLOBALS"""

# % chance of encountering each type of cell
# should add up to 1
CELL_PERCENTS = [.35, .6, .9, 1]

CELL_CATEGORIES = {
    # Category mapping for the cells

    0: BlankCell,
    1: WallCell,
    2: MonsterCell,
    3: TreasureCell
}


"""FUNCTIONS"""


def create_new_dungeon(max_x, max_y):
    # Set up a new modules
    print('Setting up modules...\n')

    cell_list = []
    dungeon = Dungeon(max_x, max_y, cell_list)  # Instantiate a new Dungeon

    for i in range(max_x * max_y):
        r = random()
        c = len(CELL_PERCENTS) - 1  # c = category (of the cell)
        for p in range(c):
            if CELL_PERCENTS[p] <= r < CELL_PERCENTS[p + 1]:
                c = p
                break

        cell_list.append(CELL_CATEGORIES[c](i))

    return dungeon
