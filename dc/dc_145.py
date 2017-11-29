# Daily Challenge #145 [Easy]: Tree Generation

# Key takeaways:
# rounding integer up

from math import ceil

inp_trunk_count = 3
inp_trunk_sym = '#'
inp_leaves_init_count = 7
inp_leaves_sym = '*'
inp_leaves_step_count = 2


def create_tree(trunk_count, trunk_sym, leaves_init_count, leaves_sym, leaves_step_count):
    height = int(ceil(leaves_init_count / leaves_step_count))

    for i in range(1, height + 1):
        print(' ' * int((leaves_step_count / 2)) * (height - i) + leaves_sym * (1 + leaves_step_count * (i - 1)))


create_tree(inp_trunk_count, inp_trunk_sym, inp_leaves_init_count, inp_leaves_sym, inp_leaves_step_count)
