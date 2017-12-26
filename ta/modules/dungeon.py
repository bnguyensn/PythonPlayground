"""Contain codes related to setting up a dungeon"""

from random import random

import sys, os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import ta.modules.creature as creature

"""CLASSES"""


class Dungeon:

    def __init__(self, max_x, max_y, cell_list):
        self.max_x = max_x
        self.max_y = max_y
        self.cell_list = cell_list

    def get_blank_cells(self):
        return [cell for cell in self.cell_list if type(cell).__name__ == 'BlankCell']


class Cell:

    def __init__(self, dungeon, number):
        self.dungeon = dungeon
        self.number = number

    def get_pos(self):
        # Since the cell number goes from bottom left to top right
        # it does not matter what max_y is.
        # max_y information is already contained in the cell number.
        return [self.number // self.dungeon.max_x,
                self.number % self.dungeon.max_x]


class BlankCell(Cell):

    def __init__(self, *args):
        super().__init__(*args)
        self.description = 'nothing interesting'


class WallCell(Cell):

    def __init__(self, *args):
        super().__init__(*args)
        self.description = 'impassable terrain'


class HoleCell(Cell):

    def __init__(self, *args):
        super().__init__(*args)
        self.description = 'a dark hole of unknown depth'


"""GLOBALS"""

# % chance of encountering each type of cell
# goes towards 1
CELL_PERCENTS = [.6, .9, 1]

CELL_CATEGORIES = {
    # Category mapping for the cells

    0: BlankCell,
    1: WallCell,
    2: HoleCell
}


"""FUNCTIONS"""


def init_monsters(dungeon):
    count = 0

    for blank_cell in dungeon.get_blank_cells():
        if random() <= .5:  # 50% chance to place a monster on a blank cell
            pos_x = blank_cell.get_pos()[0]
            pos_y = blank_cell.get_pos()[1]
            creature.Skeleton(dungeon, pos_x, pos_y)

            count += 1

    print('Placed a total of {} monsters.'.format(count))


def create_new_dungeon(max_x, max_y):
    print('Setting up dungeon...')

    # Build the dungeon

    cell_list = []
    dungeon = Dungeon(max_x, max_y, cell_list)  # Instantiate a new Dungeon

    for i in range(max_x * max_y):
        r = random()
        c = len(CELL_PERCENTS) - 1  # c = category (of the cell)
        for p in range(c):
            if CELL_PERCENTS[p] <= r < CELL_PERCENTS[p + 1]:
                c = p
                break

        cell_list.append(CELL_CATEGORIES[c](dungeon, i))

    # Place creatures

    init_monsters(dungeon)

    # End of process

    return dungeon
