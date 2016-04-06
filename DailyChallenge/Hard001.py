"""Reverse guessing game"""

from random import randint

range_low = 1
range_high = 100
answer_list = ["c", "h", "l"]
stat_efficient = True  # True = Enable statistically efficient calculations i.e. no random guesses.

try_count = 0
x = int((range_high + range_low) / 2) if stat_efficient else randint(range_low, range_high)

# Game starts
input("Think of an integer between %s and %s. \nPress 'Enter' when ready." % (range_low, range_high))

while True:
    answer = str(input("I think the number is %s? Is this this answer correct/too high/too low? Answer with C/H/L" % x)
                 ).lower()
    if answer in answer_list:  # Appropriate input
        try_count += 1
        if answer == "c":
            print("I've guessed it after %s tries! \nGame over." % try_count)
            break
        else:
            if answer == "h":
                range_low = x + 1
            else:
                range_high = x - 1
            if range_low >= range_high:
                print("The number must be %s. I've guessed it after %s tries! \nGame over." % (range_low, try_count))
                break
            else:
                x = int((range_high + range_low) / 2) if stat_efficient else randint(range_low, range_high)
    else:
        print("Please answer with either 'C', 'H' or 'L' (non-case-sensitive)")
