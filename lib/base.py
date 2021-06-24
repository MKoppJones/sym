from .runner import Runner
from .entity import Entity
import time

class Locale(Runner):
    def __init__(self, count):
        self.count = count
        self.alive: list[Entity] = []
        self.deceased: list[Entity] = []
        for x in range(self.count):
            self.alive.append(Entity(x))

    def run(self):
        curr_time = int(time.time())
        for x in self.alive:
            x.life_tick(curr_time)
            if x.alive:
                x.live(curr_time)
            else:
                self.deceased.append(x)
                self.alive.remove(x)