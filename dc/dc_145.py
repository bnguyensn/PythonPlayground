# Daily Challenge #145 [Easy]: Tree Generation

# Key takeaways:
# rounding integer
# input validation
# catch KeyboardInterrupt and SystemExit, and custom exceptions
# raise Exception to break out of nested loops (the only other way is using return)
# check if integer string is integer
# split string using empty separator

import math


def draw_tree(trunk_sym, tree_sym, tree_base_width, trunk_width, tree_step):
    # Calculate how tall the tree is
    height = int(math.ceil(tree_base_width / tree_step))

    # Calculate the top-level width
    tree_top_width = 1 if tree_base_width % 2 == 1 else 2

    # Calculate spacing for the trunk
    trunk_spacing = math.trunc((tree_base_width - trunk_width) / 2)

    # Draw leaves
    for i in range(height):
        print(' ' * math.trunc(tree_step / 2) * (height - i - 1) + tree_sym * (tree_top_width + tree_step * i))

    # Draw trunk
    print(' ' * trunk_spacing + trunk_sym * trunk_width)


def is_str_int(i):
    try:
        int(i)
        return True
    except ValueError:
        return False


def tree_generator():
    print('=== *** Welcome to the Tree Generator! *** ===')
    # Overall try/except to catch exit conditions
    while True:
        try:
            # Determine the tree's inputs using format "n#*"
            # List of possible errors:
            class TooManyInputs(Exception):
                pass

            class TooFewInputs(Exception):
                pass

            class TreeBaseWidthNotInteger(Exception):
                pass

            class TreeBaseWidthTooSmall(Exception):
                pass

            # Try/except to catch input formatting
            while True:
                try:
                    inp = input("Enter your parameters (e.g. 7 # *). "
                                "Enter 'exit' to exit: ")

                    if inp.lower() == 'exit':
                        raise KeyboardInterrupt

                    inp = inp.strip()  # Trim whitespaces

                    # Traverse the input to find the base width integer
                    # Create a copy of the input without the base width part at the same time
                    # Check that the tree base width is an integer, and not too small
                    inp_tree_base_width_str, inp_without_tree_base_width = '', ''
                    inp_index = 0
                    for c in inp:
                        if is_str_int(c):
                            inp_tree_base_width_str += c
                            inp_index += 1
                        else:
                            inp_without_tree_base_width = inp[inp_index:]
                            break
                    try:
                        inp_tree_base_width = int(inp_tree_base_width_str)
                        if inp_tree_base_width < 4:
                            raise TreeBaseWidthTooSmall
                    except ValueError:
                        raise TreeBaseWidthNotInteger

                    # Make sure not too many nor too few parameters were entered
                    sym_arr = list(inp_without_tree_base_width.replace(' ', ''))
                    if len(sym_arr) > 2:
                        raise TooManyInputs
                    elif len(sym_arr) < 2:
                        raise TooFewInputs
                    else:
                        break
                except TooManyInputs:
                    print('WARNING: You have entered too many parameters.')
                except TooFewInputs:
                    print('WARNING: You have entered too few parameters.')
                except (TreeBaseWidthNotInteger,):
                    print('WARNING: Please enter a valid integer for the tree base width.')
                except TreeBaseWidthTooSmall:
                    print("WARNING: The tree's base width should not be less than 4.")

            # Reassign variables for clarity
            inp_trunk_sym = sym_arr[0]
            inp_tree_sym = sym_arr[1]
            # This should not be larger than the tree base width
            inp_trunk_width = 3 if inp_tree_base_width % 2 == 1 else 2
            # This should be an even number, and less than the tree's base width
            inp_tree_step = 2

            print("Here's your tree:")
            draw_tree(inp_trunk_sym, inp_tree_sym, inp_tree_base_width, inp_trunk_width, inp_tree_step)
        except (KeyboardInterrupt, SystemExit):
            print('\nGoodbye!')
            break


tree_generator()
