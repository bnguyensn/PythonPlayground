# Daily Challenge #145 [Easy]: Tree Generation

# Key takeaways:
# rounding integer
# input validation
# catch KeyboardInterrupt and SystemExit

import math

inp_trunk_sym = '#'
inp_tree_sym = '*'


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
    while True:
        try:
            # Determine the tree's base width, which should not be < 4
            while True:
                try:
                    inp_tree_base_width = int(input("Enter the tree's base width (or 0 to exit):"))
                    if inp_tree_base_width == 0 or inp_tree_base_width > 3:
                        break
                    else:
                        print("WARNING: The tree's base width should not be less than 4 (unless it's 0"
                              " which means to exit).")
                        continue
                except ValueError:
                    print('WARNING: Please enter a valid integer.')

            # Exit if tree_base_width is 0
            if inp_tree_base_width == 0:
                print('Goodbye!')
                break
            else:
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
