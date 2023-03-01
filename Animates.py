"""Contains all classes for animates."""
from Inanimates import Weapon, Armour
from Miscellaneous import HardCodedStuff
import random
import time


class Animate:
    """
    Overall class for Animte objects.

    Attributes
    ----------
    name: str
        Name of object
    current_room: int
        The current room of the object
    hit_points: int
        HP of object
    weapon: Weapon
        The weapon of the object
    armour: Armour
        The armour being worn by the object
    money: int
        How much money the object has
    armour_protection: int
        How much protecion the armour of the object adds
    dead: bool
        Is the object dead or alive
    attacking: bool
        Is the object in the attacking state
    defending: bool
        Is the object in the defending state
    target: Animate
        The target of the object (if in attacking mode)

    Methods
    -------
    attack()
        Attack another Animate.
    defend()
        Defend from another Animate.
    run()
        Run from another Animate.
    take_damage()
        Take damage.
    calculate_armour_protection()
        Calculate the current armour protection of Animate.
    decide_next_move()
        Animate decides next move.
    """

    def __init__(self, name, current_room, hit_points, weapon, armour, money):
        """Initialise Animate."""
        self.name = name
        self.current_room = current_room
        self.hit_points = hit_points
        self.weapon = weapon
        self.armour = armour
        self.armour_protection = self.calculate_armour_protection()
        self.dead = False
        self.attacking = False
        self.defending = False
        self.money = money

    def attack(self):
        """
        Attack another animate.

        Sets the attacking and defending states of self to True and False
        Then forces the target to take random damage in an interval
        """
        print(self.name + " attacks " + self.target.name)
        if self.hits:
            self.hits += 1
        self.attacking = True
        self.defending = False
        self.target.take_damage(
            random.randint(self.weapon.damage - 2, self.weapon.damage + 2)
        )

    def defend(self):
        """
        Defend from another animate.

        Sets the defending and attacking states of self to True and False
        """
        if self.defending:
            print(self.name + " continues to defend")
        else:
            print(self.name + " is now defending")
        self.defending = True
        self.attacking = True

    def run(self):
        """
        Run from another Animate.

        With probability 0.5:
            Animate escapes the battle:
            Sets defending and attacking to False
        """
        print(self.name + " attempts to run from " + self.target.name)
        luck = random.randint(1, 100)
        if luck % 2 == 0:
            print(self.name + " has escaped successfully!")
            self.defending = False
            self.attacking = False
            if type(self) == Player:
                self.target.ran_on()
        else:
            print(self.name + "'s escape attempt failed")
            if type(self) == Player:
                self.target.decide_next_move()

    def take_damage(self, damage_points):
        """
        Animate takes damage.

        Damage taken is equal to damage given multiplied by (1 - your armour
        as a percentage of the maximum armour value (200)) and if defending
        that damage is divided by 2, 3 or 4

        Parameters
        ----------
        damage_points: int
            The number of damage points taken by the Animate
        """
        if self.defending:
            my_damage = int(
                (damage_points * (1 - (self.armour_protection / 200)))
                / random.randint(2, 4)
            )
            self.hit_points -= my_damage
        else:
            my_damage = int(
                damage_points * (1 - (self.armour_protection / 200))
            )
            self.hit_points -= my_damage
        print(self.name + " took " + str(my_damage) + " damage")
        if self.hit_points <= 0:
            self.die()
            self.target.attacking = False
            print(self.name + " died")
        else:
            if type(self) is Enemy:
                self.decide_next_move()
            if self.hit_points > 1:
                print(
                    self.name
                    + " has "
                    + str(self.hit_points)
                    + " hit points remaining"
                )
            else:
                print(
                    self.name
                    + " has "
                    + str(self.hit_points)
                    + " hit point remaining"
                )

    def calculate_armour_protection(self):
        """Calculate the armout protection of self.armour."""
        total = 0
        for piece in self.armour:
            total += piece.val
        return total

    def decide_next_move(self):
        """Decide the next move of Animate."""
        print("Cannae decide I'm unimplemented")
        raise NotImplementedError


