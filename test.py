from random import randint

for i in range(10):
    x = randint(1,3)
    y = randint(1,3)
    print("x = %s, y = %s" % (x, y))
    if x == y:
        print("True")
    else:
        print("False")

print("Hello world")