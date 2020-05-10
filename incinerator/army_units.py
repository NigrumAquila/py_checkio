from dataclasses import dataclass

@dataclass
class Soldier:
    soldier_type: str
    name: str
    army_type: str
    specialization: str

    def introduce(self):
        return f"{self.soldier_type} {self.name}, {self.army_type} {self.specialization}"

Swordsman = Lancer = Archer = None

class Army:
    def __getattr__(self, method_name):
        train, unit_type = method_name.split("_")
        return lambda name: Soldier(type(self).soldier_type[unit_type], name, type(self).army_type, unit_type)


class AsianArmy(Army):
    army_type = "Asian"
    soldier_type = {"swordsman": "Samurai", "lancer": "Ronin", "archer": "Shinobi"}


class EuropeanArmy(Army):
    army_type = "European"
    soldier_type = {"swordsman": "Knight", "lancer": "Raubritter", "archer": "Ranger"}