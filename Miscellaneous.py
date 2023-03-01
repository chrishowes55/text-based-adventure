from Inanimates import Armour, Weapon, Item, Ability, ShopItem
from Places import MiiRecoverii, MiiBuyy, MiiDestroyy
from Animates import Enemy, NPC


class HardCodedStuff:
    def __init__(self, _player):
        self.player = _player
        # REMEMBER: MAX ARMOUR VAL MUST BE 200 OR YOU NEED TO CHANGE EARLIER
        # TO MAKE A WEAPON UNDISCOVERABLE BY PLAYER, SET LOCATION TO ZERO
        self.items = [Item("Healing Potion", Ability("heal", 10), 2)]
        self.armour = [
            Armour(1, "Helmet of Beginner's Luck", 0, 0),
            Armour(2, "Billy's Helm", 2, 0),
        ]
        self.weapons = [Weapon("Billy's Knife", 4, 0)]
        self.enemies = [
            Enemy(
                "Billy",
                2,
                self.weapons[0],
                [self.armour[1]],
                10,
                self.player,
                10,
            )
        ]
        self.people = [NPC("Master Ozana", 2, ["Hey babe", "Yo bro"])]
        self.rooms = [
            [0, 0, 0, 0],
            [0, 2, 7, 0],
            [0, 3, 8, 1],
            [0, 4, 9, 2],
            [0, 5, 10, 3],
            [0, 6, 11, 4],
            [0, 0, 12, 5],
            [1, 8, 13, 0],
            [2, 9, 14, 7],
            [3, 10, 15, 8],
            [4, 11, 16, 9],
            [5, 12, 17, 10],
            [6, 0, 18, 11],
            [7, 14, 19, 0],
            [8, 15, 20, 13],
            [9, 16, 21, 14],
            [10, 17, 22, 15],
            [11, 18, 23, 16],
            [12, 0, 24, 17],
            [13, 20, 25, 0],
            [14, 21, 26, 19],
            [15, 22, 27, 20],
            [16, 23, 28, 21],
            [17, 24, 29, 2],
            [18, 0, 30, 23],
            [19, 26, 31, 0],
            [20, 27, 32, 25],
            [21, 28, 33, 26],
            [22, 29, 34, 27],
            [23, 30, 35, 28],
            [24, 0, 36, 29],
            [25, 32, 0, 0],
            [26, 33, 0, 31],
            [27, 34, 0, 32],
            [28, 35, 0, 33],
            [29, 36, 0, 34],
            [30, 0, 0, 35],
        ]
        self.descriptions = [
            Room(
                "You cannot go in that direction... Please try again.",
                "You cannot go in that direction... Please try again.",
                [],
            ),
            Room(
                "This is where you were created... The Mii Creation Screen\
                      where you, the saviour of your kind, were born",
                "NEVER APPEARS",
                [
                    MiiRecoverii("1R"),
                    MiiBuyy(
                        "1B",
                        [ShopItem("Bonjour", Ability("heal", 10), 0, 10)],
                        [self.weapons[0]],
                        [self.armour[0]],
                    ),
                    MiiDestroyy("1D", [self.enemies[0]], 1000),
                ],
            ),
            Room(
                "A little room that houses Master Ozana",
                "You see a small, grey room in front of you. In the middle of \
                    the room stands Master Ozana, but he tells you you must \
                        defeat the enemy in front of him to be worthy of his \
                            time",
                [MiiRecoverii("2R")],
            ),
            Room(
                "This is where you were created... The Mii Creation Screen \
                    where you, the saviour of your kind, were born3",
                "Story3",
                [MiiRecoverii("3R")],
            ),
        ]
        self.populateCommandsDict()

    def populateCommandsDict(self):
        self.commands = {
            "help": self.player.helpMe,
            "attack": self.player.attack,
            "defend": self.player.defend,
            "explore": self.player.explore,
            "stats": self.player.getStatus,
            "run": self.player.run,
            "quit": self.player.quitIt,
            "go": self.player.go,
            "target": self.player.setTarget,
            "search": self.player.search,
            "backpack": self.player.backpack,
            "talk": self.player.talk,
        }

    def decide_pass(self, player, target):
        if (
            type(
                self.get_contents_of_room(player.current_room, "list")[
                    target - 1
                ]
            )
            is MiiDestroyy
        ):
            self.get_contents_of_room(player.current_room, "list")[
                target - 1
            ].on_visit(player, self)
        else:
            self.get_contents_of_room(player.current_room, "list")[
                target - 1
            ].on_visit(player)

    def find_new_room(self, index1, index2, s, p):
        # N=0, E=1, S=2, W=3
        if index2 == 4:
            return "That was not a valid direction"
        room = self.rooms[index1][index2]
        if s == "str":
            # First time visiting show story instead of description
            if self.descriptions[room].isVisited():
                return self.descriptions[room].getShortDesc()
            else:
                if p != "test":
                    self.descriptions[room].setVisited(True)
                return self.descriptions[room].getLongDesc()
        return room

    def getStatsAtIndexInArmourArray(self, index):
        return self.armour[index].toStats()

    def getStatsAtIndexInEnemyArray(self, index):
        return self.enemies[index].get_stats()

    def get_enemies_in_room(self, room, returnType):
        returns = []
        for enemy in self.enemies:
            if not enemy.dead:
                if enemy.current_room == room:
                    if returnType == "str":
                        returns.append(enemy.get_stats())
                    else:
                        returns.append(enemy)
        if returnType == "str":
            return str(returns)[1:-1]
        return returns

    def get_people_in_room(self, room, returnType):
        returns = []
        for person in self.people:
            if person.current_room == room:
                if returnType == "str":
                    returns.append(person.name)
                else:
                    returns.append(person)
        if returnType == "str":
            return str(returns)[1:-1]
        return returns

    def get_contents_of_room(self, room, returnType):
        returns = []
        for place in self.descriptions[room].getContents():
            if returnType == "str":
                returns.append(place.name)
            else:
                returns.append(place)
        if returnType == "str":
            return str(returns)[1:-1]
        return returns

    def getItemsInRoom(self, room, returnType):
        # Return in one 2d array for ease
        pieces = []
        stabs = []
        stuffs = []
        returns = []
        for piece in self.armour:
            if piece.location == room:
                if returnType == "str":
                    returns.append(piece.name)
                else:
                    returns.append(piece)
        for weapon in self.weapons:
            if weapon.location == room:
                if returnType == "str":
                    stabs.append(weapon.name)
                else:
                    stabs.append(weapon)
        for item in self.items:
            if item.location == room:
                if returnType == "str":
                    stuffs.append(item.name)
                else:
                    stuffs.append(item)
        if returnType == "str":
            return (
                "Armour: "
                + str(pieces)[1:-1]
                + "\nWeapons: "
                + str(stabs)[1:-1]
                + "\nItems: "
                + str(stuffs)[1:-1]
            )
        return [pieces, stabs, stuffs]


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
