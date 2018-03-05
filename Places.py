import time
from Animates import Player

class Place:
    
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class MiiRecoverii(Place):

    def __init__(self, name):
        super().__init__(name)

    def onVisit(self, player):
        #Loop so we can deal with bad typers
        while True:
            heal = input("Welcome to MiiRecoverii! Would you like to be healed? (Y/N)").upper()
            if heal == "Y":
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1...Aaaaand voila! You have been healed")
                player.hitPoints = player.getFullHitPoints()
                print("Your health is now " + str(player.getFullHitPoints()))
                break
            elif heal == "N":
                print("See you soon then!")
                break
            else:
                print("I'm sorry... I don't understand you...")

class MiiBuyy(Place):

    def __init__(self, name, items, weapons, armour):
        super().__init__(name)
        self.items = items
        self.weapons = weapons
        self.armour = armour

    def onVisit(self, player):
        #Loop for bad typers
        choosing = True
        while choosing:
            choice = input("Are you shopping for items, weapons or armour?").lower()
            if choice == "items" or choice == "weapons" or choice == "armour":
                choosing = False
        if choice == "items":
            if self.items != []:
                #Print indexed list
                print("Choose an item to buy!")
                i = 1
                for item in self.items:
                    print(str(i) + "). " + item.getName() + ", Price: " + str(item.getPrice()))
                    i += 1
                target = "not an int"
                while not type(target) is int:
                    try:
                        target = int(input("Which would you like to buy? (Type 0 for none)"))
                    except ValueError as e:
                        print("This input needs to be a number")
                player.buy(self.items[target-1])
            else:  print("This shop stocks no items")
            
        if choice == "weapons":
            if self.weapons != []:
                #Print indexed list
                print("Choose an item to buy!")
                i = 1
                for weapon in self.weapons:
                    print(str(i) + "). " + weapon.getName() + ", Price: " + str(weapon.getPrice()))
                    i += 1
                target = "not an int"
                while not type(target) is int:
                    try:
                        target = int(input("Which would you like to buy? (Type 0 for none)"))
                    except ValueError as e:
                        print("This input needs to be a number")
                player.buy(self.weapons[target-1])
            else: print("This shop stocks no weapons")

        if choice == "armour":
            if self.armour != []:
                print("Choose an item to buy!")
                #Print indexed list
                i = 1
                for piece in self.armour:
                    print(str(i) + "). " + piece.getName() + ", Price: " + str(piece.getPrice()))
                    i += 1
                target = "not an int"
                while not type(target) is int:
                    try:
                        target = int(input("Which would you like to buy? (Type 0 for none)"))
                    except ValueError as e:
                        print("This input needs to be a number")
                player.buy(self.armour[target-1])
            else: print("This shop stocks no armour")

class MiiDestroyy(Place):

    def __init__(self, name, enemies, money):
        super().__init__(name)
        self.enemies = enemies
        self.money = money

    def onVisit(self, player, hcs):
        total = 0
        for enemy in self.enemies:
            print("Your target is now: " + enemy.getName())
            player.makeTarget(enemy)
            while True:
                s = input(">>>").lower()
                player.doCommand(s, hcs)
                if player.isAttacking() == False:
                    total += 1
                    break
            print("Well done! You've beaten " + str(total) + " enemies so far")
            if total == len(self.enemies):
                break
            st = input("Would you like to continue battling?(Y/N)")
            if st == "N":
                break
        if total == len(self.enemies):
            print("You beat all the enemies")
            print("Here, have this reward of $" + str(self.money))
            player.addToMoney(self.money)
        else:
            print("Good effort... Goodbye for now!")
