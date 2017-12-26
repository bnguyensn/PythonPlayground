"""Contain codes related to setting up a dungeon"""

from random import random, randrange
from math import ceil

import sys, os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import ta.modules.creature as creature


"""CLASSES"""


class Dungeon:

    def __init__(self, max_x, max_y, cell_list, player):
        self.max_x = max_x
        self.max_y = max_y
        self.cell_list = cell_list
        self.player = player
        self.oob = OutOfBoundCell(self, -1, None)

    def get_blank_cells(self):
        return [cell for cell in self.cell_list if type(cell).__name__ == 'BlankCell']

    def is_xy_inbound(self, x, y):
        return 1 <= x <= self.max_x and 1 <= y <= self.max_y

    def get_cell_from_xy(self, x, y):
        if self.is_xy_inbound(x, y):
            # Array starts from 0, cell no. starts from 1
            cell_number = (((y - 1) * self.max_x) + x)
            return self.cell_list[cell_number - 1]
        return self.oob


class Cell:

    def __init__(self, dungeon, number, content):
        self.dungeon = dungeon
        self.number = number
        self.content = content

    def get_pos(self):
        # Since the cell number goes from bottom left to top right
        # it does not matter what max_y is.
        # max_y information is already contained in the cell number.
        y = ceil(self.number / self.dungeon.max_x)
        x = self.number - self.dungeon.max_x * (y - 1)
        return [x, y]

    def get_content(self):
        if self.content is None:
            return type(self).__name__
        return self.content.name


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


class OutOfBoundCell(Cell):

    def __init__(self, *args):
        super().__init__(*args)
        self.description = 'out of bound'


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


def init_player(dungeon):
    blank_cells = dungeon.get_blank_cells()
    starting_cell = blank_cells[randrange(len(blank_cells))]
    starting_cell_pos = starting_cell.get_pos()

    dungeon.player = creature.Player(dungeon, starting_cell_pos[0], starting_cell_pos[1])

    print('Placed Player at cell #{} ({}, {}).'.format(starting_cell.number, starting_cell_pos[0], starting_cell_pos[1]))


def init_monsters(dungeon):
    count = 0

    for blank_cell in dungeon.get_blank_cells():
        if random() <= .5:  # 50% chance to place a monster on a blank cell
            pos = blank_cell.get_pos()
            blank_cell.content = creature.Skeleton(dungeon, pos[0], pos[1])

            count += 1

    print('Placed a total of {} monsters.'.format(count))


def create_new_dungeon(max_x, max_y):
    print('Setting up dungeon...')

    # Build the dungeon

    cell_list = []
    dungeon = Dungeon(max_x, max_y, cell_list, None)  # Instantiate a new Dungeon

    for i in range(1, (max_x * max_y) + 1):
        r = random()
        c = len(CELL_PERCENTS) - 1  # c = category (of the cell)
        for p in range(c):
            if CELL_PERCENTS[p] <= r < CELL_PERCENTS[p + 1]:
                c = p
                break

        cell_list.append(CELL_CATEGORIES[c](dungeon, i, None))  # Array starts from 0, cell no. starts from 1

    # Place creatures

    init_monsters(dungeon)

    # Place Player

    init_player(dungeon)

    # End of process

    return dungeon
