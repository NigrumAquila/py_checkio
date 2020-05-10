class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
    
    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        super().__init__(health, attack)


class Army:
    def __init__(self):
        self.army = []

    def add_units(self, unit, number):
        self.army += [unit() for _ in range(number)]

    @property
    def is_alive(self):
        return any([x.is_alive for x in self.army])


class Battle:
    def fight(self, army_1, army_2):
        idx_1, idx_2 = 0, 0
        while army_1.is_alive and army_2.is_alive:
            if fight(army_1.army[idx_1], army_2.army[idx_2]):
                idx_2 += 1
            else:
                idx_1 += 1
        return army_1.is_alive


def fight(unit_1, unit_2):    
    while unit_1.is_alive and unit_2.is_alive:        
        unit_2.health -= unit_1.attack        
        if unit_2.is_alive:
            unit_1.health -= unit_2.attack
    return unit_1.is_alive