from threading import Timer
import time

t = 2.  # Time it takes to open/close fully


class Door:
    def __init__(self, duration):
        self.state = 0
        self.startTime = time.time()
        self.pauseTime = 0
        self.timer = Timer(duration, self.finish)
        self.stateString = {
            "0": "CLOSED",
            "1": "OPENING",
            "2": "OPEN",
            "3": "CLOSING",
            "4": "STOPPED_WHILE_OPENING",
            "5": "STOPPED_WHILE_CLOSING"
        }

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.cancel()

    def pause(self):
        self.pauseTime = time.time()
        self.timer.cancel()

    def resume(self):
        self.timer = Timer(self.pauseTime - self.startTime, self.finish())
        self.timer.start()

    def finish(self):
        print("Cycle complete")

    def toggle(self):
        if self.state == 0:
            self.start()
            self.state = 1
        elif self.state == 1:
            self.pause()
            self.state = 4
        elif self.state == 2:
            self.start()
            self.state = 3
        elif self.state == 3:
            self.pause()
            self.state = 5
        elif self.state == 4:
            self.resume()
            self.state = 3
        elif self.state == 5:
            self.resume()
            self.state = 1

    def get_state(self):
        print("Door: " + self.stateString[str(self.state)])


def click(door):
    print("Button clicked.")
    door.toggle()
    door.get_state()

door = Door(t)

door.get_state()
click(door)
