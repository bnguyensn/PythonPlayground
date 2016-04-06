"""Reverse guessing game"""

from math import isnan
from random import randint

range_low = 1
range_high = 100
answer_list = ["c", "h", "l"]
stat_efficient = False  # True = Enable statistically efficient calculations i.e. no random guesses.

try_count = 0
x = int((range_high + range_low) / 2) if stat_efficient else randint(range_low, range_high)

# Game starts
c = input("Think of an integer between %s and %s.\nPress 'Enter' when ready."
          "\nOptional: input an integer to let the computer plays with itself!" % (range_low, range_high))

try:
    isnan(int(c))
    c = int(c)
except ValueError:
    c = None

if c is None:
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
else:
    if c <= 0:
        print("Negative integers are not allowed, the computer shall play itself for one round!")
        c = 1
    for i in range(c):
        r_low = range_low
        r_high = range_high
        y = randint(r_low, r_high)
        x = int((r_high + r_low) / 2) if stat_efficient else randint(r_low, r_high)
        # print("New round: y = " + str(y))
        while True:
            # print("guess: x = " + str(x))
            try_count += 1
            if x == y:
                break
            else:
                if x < y:
                    r_low = x + 1
                else:
                    r_high = x - 1
                if r_low >= r_high:
                    break
                else:
                    x = int((r_high + r_low) / 2) if stat_efficient else randint(r_low, r_high)
    try_average = try_count / c
    print("Final statistics:\nNumber of rounds: %s\nNumber of tries: %s\nAverage guesses: %s" % (c, try_count, try_average))


