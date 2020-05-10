import itertools


class Warrior:
    def __init__(self):
        self._health = 50
        self._attack = 5

    @property
    def is_alive(self):
        return self._health > 0

    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, health):
        self._health = health
    
    @property
    def attack(self):
        return self._attack
    
    @attack.setter
    def attack(self, attack_power):
        self._attack = attack_power

    def attack_enemy(self, enemy: object) -> None:
        dmg = self._attack
        return enemy.take_damage(dmg)
        
    def take_damage(self, dmg: int) -> int:
        self._health -= dmg
        return dmg


class Knight(Warrior):
    def __init__(self):
        super(Knight, self).__init__()
        self._attack += 2


class Defender(Warrior):
    def __init__(self):
        super(Defender, self).__init__()
        self._health += 10
        self._attack -= 2
        self._defense = 2
        
    def take_damage(self, dmg: int) -> int:
        final_dmg = dmg - self._defense
        if final_dmg > 0:
            self._health -= final_dmg
        return final_dmg


class Vampire(Warrior):
    def __init__(self):
        super(Vampire, self).__init__()
        self._health -= 10
        self._attack -= 1
        self._vampirism = 0.5
        
    def attack_enemy(self, enemy: object):
        dmg_done = super(Vampire, self).attack_enemy(enemy)
        self._health += dmg_done * self._vampirism
        return dmg_done


def fight(unit_1, unit_2):
    for i in itertools.count():
        if not i % 2:
            # Unit 1 attack
            unit_1.attack_enemy(unit_2)
            if not unit_2.is_alive:
                return True
        else:
            # Unit 2 attack
            unit_2.attack_enemy(unit_1)
            if not unit_1.is_alive:
                return False


class Army(object):
    def __init__(self):
        self._units = []
        self._index = 0

    @property
    def is_alive(self):
        return self._index < len(self._units)
        
    def add_units(self, unit_type, number):
        self._units.extend((unit_type() for i in range(number)))
        
    def get_unit(self):
        return self._units[self._index]
    
    def unit_is_death(self):
        self._index += 1


class Battle(object):
    @staticmethod
    def fight(army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            if fight(army_1.get_unit(), army_2.get_unit()):
                army_2.unit_is_death()
            else:
                army_1.unit_is_death()
        return army_1.is_alive