# Daily Challenge #228 [Easy]: Alphabetical Order Letters

# Key takeaways:
# The ord(c) function which returns a letter's Unicode value
# The all(iterable) function
# Fast way to check if list is sorted numerically
# List comprehension

inp_str = 'billowy\n' \
      'biopsy\n' \
      'chinos\n' \
      'defaced\n' \
      'chintz\n' \
      'sponged\n' \
      'bijoux\n' \
      'abhors\n' \
      'fiddle\n' \
      'begins\n' \
      'chimps\n' \
      'wronged\n'


def is_alphabetical_order(text):
    # Convert all letters in the text to their corresponding alphabetical order
    converted_text = [ord(letter) for letter in text]

    # Check if the above array is sorted
    # The all(iterable) function returns TRUE if all elements of the iterable are true
    # or if the iterable is empty
    if all(converted_text[i] <= converted_text[i + 1] for i in range(len(converted_text) - 1)):
        return text + ' IN ORDER'
    return text + ' NOT IN ORDER'


def program(i):
    inp_list = i.strip().split('\n')
    for i in inp_list:
        print(is_alphabetical_order(i))


program(inp_str)
