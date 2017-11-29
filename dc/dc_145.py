# Daily Challenge #145 [Easy]: Tree Generation

# Key takeaways:
# rounding integer
# input validation
# catch KeyboardInterrupt and SystemExit, and custom exceptions
# raise Exception to break out of nested loops (the only other way is using return)
# check if variable is integer
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


def tree_generator():

    def check_tree_base_width_int(w):
        try:
            int(w)
            return True
        except ValueError:
            raise TreeBaseWidthNotInteger

    # Overall try/except to catch exit conditions
    while True:
        try:
            # Determine the tree's inputs using format "n # *"
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
                    inp = input("Enter the tree drawing input e.g. 7 # *:")
                    inp_arr = list(inp.replace(' ', ''))
                    print(inp_arr)
                    if len(inp_arr) > 3:
                        raise TooManyInputs
                    elif len(inp_arr) < 3:
                        raise TooFewInputs
                    elif check_tree_base_width_int(inp_arr[0]):
                        inp_arr[0] = int(inp_arr[0])
                    elif inp_arr[0] < 3:
                        raise TreeBaseWidthTooSmall
                    else:
                        break
                except TooManyInputs:
                    print('WARNING: You have entered too many inputs.')
                except TooFewInputs:
                    print('WARNING: You have entered too few inputs.')
                except (TreeBaseWidthNotInteger,):
                    print('WARNING: Please enter a valid integer for the tree base width.')
                except TreeBaseWidthTooSmall:
                    print("WARNING: The tree's base width should not be less than 4 (unless it's 0"
                          " which means to exit).")


            """# Determine the tree's base width, which should not be < 4
            while True:
                try:
                    inp_tree_base_width = int(input("Enter the tree's base width (or 0 to exit):"))
                    if inp_tree_base_width == 0:
                        raise KeyboardInterrupt
                    elif inp_tree_base_width > 3:
                        break
                    else:
                        print("WARNING: The tree's base width should not be less than 4 (unless it's 0"
                              " which means to exit).")
                        continue
                except ValueError:
                    print('WARNING: Please enter a valid integer.')"""

            # Convert tree base width to integer
            inp_tree_base_width = inp_arr[0]
            # Reassign variables for clarity
            inp_trunk_sym = inp_arr[1]
            inp_tree_sym = inp_arr[2]
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
