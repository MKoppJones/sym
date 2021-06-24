import time

class Entity:
    def __init__(self, num): 
        self.num = num
        self.hunger = 100
        self.born_at = int(time.time())
        self.age = 0
        self.alive = True
        self.last_update = self.born_at

    def _generate_label(self):
        return f'Entity{{{self.num}}} - Age: {self.age} - Hunger: {self.hunger} | '

    def life_tick(self, curr_time):
        if curr_time > self.last_update:
            self.age = curr_time - self.born_at
            self.alive = self.age < 9
            self.hunger -= 1
            self.last_update = curr_time
    
    def live(self, curr_time):
        self.breath()

    def breath(self):
        if self.alive:
            print(f"{self._generate_label()} breathed")