from Inanimates import *
from Places import *
from Animates import Player, Enemy

class HardCodedStuff:
    def __init__ (self, _player):
        self.player = _player
        ##REMEMBER: MAX ARMOUR VAL MUST BE 200 OR YOU NEED TO CHANGE EARLIER##
        self.armour = [Armour(1, "Helmet of Beginner's Luck"), Armour(2, "Billy's Helm")]
        self.weapons = [Weapon("Billy's Knife", 10)]
        self.enemies = [Enemy("Billy", 2, self.weapons[0], [self.armour[1]], 10, self.player)]
        self.rooms = [[0,0,0,0],[0, 2, 7, 0], [0, 3, 8, 1], [0, 4, 9, 2], [0, 5, 10, 3],[0, 6, 11, 4], [0, 0, 12, 5], [1, 8, 13, 0], [2, 9, 14, 7],[3, 10, 15, 8], [4, 11, 16, 9], [5, 12, 17, 10], [6, 0, 18, 11],[7, 14, 19, 0], [8, 15, 20, 13], [9, 16, 21, 14], [10, 17, 22, 15], [11, 18, 23, 16], [12, 0, 24, 17], [13, 20, 25, 0], [14, 21, 26, 19], [15, 22, 27, 20], [16, 23, 28, 21], [17, 24, 29, 2], [18, 0, 30, 23], [19, 26, 31, 0], [20, 27, 32, 25], [21, 28, 33, 26], [22, 29, 34, 27], [23, 30, 35, 28], [24, 0, 36, 29], [25, 32, 0, 0], [26, 33, 0, 31], [27, 34, 0, 32], [28, 35, 0, 33], [29, 36, 0, 34], [30, 0, 0, 35]]
        self.descriptions = [Room("You cannot go in that direction... Please try again.", "You cannot go in that direction... Please try again.", []), Room("This is where you were created... The Mii Creation Screen where you, the saviour of your kind, were born", "Story", [MiiRecoverii("1R")]), Room("This is where you were created... The Mii Creation Screen where you, the saviour of your kind, were born2", "Story2", [MiiRecoverii("2R")]), Room("This is where you were created... The Mii Creation Screen where you, the saviour of your kind, were born3", "Story3", [MiiRecoverii("3R")])]
        self.populateCommandsDict()

    def populateCommandsDict(self):
        self.commands = {
            "help": self.player.helpMe,
            "attack": self.player.attack,
            "defend": self.player.defend,
            "explore": self.player.explore,
            "status": self.player.getStatus,
            "run": self.player.run,
            "quit": self.player.quitIt,
            "go": self.player.go,
            "target": self.player.setTarget,
      } 

    def findNewRoom(self, index1, index2, s):
        if index2 == 4:
            return "That was not a valid direction"
        room = self.rooms[index1][index2]
        if s == "str":
            if self.descriptions[room].isVisited():
                return self.descriptions[room].getShortDesc()
            self.descriptions[room].setVisited(True)
            return self.descriptions[room].getLongDesc()
        return room

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

    def getContentsOfRoom(self, room, returnType):
        returns = []
        for place in self.descriptions[room].getContents():
            if returnType == "str":
                returns.append(place.getName())
            else: returns.append(place)
        if returnType == "str":
            return str(returns)[1:-1]
        return returns
    


class Room:

    def __init__(self, shortDesc, longDesc, contents):
        self.shortDesc = shortDesc
        self.longDesc = longDesc
        self.contents = contents
        self.visited = False

    def isVisited(self):
        return self.visited

    def setVisited(self, boolean):
        self.visited = boolean

    def getShortDesc(self):
        return self.shortDesc

    def getLongDesc(self):
        return self.longDesc

    def getContents(self):
        return self.contents