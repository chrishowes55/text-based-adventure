from Inanimates import Weapon, Armour
import random

##Super-class for all animate objects
class Animate:

    ##Constructor for Animate, sets inherited properties of the method
    def __init__(self, name, currentRoom, hitPoints, weapon, armour):
        self.name = name
        self.currentRoom = currentRoom
        self.hitPoints = hitPoints
        self.weapon = weapon
        self.armour = armour
        self.armourProtection = self.getArmourProtection(armour)
        self.dead = False
        self.attacking = False
        self.defending = False

    ##All Animate objects have a way of attacking
    def attack(self):
        print(self.name + " attacks " + self.target.getName())
        self.attacking = True
        self.defending = False
        self.target.takeDamage(random.randint(self.weapon.getDamage()-2, self.weapon.getDamage()+2))

    ##All Animate objects have a way of defending
    def defend(self):
        if self.defending:
            print(self.name + " continues to defend")
        else: print(self.name + " is now defending")
        self.defending = True
        self.attacking = True

    ##All Animate objects have a way of running
    def run(self):
        print(self.name + " attempts to run from " + self.target.getName())
        luck = random.randint(1, 100)
        if luck % 2 == 0:
            print(self.name + " has escaped successfully!")
            self.defending = False
            self.attacking = False
        else: print(self.name + "'s escape attempt failed")

    def takeDamage(self, damagePoints):
        ##damage taken is equal to damage given multiplied by (1 - your armour as a percentage of the maximum armour value (200)) and if defending that damage is divided by 2, 3 or 4
        if self.isDefending():
            myDamage = int((damagePoints * (1 - (self.armourProtection / 200))) / random.randint(2, 4))
            self.hitPoints -= myDamage
        else:
            myDamage = int(damagePoints * (1 - (self.armourProtection / 200)))
            self.hitPoints -= myDamage
        print(self.name + " took " + str(myDamage) + " damage")
        if self.hitPoints <= 0:
            self.die()
            self.target.setAttacking(False)
            print(self.name + " died")
        else:
            if self.hitPoints > 1: print(self.name + " has " + str(self.hitPoints) + " hit points remaining")
            else: print(self.name + " has " + str(self.hitPoints) + " hit point remaining")

    def isDead(self):
        return self.dead

    def getArmourProtection(self, armour):
        total = 0
        for piece in armour:
            total += piece.getVal()
        return total

    def decideNextMove(self):
        print("Cannae decide I'm unimplemented")

    def isDefending(self):
        return self.defending

    def isAttacking(self):
        return self.attacking

    def setAttacking(self, boolean):
        self.attacking = boolean

