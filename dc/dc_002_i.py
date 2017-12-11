# Daily Challenge #002 [Intermediate]: Text Adventure

# Key takeaways:

command_dict = {
    'W': 'Moved North',
    'A': 'Moved West',
    'S': 'Moved South',
    'D': 'Moved East',
    'E': 'Looked around...'
}

cell_dict = {
    # % chance of encountering each type of cell
    0: .35,  # blank
    1: .25,  # wall
    2: .3,  # monster
    3: .1  # treasure
}


def process_cell_dict(d):
    # Create an array containing the % chance that a particular cell will appear
    # based on a cell dictionary

    cell_dist_list = []
    s = 0
    for i in range(len(list(d.values()))):
        s = round(s + d[i], 2)
        cell_dist_list.append(s)
    print(cell_dist_list)
    return cell_dist_list


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


def create_new_dungeon(max_x, max_y):
    # Set up a new dungeon
    print('Setting up dungeon...\n')

    cell_list = []
    dungeon = Dungeon(max_x, max_y, cell_list)

    for i in range(max_x * max_y):
        cell_list.append(Cell(i))

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
          "Escape from the dungeon. Enter 'W', 'A', 'S', 'D' to move.\n"
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
    cell_dist_list = process_cell_dict(cell_dict)
    dungeon = create_new_dungeon(10, 10)
    # start_taking_input()


program()
