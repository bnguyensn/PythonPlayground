# Daily Challenge #001 [Easy]: Printing Information

# Key takeaways:
# Format input
# Error handling
# The any() function
# The str.title() type

from string import whitespace
from string import digits


def program():
    print('Welcome to the info printer!\n'
          "Please follow the instructions, or type 'exit' anytime to quit.\n")

    class NameWithDigits(Exception):  # Catch name with digits error
        pass

    class AgeNegative(Exception):  # Catch negative age input error
        pass

    class UsernameWithSpaces(Exception):  # Catch username with whitespaces error
        pass

    while True:
        try:
            # Name
            while True:
                try:
                    inp_name = input('Enter your name: ')
                    if inp_name == 'exit':
                        raise KeyboardInterrupt
                    elif any(digit in inp_name for digit in digits):
                        raise NameWithDigits
                    break
                except NameWithDigits:
                    print('*** Error: name should not contain numbers.')

            # Age
            while True:
                try:
                    inp_age = input('Enter your age: ')
                    if inp_age == 'exit':
                        raise KeyboardInterrupt
                    elif int(inp_age) < 0:
                        raise AgeNegative
                    break
                except ValueError:
                    print('*** Error: age must be a positive integer.')
                except AgeNegative:
                    print('*** Error: age must not be less than 0.')

            # Username
            while True:
                try:
                    inp_username = input('Enter your username: ')
                    if inp_username == 'exit':
                        raise KeyboardInterrupt
                    elif any(ws in inp_username for ws in whitespace):
                        raise UsernameWithSpaces
                    break
                except UsernameWithSpaces:
                    print('*** Error: username should not contain spaces.')

            # Print result
            print('Your name is {}, you are {} y/o, and your username is {}.'
                  .format(inp_name.title(), inp_age, inp_username))
        except (KeyboardInterrupt, SystemExit):
            print('Goodbye!')
            break


program()
