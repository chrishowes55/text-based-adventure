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

    ##All Animate objects have a way of attacking
    def attack(self):
        self.defending = True
        self.target.takeDamage(self.weapon.getDamage())

    ##All Animate objects have a way of defending
    def defend(self):
        self.defending = True

    ##All Animate objects have a way of running
    def run(self):
        print("run")
        self.defending = False

    def die(self):
        print(self.name + " is dead... Well done!")
        self.dead = True

    def isDead(self):
        return self.dead

    #All Animate objects must be able to take damage
    def takeDamage(self, damagePoints):
        ##damage taken is equal to damage given multiplied by (1 - your armour as a percentage of the maximum armour value (200)) and if defending that damage is halved
        if self.target.isDefending():
            self.hitPoints -= int((damagePoints * (1 - (self.armourProtection / 200))) / 2)
        else: self.hitPoints -= int(damagePoints * (1 - (self.armourProtection / 200)))
        if self.hitPoints <= 0:
            self.die()
        print(self.hitPoints)

    def getArmourProtection(self, armour):
        total = 0
        for piece in armour:
            total += piece.getVal()
        return total

    def isDefending(self):
        return self.defending

class Player(Animate):
    
    def __init__(self, name):
        super().__init__(name, 1, 10, Weapon("Hands",  5), [Armour(1, "Helmet of Beginner's Luck")])
    
    def getName(self):
        return self.name

    def explore(self, hcs):
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
            if hcs.getEnemiesInRoom(self.currentRoom, "str"):
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
                self.setTarget(hcs.getEnemiesInRoom(self.currentRoom, "list")[target-1])
                    
      

    def helpMe(self):
        print("Commands to choose from are: explore, help, status, attack, run, defend, quit")

    def getStatus(self):
        print("My status")

    def quitIt(self):
        print("Quitting")
        quit()

    def doCommand(self, s, hcs):
        if s in hcs.getCommands() and s != "explore":
            hcs.getCommands()[s]()
        elif s in hcs.getCommands():
            hcs.getCommands()[s](hcs)
        else:
            print("Invalid input... Please try again")

    def setTarget(self, target):
        self.target = target
        print(self.target)

class Enemy(Animate):
    
    def __init__(self, name, currentRoom, hitPoints):
        super().__init__(name, currentRoom, hitPoints)
    
class HardCodedStuff:
    def __init__ (self, _player):
        self.player = _player
        ##REMEMBER: MAX ARMOUR VAL MUST BE 200 OR YOU NEED TO CHANGE EARLIER##
        self.armour = [Armour(1, "Helmet of Beginner's Luck"), Armour(2, "Billy's Helm")]
        self.enemies = [Enemy("Billy", 2, Weapon("Billy's Knife", 10), [self.armour[1]], 10, self.player)]
        self.rooms = [[0,0,0,0],[0, 2, 7, 0], [0, 3, 8, 1], [0, 4, 9, 2], [0, 5, 10, 3],[0, 6, 11, 4], [0, 0, 12, 5], [1, 8, 13, 0], [2, 9, 14, 7],[3, 10, 15, 8], [4, 11, 16, 9], [5, 12, 17, 10], [6, 0, 18, 11],[7, 14, 19, 0], [8, 15, 20, 13], [9, 16, 21, 14], [10, 17, 22, 15], [11, 18, 23, 16], [12, 0, 24, 17], [13, 20, 25, 0], [14, 21, 26, 19], [15, 22, 27, 20], [16, 23, 28, 21], [17, 24, 29, 2], [18, 0, 30, 23], [19, 26, 31, 0], [20, 27, 32, 25], [21, 28, 33, 26], [22, 29, 34, 27], [23, 30, 35, 28], [24, 0, 36, 29], [25, 32, 0, 0], [26, 33, 0, 31], [27, 34, 0, 32], [28, 35, 0, 33], [29, 36, 0, 34], [30, 0, 0, 35]]
        self.descriptions = ["You cannot go in that direction... Please try again.", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
        self.populateCommandsDict()

    def populateCommandsDict(self):
        self.commands = {
            "help": player.helpMe,
            "attack": player.attack,
            "defend": player.defend,
            "explore": player.explore,
            "status": player.getStatus,
            "run": player.run,
            "quit": player.quitIt,
      } 

    def findNewRoom(self, index1, index2, s):
        if index2 == 4:
            return "That was not a valid direction"
        room = self.rooms[index1][index2]
        if s == "str":
            return self.descriptions[room]
        else: return room

    def getCommands(self):
        return self.commands

    def getStatsAtIndexInArmourArray(self, index):
        return self.armour[index].toStats()

    def getStatsAtIndexInEnemyArray(self, index):
        return self.enemies[index].getStats()

    def getEnemiesInRoom(self, room, returnType):
        returns = []
        for enemy in self.enemies:
            if not enemy.isDead():
                if enemy.getRoom() == room:
                    if returnType == "str":
                          returns.append(enemy.getStats())
                    else:
                          returns.append(enemy)
        if returnType == "str":
            return str(returns)[1:-1]
        return returns
    
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
    
class Enemy(Animate):
    
    def __init__ (self, name, room, weapon, armour, hitPoints, player):
        super().__init__(name, room, hitPoints, weapon, armour)
        self.target = player

    def getStats(self):
        return self.getName() + ": Health: " + str(self.getHealth())

    def getRoom(self):
        return self.currentRoom

    def getName(self):
        return self.name

    def getHealth(self):
        return self.hitPoints


class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def getDamage(self):
        return self.damage

        
    
player = Player(input("Hello Player! What's your name?\n>>>"))
print("Hello there " + player.getName())
hcs = HardCodedStuff(player)
print("Your armour stats: " + hcs.getStatsAtIndexInArmourArray(0))
playing = True
while playing:
    s = input(">>>").lower()
    player.doCommand(s, hcs)
