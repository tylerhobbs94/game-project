class champion:
    name = "champion"
    #! is_alive function for everyone with the command is_alive and can return their health status with "while %s is_alive() and/ or %s is alive"
    def is_alive(self):
        """
        #see's if hero is alive
        """
        if self.health > 0:
            return True
        else:
            return False
    #! Function for attack that everyone uses since we imported champion into each class.
    def attack(self, enemy):

        enemy.health -= self.power
        if not enemy.is_alive():
            enemy.health = 0
        print("%s does %d damage to %s." % (self.name,self.power,enemy.name))
        
        if not enemy.is_alive():
            print(self.winphrase)
    #! prints status of object, used in game as a way to find hero and enemies help.
    def print_status(self):
        print("%s has %d health and %d power."% (self.name, self.health, self.power))
    #! Function for our level up system, just a simple multiply into self.health and power and use the function later on.
    def level_up(self):
        self.health = self.health * 3
        self.power = self.power * 3