class Player(Animate):
    """
    Class to represent the Player - extends Animate.

    Attributes
    ----------
    name: str
        Name of the player
    current_room: int
        The current room of the player
    hit_points: int
        current HP of player
    full_hit_points: int
        full HP of player - used to calculate new HP
    initial_hit_points: int
        initial HP of player - used to calculate new HP
    weapon: Weapon
        The weapon of the player
    armour: Armour
        The armour being worn by the player
    money: int
        How much money the player has
    armour_protection: int
        How much protecion the armour of the player adds
    dead: bool
        Is the player dead or alive
    attacking: bool
        Is the player in the attacking state
    defending: bool
        Is the player in the defending state
    target: Animate
        The target of the player (if in attacking mode)
    level: int
        The level of the player
    level_xps: list
        The XP values required for each level up
    hits: int
        The number of hits given in a fight - used to calculate XP
    backpack: list
        List of the items the player has currently

    Methods
    -------
    buy(item: Inanimate)
        Buy an item.
    increment_xp()
        Gain XP on defeat of an enemy.
    attack()
        Attack an enemy.
    defend()
        Defend from another Animate.
    die()
        Die.
    go()
        Go somewhere in the room.
    search()
        Search the room.
    set_target()
        Set the target of the player.
    explore()
        Move to a new room.
    talk()
        Talk to any NPCs in the room.
    increment_level()
        Level up.
    get_full_hit_points()
        Calculate and return the full hit points of the player.
    set_full_hit_points()
        Calculate the full hit points of the player.
    backpack()
        Print out the contents of the backpack.
    equip(item: Inanimate)
        Equip an item.
    use(item: Inanimate)
        Use an item.
    help_me()
        Output help with available inputs.
    get_status()
        Output player's status
    do_command(s: str)
        Carry out the requested command
    """

    def __init__(self, name):
        """Initialise player."""
        super().__init__(
            name,
            1,
            15,
            Weapon("Hands", 5, 0),
            [Armour(1, "Helmet of Beginner's Luck", 0, 0)],
            0,
        )
        self.level = 1
        self.full_hit_points = 15
        self.initial_hit_points = 15
        self.level_xps = [
            0,
            10,
            25,
            45,
            70,
            100,
            135,
            180,
            230,
            285,
            345,
            1000000000,
        ]
        self.hits = 0
        self.xp = 0
        self.backpack = [
            Weapon("Hands", 5, 0),
            Armour(1, "Helmet of Beginner's Luck", 0, 0),
        ]

    def buy(self, item):
        """Buy an item."""
        if item.price - self.money > 0:
            print("You cannot buy this")
        else:
            print("Item bought!")
            self.money -= item.price
            self.backpack.append(item)

    def increment_xp(self):
        """
        Gain XP on defeat of enemy.

        XP given is equal to number of hits dealt squared (slightly flawed,
        maybe revisit)
        """
        self.xp += self.hits**2
        if self.xp >= self.level_xps[self.level]:
            diff = self.xp - self.level_xps[self.level]
            self.increment_level()
            self.xp = diff
        print(
            "You need another "
            + str(self.level_xps[self.level] - self.xp)
            + " XP to level up"
        )

    def attack(self):
        """Attack an enemy."""
        if not self.target.dead:
            super().attack()
        else:
            print("You cannot attack while target is dead")

    def defend(self):
        """Defend from another Animate."""
        super().defend()
        self.target.decide_next_move()

    def die(self):
        """Die."""
        print("You died... please restart")
        self.quit_it()

    def go(self):
        """
        Go somewhere in the room.

        Cannot go anywhere while attacking.
        """
        hcs = HardCodedStuff()
        if not self.attacking:
            if hcs.get_contents_of_room(self.current_room, "str") != "":
                # Fairly common construct in this code - prints an indexed
                # list to choose from
                print("You may choose somewhere to visit")
                i = 1
                for place in hcs.get_contents_of_room(
                    self.current_room, "list"
                ):
                    print(str(i) + "). " + place.name)
                    i += 1
                target = "not an int"
                while not type(target) is int:
                    try:
                        target = int(
                            input(
                                "Where would you like to go? (Type 0 for none \
                                    of these)"
                            )
                        )
                    except ValueError:
                        print("This input must be a number")
                hcs.decide_pass(self, target)
        else:
            print("You cannot go anywhere whilst attacking")

    def search(self, hcs):
        """Search the room and choose whether to collect items."""
        if not self.attacking:
            if hcs.getItemsInRoom(self.current_room, "list") != [[], [], []]:
                # Goes through room and finds everything in it
                print(
                    "Items in this room: "
                    + hcs.getItemsInRoom(self.current_room, "str")
                )
                for array in hcs.getItemsInRoom(self.current_room, "list"):
                    for thing in array:
                        print(self.name + " found " + thing.name)
                        add = input("Add to backpack? (Y/N)").upper()
                        if add == "Y":
                            self.backpack.append(thing)
                        time.sleep(1)
            else:
                print("There was nothing in this room")

    def set_target(self):
        """Set the target of the player."""
        hcs = HardCodedStuff()
        if hcs.get_enemies_in_room(self.current_room, "str") != "":
            # Prints indexed list
            print("You must choose an enemy to target")
            i = 1
            for enemy in hcs.get_enemies_in_room(self.current_room, "list"):
                print(str(i) + "). " + enemy.name)
                i += 1
            target = "not an int"
            while not type(target) is int:
                try:
                    target = int(input("Who would you like to target?"))
                except ValueError:
                    print("This input must be a number")
            self.target = hcs.get_enemies_in_room(self.current_room, "list")[
                target - 1
            ]
            self.attacking = True

    def explore(self):
        """Move to a new room."""
        hcs = HardCodedStuff()
        if not self.attacking:
            choosing = True
            while choosing:
                direction = input("Which way do you want to go? (N/E/S/W)")
                # Converts input to int
                if direction == "N":
                    direction_int = 0
                elif direction == "E":
                    direction_int = 1
                elif direction == "S":
                    direction_int = 2
                elif direction == "W":
                    direction_int = 3
                else:
                    direction_int = 4

                # We have gone valid way
                if (
                    hcs.find_new_room(
                        self.current_room, direction_int, "str", "test"
                    )
                    != "That was not a valid direction"
                    and hcs.find_new_room(
                        self.current_room, direction_int, "str", "test"
                    )
                    != "You cannot go in that direction... Please try again."
                ):
                    choosing = False
                    print(
                        hcs.find_new_room(
                            self.current_room, direction_int, "str", "non"
                        )
                    )
                else:
                    print(
                        hcs.find_new_room(
                            self.current_room, direction_int, "str", "non"
                        )
                    )
            if (
                hcs.find_new_room(
                    self.current_room, direction_int, "num", "test"
                )
                != 0
            ):
                self.current_room = int(
                    hcs.find_new_room(
                        self.current_room, direction_int, "num", "non"
                    )
                )
            # Does basic housekeeping for new room
            print(
                "Enemies in this room: \n"
                + hcs.get_enemies_in_room(self.current_room, "str")
            )
            self.set_target()
            print(
                "Contents of this room: \n"
                + hcs.get_contents_of_room(self.current_room, "str")
            )
            print(
                "People in this room: \n"
                + hcs.get_people_in_room(self.current_room, "str")
            )
        else:
            print(
                "You cannot explore while attacking... Please run away first"
            )

    def talk(self):
        """Talk to any NPCs in the room."""
        hcs = HardCodedStuff()
        if hcs.get_people_in_room(self.current_room, "str") != "":
            # Prints indexed list
            print("You must choose a person to talk to (0 for none)")
            i = 1
            for person in hcs.get_people_in_room(self.current_room, "list"):
                print(str(i) + "). " + person.name)
                i += 1
            target = "not an int"
            while not type(target) is int:
                try:
                    target = int(input("Who would you like to target?"))
                except ValueError:
                    print("This input must be a number")
            if target != 0:
                hcs.get_people_in_room(self.current_room, "list")[
                    target - 1
                ].do_dialogue()

    def increment_level(self):
        """Increment the player's level."""
        self.level += 1
        print(
            "You have levelled up! Your new full health is "
            + str(self.get_full_hit_points())
            + ", so go to a MiiRecoverii to upgrade your health"
        )

    def get_full_hit_points(self):
        """Calculate and then return the full hit points of the player."""
        self.set_full_hit_points()
        return self.full_hit_points

    def set_full_hit_points(self):
        """Calculate the full hit points of the player."""
        # nth term is (5/2)(n^2)+(5/2)n+10
        change = 10
        change_increment = 5
        total = self.initial_hit_points
        for i in range(1, self.level):
            total += change
            change += change_increment
        self.full_hit_points = total

    def backpack(self):
        """Print out the contents of the backpack."""
        if self.backpack != []:
            # Prints indexed list
            i = 1
            for item in self.backpack:
                print(str(i) + "). " + item.name)
                i += 1
            target = "not an int"
            while not type(target) is int:
                try:
                    target = int(
                        input("Please select an item (Type 0 for none)")
                    )
                except ValueError:
                    print("This input must be a number")
            chosen_item = self.backpack[target - 1]
            # Another indexed list
            print("What would you like to do with " + chosen_item + "?")
            print("You can 1). Remove or 2). Equip / Use")
            target = "not an int"
            while not type(target) is int:
                try:
                    target = int(
                        input("Please select an option (Type 0 for none")
                    )
                except ValueError:
                    print("This input must be a number")
            if target == 1:
                self.backpack.remove(chosen_item)
            if target == 2:
                if type(chosen_item) is Weapon or type(chosen_item) is Armour:
                    self.equip(chosen_item)
                else:
                    self.use(chosen_item)

    def equip(self, item):
        """Equip an item."""
        if type(item) is Weapon:
            self.weapon = item
        elif type(item) is Armour:
            # Can't wear two helmets etc.
            i = 0
            for piece in self.armour:
                if piece.place == item.place:
                    self.backpack.append(piece)
                    self.armour[i] = item
                    self.armour_protection = self.calculate_armour_protection()
                    self.backpack.remove(item)
                    break
                i += 1
        else:
            print("You can't equip this")

    def use(self, item):
        """Use an item."""
        if item.ability.type_of == "heal":
            self.hit_points += item.ability.val
        else:
            print("ERROR IN MY CODE SORRY: not aware of this ability")

    def help_me(self):
        """Get help with available inputs."""
        print(
            "Commands to choose from are: explore, go, help, status, attack, \
                run, defend, target, search, backpack and quit"
        )

    def get_status(self):
        """Output player's status."""
        print("Your status:")
        print("\nYour armour stats: ")
        for piece in self.armour:
            print(piece.to_stats() + "\n")
        print("Your weapon stats: " + self.weapon.to_stats())
        print("\nYour remaining HP: " + str(self.hit_points))
        print("\nYour level: " + str(self.level))
        print("\nYour XP: " + str(self.xp))
        print("\nYour money: $" + str(self.money))

    def quit_it(self):
        """Quit the game."""
        print("Quitting")
        quit()

    def do_command(self, s):
        """Carry out the requested command."""
        hcs = HardCodedStuff()
        if s in hcs.commands:
            hcs.commands[s]()
        else:
            print("Invalid input... Please try again")


