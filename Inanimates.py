class Inanimate:

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

class Armour(Inanimate):
    
    def __init__ (self, val, name, location, place):
        super().__init__(name, location)
        self.val = val
    
    def getVal(self):
        return self.val

    def getPlace(self):
        return self.place
    
    def toStats(self):
        return self.name + ": Armour Points: " + str(self.val)


class Weapon(Inanimate):

    def __init__(self, name, damage, location):
        super().__init__(name, location)
        self.damage = damage

    def getDamage(self):
        return self.damage

    def toStats(self):
        return self.name +": Damage Given: " + str(self.damage)

class Item(Inanimate):

    def __init__(self, name, ability, location):
        super().__init__(name, location)
        self.ability = ability

    def getAbility(self):
        return self.ability

class Shop:

    def __init__(self, price):
        self.price = price

    def getPrice(self):
        return self.price

class ShopItem(Item, Shop):

    def __init__(self, name, ability, location, price):
        Item.__init__(self, name, ability, location)
        Shop.__init__(self, price)

class Ability:

    def __init__(self, typeOf, val):
        self.typeOf = typeOf
        self.val = val

    def getTypeOf(self):
        return self.typeOf

    def getVal(self):
        return val

