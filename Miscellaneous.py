"""A file containing lots of bits and bobs."""
from Inanimates import Armour, Weapon, Item, Ability, ShopItem
from Places import MiiRecoverii, MiiBuyy, MiiDestroyy
from Animates import Enemy, NPC


class HardCodedStuff:
    """
    A class containing many of the hard-coded things in the game.

    Attributes
    ----------
    player: Player
        The player (if required)
    items: list
        A list of all the different items in the game
    armour: list
        A list of all the different armour in the game
    weapons: list
        A list of all the different weapons in the game
    enemies: list
        A list of all the different enemies in the game
    people: list
        A list of all the different NPCs in the game
    rooms: 2D list
        A list of all the different rooms in the game (forgot how it works)
    descriptions: list
        A list of all the different rooms with descriptions

    Methods
    -------
    populate_commands()
        Map commands to actions
    find_new_room(index1: int, index2: int, s: str, p: str)
        Put the player in new room
    get_stats_armour(index: int)
        Return the stats of the armour at index
    get_stats_enemy(index: int)
        Return the stats of the enemy at index
    get_enemies_in_room(room: int, return_type: str)
        Return all of the enemies in the room in a list or str
    get_people_in_room(room: int, return_type: str)
        Return all of the NPCs in the room in a list or str
    get_contents_of_room(room: int, return_type: str)
        Return the contents of the room
    get_items_in_room(room: int, return_type: str)
        Return all of the items in the room
    """

    def __init__(self, _player):
        """Initialize HardCodedStuff."""
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
                "This is where you were created... The Mii Creation Screen "
                + "where you, the saviour of your kind, were born",
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
                "You see a small, grey room in front of you. In the middle of "
                + "the room stands Master Ozana, but he tells you you must "
                + "defeat the enemy in front of him to be worthy of his "
                + "time",
                [MiiRecoverii("2R")],
            ),
            Room(
                "This is where you were created... The Mii Creation Screen "
                + "where you, the saviour of your kind, were born3",
                "Story3",
                [MiiRecoverii("3R")],
            ),
        ]
        self.populate_commands()

    def populate_commands(self):
        """Facilitate player input by mapping commands to actions."""
        self.commands = {
            "help": self.player.help_me,
            "attack": self.player.attack,
            "defend": self.player.defend,
            "explore": self.player.explore,
            "stats": self.player.get_status,
            "run": self.player.run,
            "quit": self.player.quit_it,
            "go": self.player.go,
            "target": self.player.set_target,
            "search": self.player.search,
            "backpack": self.player.get_backpack,
            "talk": self.player.talk,
        }

    def find_new_room(self, index1, index2, s, p):
        """Put the player in the new room."""
        # N=0, E=1, S=2, W=3
        if index2 == 4:
            return "That was not a valid direction"
        room = self.rooms[index1][index2]
        if s == "str":
            # First time visiting show story instead of description
            if self.descriptions[room].visited:
                return self.descriptions[room].short_desc
            else:
                if p != "test":
                    self.descriptions[room].visited = True
                return self.descriptions[room].long_desc
        return room

    def get_stats_armour(self, index):
        """Return the stats of the armour at index."""
        return self.armour[index].to_stats()

    def get_stats_enemy(self, index):
        """Return the stats of the enemy at index."""
        return self.enemies[index].get_stats()

    def get_enemies_in_room(self, room, return_type):
        """Return all of the enemies in the room in a list or str."""
        returns = []
        for enemy in self.enemies:
            if not enemy.dead:
                if enemy.current_room == room:
                    if return_type == "str":
                        returns.append(enemy.get_stats())
                    else:
                        returns.append(enemy)
        if return_type == "str":
            return str(returns)[1:-1]
        return returns

    def get_people_in_room(self, room, return_type):
        """Return all of the NPCs in the room in a list or str."""
        returns = []
        for person in self.people:
            if person.room == room:
                if return_type == "str":
                    returns.append(person.name)
                else:
                    returns.append(person)
        if return_type == "str":
            return str(returns)[1:-1]
        return returns

    def get_contents_of_room(self, room, return_type):
        """Return the contents of the room, ie MiiRecoverii..."""
        returns = []
        for place in self.descriptions[room].contents:
            if return_type == "str":
                returns.append(place.name)
            else:
                returns.append(place)
        if return_type == "str":
            return str(returns)[1:-1]
        return returns

    def get_items_in_room(self, room, return_type):
        """
        Return all of the items in the room in a 2D array or str.

        Array in form [items, weapons, armour]
        """
        # Return in one 2d array for ease
        pieces = []
        stabs = []
        stuffs = []
        returns = []
        for piece in self.armour:
            if piece.location == room:
                if return_type == "str":
                    returns.append(piece.name)
                else:
                    returns.append(piece)
        for weapon in self.weapons:
            if weapon.location == room:
                if return_type == "str":
                    stabs.append(weapon.name)
                else:
                    stabs.append(weapon)
        for item in self.items:
            if item.location == room:
                if return_type == "str":
                    stuffs.append(item.name)
                else:
                    stuffs.append(item)
        if return_type == "str":
            return (
                "Armour: "
                + str(pieces)[1:-1]
                + "\nWeapons: "
                + str(stabs)[1:-1]
                + "\nItems: "
                + str(stuffs)[1:-1]
            )
        return [pieces, stabs, stuffs]

    def decide_pass(self, player, target):
        """Annoying method."""
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


class Room:
    """
    A class to represent a room.

    Attributes
    ----------
    short_desc: str
        A short description of the room
    long_desc: str
        A long description of the room
    contents: list
        A list of the contents of the room (ie MiiRecoverii...)
    visited: bool
        A boolean to show if the room has been visited before
    """

    def __init__(self, short_desc, long_desc, contents):
        """Initialize the room."""
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.contents = contents
        self.visited = False
