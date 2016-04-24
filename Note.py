"""imports the datetime function in the datetime library"""
from datetime import datetime
import math
from threading import Timer

name = "john"
lastname = "doe"

print("%s %s" % (name, lastname))

now = datetime.now()

print("%s/%s/%s %s:%s:%s" % (now.day, now.month, now.year, now.hour, now.minute, now.second))

# Comparative order: not >> and >> or


def foo1(*args):  # Multiple arguments
    print(max(args))


foo1(1, 2, 3, 4, 5, -1)

numbers = [1, 2, 3, 4]
numbersSqr = []
numbers.index(1)
numbers.insert(0, 0)
numbers.append(5)
for i in numbers:
    numbersSqr.append(i ** 2)
print(numbersSqr)

inventory = {
    "gold": 200,
    "rucksack": ["dagger", "flint", "lockpick", "map", "acorn"]
}
inventory["rucksack"].remove("flint")
inventory["rucksack"].sort()
print(inventory)

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def compute_bill(food):
    total = 0
    for key in food:
        total += food[key]
    return total

n = [3, 5, 7]


def print_list(x):
    for i in range(0, len(x)):
        print(x[i])

range(6)  # => [0,1,2,3,4,5] (Stop)
range(1, 6)  # => [1,2,3,4,5] (Start, Stop)
range(1, 6, 3)  # => [1,4] (Start, Stop, Step)

word = "Word"
for i in word:
    print(i)  # This will print W, o, r, d on separate lines
for i in word:
    print(i, end=" ")  # This will print W, o, r, d on the same line, with one space between each letter
print("\n")

#  The Index Enumerate For method:
choices = ['pizza', 'pasta', 'salad', 'nachos']
print('Your choices are:')
for index, item in enumerate(choices):
    print(index + 1, item)
print("\n")

#  The Zip method:
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):
    print(max(a, b))
print("\n")

# List of numbers from 0 to 50 (incl.)
my_list = range(51)

# List comprehension
evens_to_50 = [i for i in range(51) if i % 2 == 0]  # All even numbers from 0 to 50 (incl.)
doubled_divisible_by_3 = [x*2 for x in range(1, 6) if (x*2) % 3 == 0]
c = ['C' for x in range(5) if x < 3]  # Contains 3 Cs

# List slicing: lst[start:end:stride] (inclusive:exclusive:space btw items) default[0:end:1] e.g. lst[::]
# Note: [0:end:1] end is exclusive so if i = end (starting from 0) will not iterate

# List reversing: lst[::-x] i.e. traversing from right to left

# Functional programming lambda
my_list_lambda = range(16)
filter(lambda x: x % 3 == 0, my_list_lambda)

# Iterating over dictionaries
inventory.items()
inventory.keys()
inventory.values()

# Bitwise operators
""" Bitwise operators
5 >> 4  # Right Shift
5 << 1  # Left Shift
8 & 5   # Bitwise AND
9 | 4   # Bitwise OR
12 ^ 42 # Bitwise XOR, either corresponding bits are 1, but NOT both
~88     # Bitwise NOT, flips all the bits i.e. adding 1 and make negative ~88 = -89

print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b1 + 0b11
print 0b11 * 0b11
"""
bin(1)  # int -> binary
oct(1)  # int -> base 8
hex(1)  # int -> base 16
int("110", 2)  # Convert "110" in base 2 to base 10

# Classes


class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        return False


class Equilateral(Triangle):
    angle = 60

    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle

# File I/O:
f = open("output.txt", "w")
"""
Open output.txt in "write" mode, storing the result in file object f
Other modes: "r+" (read and write), "r" (read)
"""
f.write("something" + "\n")  # Remember to convert to string
f.read()
f.readline()
f.close()  # Must close the file i.e. flush the buffer i.e. ensuring data will make it to the target file

if not f.closed:
    f.close()

with open("output.txt", "w") as f:  # Invoke a file object's __exit__ method i.e. file will .close() automatically
    f.write("something")

t = 3.


class Door:
    def __init__(self, duration):
        self.duration = duration
        self.T = Timer(self.duration, self.foo)

    def foo(self):
        print("Hello world.")

    def start(self):
        self.T.start()

my_door = Door(t)
my_door.start()