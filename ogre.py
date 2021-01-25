from Champion import champion
import random


class Ogre(champion):
    name = "Ogre"
    def __init__(self, health = 120, power = 15):
        self.health = health
        self.power = power
        self.winphrase = "The ogre hits you in the head with his club and your head explodes.... You die...Game Over."

    def attack(self, enemy):
        power = self.power
        double_damage = random.randint(1, 101)
        if double_damage > 90:
            self.power = self.power * 2
            print("Critical Hit!")
        super().attack(enemy)
        self.power = power