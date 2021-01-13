import random


class Power:
    def __init__(self, name, cost, damage, type):
        # type defines its good or bad power
        # good one helps heal & bad ones damages
        super().__init__()
        self.name = name
        self.cost = cost
        self.damage = damage
        self.type = type

    def generate_damage(self):
        min = self.damage - 20
        max = self.damage + 20
        return random.randrange(min, max)
