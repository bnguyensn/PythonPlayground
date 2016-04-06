"""Reverse guessing game"""

from random import randint

range_low = 1
range_high = 100
answer_list = ["c", "h", "l"]

try_count = 0
x = randint(range_low, range_high)

# Game starts
print()
input("Think of an integer between %s and %s. \nPress 'Enter' when ready." % (range_low, range_high))

while True:
    answer = str(input("I think the number is %s? Is this this answer correct/too high/too low? Answer with C/H/L" % x)
                 ).lower()
    if answer in answer_list:  # Appropriate input
        try_count += 1
        if answer == "c":
            print("I've guessed it after %s tries! \nGame over." % try_count)
            break
        elif answer == "h":
            range_low = x + 1
            x = randint(range_low, range_high)
        else:
            range_high = x - 1
            x = randint(range_low, range_high)
    else:
        print("Please answer with either 'C', 'H' or 'L' (non-case-sensitive)")
