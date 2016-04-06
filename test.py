from threading import Timer

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
