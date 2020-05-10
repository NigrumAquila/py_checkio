class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0

    def take_hit(self, hit):
        self.health -= hit
        return hit

    def do_attack(self, other1, other2 = None, **options):
        hit = options.get('hit', self.attack)
        return other1.take_hit(hit)

class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.attack = 6

    def do_attack(self, other1, other2 = None, **options):
        damage = super().do_attack(other1)
        damage2 = super().do_attack(other2, None, hit = damage / 2) if other2 else 0
        return damage + damage2

class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5

    def do_attack(self, other1, other2 = None, **options):
        damage = super().do_attack(other1)
        self.health += damage * self.vampirism
        return damage

class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2

    def take_hit(self, hit):
        return super().take_hit(max(0, hit - self.defense))

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

def fight(unit_1, unit_2):
    while True:
        unit_1.do_attack(unit_2)
        if not unit_2.is_alive:
            return True
        unit_2.do_attack(unit_1)
        if not unit_1.is_alive:
            return False

class Army:
    def __init__(self):
        self.units = []

    def add_units(self, klass, count):
        for i in range(count):
            self.units.append(klass())

    def cleanup(self):
        front_warrior_dead = self.units and not self.units[0].is_alive
        self.units = [u for u in self.units if u.is_alive]
        return front_warrior_dead

    def all_dead(self):
        return self.units == []

class Battle:
    def fight(self, army1, army2):
        army1_turn = True
        while not army1.all_dead() and not army2.all_dead():
            if army1_turn:
                army1.units[0].do_attack(*army2.units[:2])
            else:
                army2.units[0].do_attack(*army1.units[:2])
            army1_turn = not army1_turn

            front_warrior_dead1 = army1.cleanup()
            front_warrior_dead2 = army2.cleanup()
            if front_warrior_dead1 or front_warrior_dead2:
                army1_turn = True

        return army2.all_dead()