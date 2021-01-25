from Champion import champion


class Potion(champion):
    def __init__(self, power = 10):
        self.power = power
    
    def heals(self):
        self.health += self.power
        if self.is_alive():
            self.health < 0
        print("%s does %d healing to %s" % (self.name, self.power, self.name))

        if self.is_alive():
            print("tis only a flesh wound")