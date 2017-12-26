"""Contain codes related to processing user inputs"""

command_dict = {
    # List valid user inputs

    'W': 'Moved North',
    'A': 'Moved West',
    'S': 'Moved South',
    'D': 'Moved East',
    'E': 'Looked around...'
}


def process_input(inp, player):
    x, y = player.pos_x, player.pos_y
    dd = {
        # direction_dict
        'W': [x, y + 1],
        'A': [x + 1, y],
        'S': [x, y - 1],
        'D': [x - 1, y],
    }

    if inp == 'E':
        print('You are at {player_pos_x}, {player_pos_y}.\n'
              'To your North is {cell_north}.\n'
              'To your East is {cell_east}.\n'
              'To your South is {cell_south}.\n'
              'To your West is {cell_west}.\n'
              .format(player_pos_x=x,
                      player_pos_y=y,
                      cell_north=player.dungeon.get_cell_from_xy(dd['W'][0], dd['W'][1]).get_content(),
                      cell_east=player.dungeon.get_cell_from_xy(dd['D'][0], dd['D'][1]).get_content(),
                      cell_south=player.dungeon.get_cell_from_xy(dd['S'][0], dd['S'][1]).get_content(),
                      cell_west=player.dungeon.get_cell_from_xy(dd['A'][0], dd['A'][1]).get_content()))
    else:
        target_x, target_y = dd[inp][0], dd[inp][1]
        target_cell = player.dungeon.get_cell_from_xy(target_x, target_y)
        target_content = target_cell.content

        if target_content is None:
            player.move(target_x, target_y)
        else:
            player.attack(target_content)


def input_is_valid(inp):
    class InputInvalid(Exception):
        pass

    try:
        if inp not in list(command_dict.keys()):
            raise InputInvalid
        return True
    except InputInvalid:
        print('Invalid command. Please try again')
        return False


def start_taking_input(player):
    print('Welcome to Text Adventure, {player_name}\n\n'
          "Escape from the dungeon. Enter 'W', 'A', 'S', 'D' to move.\n"
          "Enter 'E' to interact.\n"
          "Enter 'exit' to quit.\n\n"
          .format(player_name=player.name))

    while True:
        try:
            inp = input('Enter a command: ').upper()

            # Check if user want to exit
            if inp == 'EXIT':
                raise KeyboardInterrupt

            # Check if entered command is valid
            # Process command if so, else restart the loop
            if input_is_valid(inp):
                process_input(inp, player)
            else:
                continue
        except (KeyboardInterrupt, SystemError):
            print('Goodbye!')
            break
