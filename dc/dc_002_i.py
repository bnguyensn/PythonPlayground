# Daily Challenge #002 [Intermediate]: Text Adventure

# Key takeaways:

from random import random

command_dict = {
    'W': 'Moved North',
    'A': 'Moved West',
    'S': 'Moved South',
    'D': 'Moved East',
    'E': 'Looked around...'
}

cell_percents_d = {
    # % chance of encountering each type of cell
    0: .35,  # blank
    1: .25,  # wall
    2: .3,  # monster
    3: .1  # treasure
}


def process_cell_dict(d):
    # Create an array containing the % chance that a particular cell will appear
    # based on a cell dictionary

    cell_percents, s = [], 0
    for i in range(len(list(d.values()))):
        s = round(s + d[i], 2)
        cell_percents.append(s)
    return cell_percents


def move(direction):
    pass


def prompt(message):
    pass


"""Dungeon & cells"""


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


cell_categories_d = {
    # Category mapping for the cells
    0: BlankCell,
    1: WallCell,
    2: MonsterCell,
    3: TreasureCell
}


def create_new_dungeon(max_x, max_y, cell_percents, cell_categories):
    # Set up a new modules
    print('Setting up modules...\n')

    cell_list = []
    dungeon = Dungeon(max_x, max_y, cell_list)

    for i in range(max_x * max_y):
        r = random()
        c = len(cell_percents) - 1  # c = category (of the cell)
        for p in range(c):
            if cell_percents[p] <= r < cell_percents[p + 1]:
                c = p
                break

        cell_list.append(cell_categories[c](i))

    return dungeon


"""Process input"""


def process_input(inp):
    print(command_dict[inp])


def check_input(inp):
    class InputInvalid(Exception):
        pass

    try:
        if inp not in list(command_dict.keys()):
            raise InputInvalid
        return True
    except InputInvalid:
        print('Invalid command. Please try again')
        return False


def start_taking_input():
    # Start taking input
    print('Welcome to Text Adventure\n\n'
          "Escape from the modules. Enter 'W', 'A', 'S', 'D' to move.\n"
          "Enter 'E' to interact.\n"
          "Enter 'exit' to quit.\n\n")

    while True:
        try:
            inp = input('Enter a command: ').upper()

            # Check if user want to exit
            if inp == 'EXIT':
                raise KeyboardInterrupt

            # Check if entered command is valid
            # Process command if so, else restart the loop
            if check_input(inp):
                process_input(inp)
            else:
                continue
        except (KeyboardInterrupt, SystemError):
            print('Goodbye!')
            break


"""Let's go baby!"""


def program():
    cell_percents = process_cell_dict(cell_percents_d)
    print(cell_percents)

    dungeon = create_new_dungeon(10, 10, cell_percents, cell_categories_d)
    category_count = {}
    for cell in dungeon.cell_list:
        cell_name = cell.__class__.__name__
        if cell_name in category_count:
            category_count[cell_name] += 1
        else:
            category_count[cell_name] = 1
    print(category_count)

    # start_taking_input()


program()
