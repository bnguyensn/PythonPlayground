# Daily Challenge #224 [Easy]: Shuffling List

# Key takeaways:
# Shuffling list

from random import randint

inputString = 'apple blackberry cherry dragonfruit grapefruit kumquat mango nectarine persimmon raspberry raspberry' \
              ' a e i o u'


def shuffle_basic(inp_str, iteration):
    # Idea:
    # Each item in the input list has an ID
    # Take a random ID, remove it out of the ID list and put it in the "Shuffled" list
    # Repeat this on the remaining items in the ID list
    # End when there are no items remaining

    for i in range(0, iteration):
        inp_arr = inp_str.split(' ')
        shuffled_list_arr = []

        i = 0
        while i < len(inp_arr):
            n = randint(0, len(inp_arr) - 1)
            shuffled_list_arr.append(inp_arr[n])
            del inp_arr[n]
        print(' '.join(shuffled_list_arr))


shuffle_basic(inputString, 5)
