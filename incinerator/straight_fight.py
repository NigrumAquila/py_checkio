class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0

    def hit(self, other):
        other.loss(self.attack)

    def damage(self, attack):
        return attack

    def loss(self, attack):
        self.health -= self.damage(attack)


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3)
        self.defense = 2

    def damage(self, attack):
        return max(0, attack - self.defense)


class Vampire(Warrior):
    def __init__(self):
        super().__init__(health=40, attack=4)
        self.vampirism = 50

    def hit(self, other):
        super().hit(other)
        self.health += other.damage(self.attack) * self.vampirism // 100


class Lancer(Warrior):
    def __init__(self):
        super().__init__(attack=6)


class Healer(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=0)
        self.heal_rate = 2

    def heal(self, other):
        other.health += self.heal_rate


def fight(unit_1, unit_2):
    while 1:
        unit_1.hit(unit_2)
        if unit_2.health <= 0:
            return True
        unit_2.hit(unit_1)
        if unit_1.health <= 0:
            return False


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_class, count):
        for _ in range(count):
            self.units.append(unit_class())

    @property
    def first_alive_unit(self):
        for unit in self.units:
            if unit.is_alive:
                return unit

    def next_unit(self, unit):
        i = self.units.index(unit)
        if i + 1 < len(self.units):
            return self.units[i + 1]

    @property
    def is_alive(self):
        return self.first_alive_unit is not None

    @property
    def alive_units(self):
        return [u for u in self.units if u.is_alive]


class Battle:
    @staticmethod
    def hit(army_1, army_2):
        unit_1 = army_1.first_alive_unit
        unit_2 = army_2.first_alive_unit

        unit_22 = army_2.next_unit(unit_2)
        unit_1.hit(unit_2)
        if unit_22 and isinstance(unit_1, Lancer):
            unit_22.loss(unit_1.attack // 2)

        unit_12 = army_1.next_unit(unit_1)
        if unit_12 and isinstance(unit_12, Healer):
            unit_12.heal(unit_1)

    @classmethod
    def fight(cls, army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            unit_1 = army_1.first_alive_unit
            unit_2 = army_2.first_alive_unit
            while 1:
                cls.hit(army_1, army_2)
                if unit_2.health <= 0:
                    break
                cls.hit(army_2, army_1)
                if unit_1.health <= 0:
                    break
        return army_1.is_alive

    @classmethod
    def straight_fight(cls, army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            for unit_1, unit_2 in zip(army_1.alive_units, army_2.alive_units):
                fight(unit_1, unit_2)
        return army_1.is_alive