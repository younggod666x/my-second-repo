import random


class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power * random.randint(30, 90) / 100
        other.hp = round(other.hp - damage, 2)
        print(f"{self.name} attacks {other.name} for {damage:g} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp} HP"
