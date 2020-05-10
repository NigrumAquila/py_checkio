import math
class Army:
    def __init__(self):
        self.units = []
    def add_units(self,fighter,x):
        for i in range(x):
            self.units.append(fighter())
    def update(self):
        self.units = [x for x in self.units if x.is_alive]
            
    def hit(self,enemy):
        self.units[0].hit(enemy.units[0])
        if len(enemy.units)>1 and self.units[0].second_attack>0:
            enemy.units[1].health -= max(0, (max(0,self.units[0].attack-enemy.units[0].defense)*self.units[0].second_attack)-enemy.units[1].defense)
        if len(self.units)>1 and self.units[1].heal_power>0:
            self.units[1].heal(self.units[0])
        if len(self.units)>2 and self.units[2].heal_power>0:
            self.units[2].heal(self.units[1])
class Weapon:
    def __init__(self,h=0,a=0,d=0,v=0,hp=0):
        self.health = h
        self.attack = a
        self.defense = d
        self.vampirism = v
        self.heal_power = hp
    

    
class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self.attack = 2
        self.health = 5
        
class Shield(Weapon):
    def __init__(self):
        super().__init__()
        self.attack = -1
        self.health = 20
        self.defense = 2

class GreatAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.attack = 5
        self.health = -15
        self.defense = -2
        self.vampirism = 10
        
class Katana(Weapon):
    def __init__(self):
        super().__init__()
        self.attack = 6
        self.health = -20
        self.defense = -5
        self.vampirism = 50

class MagicWand(Weapon):
    def __init__(self):
        super().__init__()
        self.attack = 3
        self.health = 30
        self.heal_power = 3
        
class Warrior:
    def __init__(self):
        self.health = 50
        self.m_health = 50
        self.attack = 5
        self.defense = 0
        self.vampirism = 0
        self.second_attack = 0
        self.heal_power = 0

    @property
    def is_alive(self):
        return self.health > 0
    
    def hit(self,enemy):
        damage = max (0, self.attack-enemy.defense)
        enemy.health-= damage
        self.health = min(self.m_health, self.health + math.floor(damage*self.vampirism/100))
        
    def equip_weapon(self, weapon_name):
        self.health += weapon_name.health
        self.m_health+= weapon_name.health
        if self.attack>0:
            self.attack = max(0, self.attack+weapon_name.attack)
        if self.defense>0:
            self.defense = max(0, self.defense+weapon_name.defense)
        if self.vampirism>0:
            self.vampirism = max(0,self.vampirism+weapon_name.vampirism)
        if self.heal_power>0:
            self.heal_power = max(0,self.heal_power + weapon_name.heal_power)
        
class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 4
        self.health = 40
        self.m_health = 40
        self.vampirism = 50

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 3
        self.health = 60
        self.m_health = 60
        self.defense = 2

class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6
        self.second_attack = 0.5
        
class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 0
        self.health = 60
        self.m_health = 60
        self.heal_power = 2
    def heal(self,healed):
        healed.health = min (healed.m_health, healed.health+self.heal_power)
        
        
class Battle():
    def fight(self,a1, a2):
        while len(a1.units)>0 and len(a2.units)>0:
            fightArmy(a1,a2)
            a1.update()
            a2.update()
        return (len(a1.units)>0)
        
    def straight_fight(self,a1,a2):
        while len(a1.units)>0 and len(a2.units)>0:
            length = min(len(a1.units),len(a2.units))
            for i in range(length):
                fight(a1.units[i], a2.units[i])
            a1.update()
            a2.update()
        return (len(a1.units)>0)
                
def fightArmy(a1,a2):
    while a1.units[0].is_alive:
        a1.hit(a2)
        if a2.units[0].is_alive:
            a2.hit(a1)
        else: return True
    return False
            
        
def fight(unit_1, unit_2):
    while unit_1.is_alive:
        unit_1.hit(unit_2)
        if unit_2.health>0:
            unit_2.hit(unit_1)
        else: return True
    return False