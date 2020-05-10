class Warrior:
    def __init__(self):
        self.health, self.attack = 50, 5

    def is_attacked(self, other):
        if (other.is_alive):
            self.health -= other.attack

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        self.health, self.attack = 50, 7


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.is_attacked(unit_1)
        unit_1.is_attacked(unit_2)
    return unit_1.is_alive