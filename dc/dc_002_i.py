# Daily Challenge #002 [Intermediate]: Text Adventure

# Key takeaways:

command_dict = {
    'W': 'Moved North',
    'A': 'Moved West',
    'S': 'Moved South',
    'D': 'Moved East',
    'E': 'Looked around...'
}


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

    def __init__(self, dungeon, number, category):
        self.dungeon = dungeon
        self.number = number
        self.category = category

    def get_pos(self):
        # Since the cell number goes from bottom left to top right
        # it does not matter what the max_y is.
        # max_y information is already contained in the cell number.
        return [self.number // self.dungeon.max_x,
                self.number % self.dungeon.max_x]


def dungeon_setup(max_x, max_y):
    # Set up dungeon
    print('Setting up dungeon...\n')

    cell_list = []
    dungeon = Dungeon(max_x, max_y, cell_list)
    for i in range(max_x * max_y):
        cell_list.append(Cell(dungeon, i, 0))

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
    dungeon = dungeon_setup(10, 10)

    start_taking_input()


program()