class Enemy(Animate):
    """
    Class representing Enemy characters.

    Attributes
    ----------
    name: str
        Name of the enemy
    room: int
        Room where the enemy is
    hit_points: int
        HP of enemy
    weapon: Weapon
        The weapon of the enemy
    armour: Armour
        The armour being worn by the enemy
    money: int
        How much money the enemy has
    armour_protection: int
        How much protecion the armour of the enemy adds
    dead: bool
        Is the enemy dead or alive
    attacking: bool
        Is the enemy in the attacking state
    defending: bool
        Is the enemy in the defending state
    target: Animate
        The target of the enemy - set to player

    Methods
    -------
    get_stats()
        Output the stats of the enemy.
    ran_on()
        Be run from by player.
    die()
        Die.
    decide_next_move()
        Decide the next move.
    """

    def __init__(self, name, room, weapon, armour, hit_points, player, money):
        """Initialise the enemy."""
        super().__init__(name, room, hit_points, weapon, armour, money)
        self.target = player

    def get_stats(self):
        """Output the stats of the enemy."""
        return self.name + ": Health: " + str(self.hit_points)

    def ran_on(self):
        """Be run from by player.

        Effectively sets enemy to dead, as Player will not have to fight
        them again
        """
        self.target.hits = 0
        self.dead = True

    def die(self):
        """Die."""
        print(self.name + " is dead... Well done!")
        self.target.increment_xp()
        self.target.hits = 0
        # You gain your enemies' money
        self.target.money += self.money
        print("Player now has $" + str(self.target.money))
        self.dead = True

    def decide_next_move(self):
        """
        Decide the next move.

        Can only run with probability 1%
        Has a 29% chance of defending, and 70% of attacking
        """
        luck = random.randint(1, 100)
        if luck % 88 == 0:
            self.run()
        else:
            if luck > 70:
                self.defend()
            else:
                self.attack()

    def run(self):
        """Run from player with probability 50%."""
        print(self.name + " attempts to run from " + self.target.name)
        luck = random.randint(1, 100)
        if luck % 2 == 0:
            print(self.name + " has escaped successfully!")
            self.defending = False
            self.attacking = False
            self.target.attacking = False
        else:
            print(self.name + "'s escape attempt failed")


class NPC(Animate):
    """
    NPC Character.

    Attributes
    ----------
    name: str
        Name of the NPC
    room: int
        Room of the NPC
    lines: list
        List of the lines of the NPC

    Methods
    -------
    do_dialogue:
        Print your dialogue to the player
    """

    def __init__(self, name, room, lines):
        """Initialise NPC."""
        self.name = name
        self.room = room
        self.lines = lines

    def do_dialogue(self):
        """Print your dialogue to the player."""
        for line in self.lines:
            print(line)
            time.sleep(len(line.split(" ")) // 4 + 1)
