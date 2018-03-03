class Armour:
    
    def __init__ (self, val, name):
        self.val = val
        self.name = name
    
    def getVal(self):
        return self.val
    
    def getName(self):
        return self.name
    
    def toStats(self):
        return self.name + ": Armour Points: " + str(self.val)


class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def getDamage(self):
        return self.damage

    def toStats(self):
        return self.name +": Damage Given: " + str(self.damage)