class Player(Animate):
    
    def __init__(self, name):
        super().__init__(name, 1, 15, Weapon("Hands",  5, 0,), [Armour(1, "Helmet of Beginner's Luck", 0)])
        self.level = 1
        self.fullHitPoints = 15
        self.initialHitPoints = 15
        self.levelXPs = [0, 10, 25, 45, 70, 100, 135, 180, 230, 285, 345, 1000000000]
        self.hits = 0
        self.xp = 0

    def incrementXP(self):
        self.xp += self.hits**2
        if self.xp >= self.levelXPs[self.level]:
            diff = self.xp - self.levelXPs[self.level]
            self.incrementLevel()
            self.xp = 0 + diff
        print("You need another " + str(self.levelXPs[self.level] - self.xp) + " XP to level up")
        
    def attack(self):
        print(self.name + " attacks " + self.target.getName())
        self.hits += 1
        self.attacking = True
        self.defending = False
        self.target.takeDamage(random.randint(self.weapon.getDamage()-2, self.weapon.getDamage()+2))
    
    def getName(self):
        return self.name
    
    def defend(self):
        if self.defending:
            print(self.name + " continues to defend")
        else: print(self.name + " is now defending")
        self.defending = True
        self.attacking = True
        self.target.decideNextMove()
            
    def die(self):
        print("You died... please restart")
        self.quitIt()

    def run(self):
        print(self.name + " attempts to run from " + self.target.getName())
        luck = random.randint(1, 100)
        if luck % 2 == 0:
            print(self.name + " has escaped successfully!")
            self.defending = False
            self.attacking = False
        else:
            print(self.name + "'s escape attempt failed")
            self.target.decideMextMove()

    def go(self, hcs):
        if not self.attacking:
            if hcs.getContentsOfRoom(self.currentRoom, "str") != "":
                print("You may choose somewhere to visit")
                i = 1
                for place in hcs.getContentsOfRoom(self.currentRoom, "list"):
                    print(str(i) + "). " + place.getName())
                    i += 1
                target = "not an int"
                while not type(target) is int:
                    try:
                        target = int(input("Where would you like to go? (Type 0 for none of these)"))
                    except ValueError as e:
                        print("This input must be a number")
                hcs.getContentsOfRoom(self.currentRoom, "list")[target-1].onVisit(self)
        else: print("You cannot go anywhere whilst attacking")

    def search(self, hcs):
        if not self.attacking:
            if hcs.getItemsInRoom(self.currentRoom, "list") != [[], [], []]:
                print("Items in this room: " + hcs.getItemsInRoom(self.currentRoom, "str"))
                for array in hcs.getItemsInRoom(self.currentRoom, "list"):
                    for thing in array:
                        print(self.name + " found " + thing.getName())
            else: print("There was nothing in this room")

    def setTarget(self, hcs):
        if hcs.getEnemiesInRoom(self.currentRoom, "str") != "":
            print("You must choose an enemy to target")
            i = 1
            for enemy in hcs.getEnemiesInRoom(self.currentRoom, "list"):
                print(str(i) + "). " + enemy.getName())
                i += 1
            target = "not an int"
            while not type(target) is int:
                try:
                    target = int(input("Who would you like to target?"))
                except ValueError as e:
                    print("This input must be a number")
            self.makeTarget(hcs.getEnemiesInRoom(self.currentRoom, "list")[target-1])
            self.attacking = True

    def explore(self, hcs):
        if not self.attacking:
            choosing = True
            while choosing:
                direction = input("Which way do you want to go? (N/E/S/W)")
                if direction == "N":
                    directionInt = 0
                elif direction == "E":
                    directionInt = 1
                elif direction == "S":
                    directionInt = 2
                elif direction == "W":
                    directionInt = 3
                else:
                    directionInt = 4

                if hcs.findNewRoom(self.currentRoom, directionInt, "str") != "That was not a valid direction" and hcs.findNewRoom(self.currentRoom, directionInt, "str") != "You cannot go in that direction... Please try again.":
                    choosing = False
                    print(hcs.findNewRoom(self.currentRoom, directionInt, "str"))
                if hcs.findNewRoom(self.currentRoom, directionInt, "num") != 0:
                    self.currentRoom = int(hcs.findNewRoom(self.currentRoom, directionInt, "num"))
                print("Enemies in this room: \n" + hcs.getEnemiesInRoom(self.currentRoom, "str"))
                self.setTarget(hcs)
                print("Contents of this room: \n" + hcs.getContentsOfRoom(self.currentRoom, "str"))
        else: print("You cannot explore while attacking... Please run away first")
                    
    def getLevel(self):
        return self.level

    def incrementLevel(self):
        self.level += 1
        print("You have levelled up! Your new full health is " + str(getFullHitPoints()) + ", so go to a MiiRecoverii to upgrade your health")

    def getFullHitPoints(self):
        self.setFullHitPoints()
        return self.fullHitPoints

    def setFullHitPoints(self):
        change = 10
        changeIncrement = 5
        total = self.initialHitPoints
        for i in range(1, self.level):
            total += change
            change += changeIncrement
        self.fullHitPoints = total

    def helpMe(self):
        print("Commands to choose from are: explore, go, help, status, attack, run, defend, target, quit")

    def getStatus(self):
        print("Your status:")
        print("\nYour armour stats: ")
        for piece in self.armour:
            print(piece.toStats() + "\n")
        print("Your weapon stats: " + self.weapon.toStats())
        print("\nYour remaining HP: " + str(self.hitPoints))
        print("\nYour level: "+ str(self.level))
        print("\nYour XP: " + str(self.xp))

    def quitIt(self):
        print("Quitting")
        quit()

    def doCommand(self, s, hcs):
        if s in hcs.getCommands() and s != "explore" and s != "target" and s != "go" and s != "search":
            hcs.getCommands()[s]()
        elif s in hcs.getCommands():
            hcs.getCommands()[s](hcs)
        else:
            print("Invalid input... Please try again")

    def makeTarget(self, target):
        self.target = target


class Enemy(Animate):
    
    def __init__ (self, name, room, weapon, armour, hitPoints, player):
        super().__init__(name, room, hitPoints, weapon, armour)
        self.target = player

    def getStats(self):
        return self.name + ": Health: " + str(self.hitPoints)

    def getRoom(self):
        return self.currentRoom
            
    def die(self):
        print(self.name + " is dead... Well done!")
        self.target.incrementXP()
        self.target.hits = 0
        self.dead = True

    def getName(self):
        return self.name

    def getHealth(self):
        return self.hitPoints

    def decideNextMove(self):
        luck = random.randint(1, 100)
        if luck % 88 == 0:
            self.run()
        else:
            if luck > 70:
                self.defend()
            else:
                self.attack()

    def takeDamage(self, damagePoints):
        ##damage taken is equal to damage given multiplied by (1 - your armour as a percentage of the maximum armour value (200)) and if defending that damage is divided by 2, 3 or 4
        if self.isDefending():
            myDamage = int((damagePoints * (1 - (self.armourProtection / 200))) / random.randint(2, 4))
            self.hitPoints -= myDamage
        else:
            myDamage = int(damagePoints * (1 - (self.armourProtection / 200)))
            self.hitPoints -= myDamage
        print(self.name + " took " + str(myDamage) + " damage")
        if self.hitPoints <= 0:
            self.die()
            self.target.setAttacking(False)
            print(self.name + " died")
        else:
            self.decideNextMove()
            if self.hitPoints > 1: print(self.name + " has " + str(self.hitPoints) + " hit points remaining")
            else: print(self.name + " has " + str(self.hitPoints) + " hit point remaining")
