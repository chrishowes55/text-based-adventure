"""File containing all place-related classes."""
import time


class Place:
    """
    Class to represent a place.

    Attributes
    ----------
    name: str
        The name of the place
    """

    def __init__(self, name):
        """Initialize the place."""
        self.name = name


class MiiRecoverii(Place):
    """
    Class to represent MiiRecoverii - a place to heal.

    Attributes
    ----------
    name: str
        Name of the MiiRecoverii

    Methods
    -------
    on_visit(player: Player)
        Do the correct output when player visits
    """

    def __init__(self, name):
        """Initialize the MiiRecoverii."""
        super().__init__(name)

    def on_visit(self, player):
        """Do the correct output when player visits."""
        # Loop so we can deal with bad typers
        while True:
            heal = input(
                "Welcome to MiiRecoverii! Would you like to be healed? (Y/N)"
            ).upper()
            if heal == "Y":
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1...Aaaaand voila! You have been healed")
                player.hit_points = player.full_hit_points
                print("Your health is now " + str(player.full_hit_points))
                break
            elif heal == "N":
                print("See you soon then!")
                break
            else:
                print("I'm sorry... I don't understand you...")


class MiiBuyy(Place):
    """
    Class to represent MiiBuyy - a place to shop.

    Attributes
    ----------
    name: str
        Name of the MiiBuyy
    items: list
        A list of the items in the shop
    weapons: list
        A list of the weapons in the shop
    armour: list
        A list of the armour in the shop

    Methods
    -------
    on_visit(player: Player)
        Do the correct output when player visits
    """

    def __init__(self, name, items, weapons, armour):
        """Initialize the MiiBuyy."""
        super().__init__(name)
        self.items = items
        self.weapons = weapons
        self.armour = armour

    def on_visit(self, player):
        """Do the correct output when player visits."""
        # Loop for bad typers
        choosing = True
        while choosing:
            choice = input(
                "Are you shopping for items, weapons or armour?"
            ).lower()
            if choice == "items":
                chosen = self.items
                choosing = False
            elif choice == "weapons":
                chosen = self.weapons
                choosing = False
            elif choice == "armour":
                chosen = self.armour
                choosing = False

        if chosen != []:
            # Print indexed list
            print("Choose an item to buy!")
            i = 1
            for thing in chosen:
                print(
                    str(i)
                    + "). "
                    + thing.name
                    + ", Price: "
                    + str(thing.price)
                )
                i += 1
            target = "not an int"
            while not type(target) is int:
                try:
                    target = int(
                        input(
                            "Which would you like to buy? "
                            + "(Type 0 for none)"
                        )
                    )
                except ValueError:
                    print("This input needs to be a number")
            player.buy(chosen[target - 1])
        else:
            print("This shop stocks no " + choice)


class MiiDestroyy(Place):
    """
    Class to represent MiiDestroyy - a place to fight.

    Attributes
    ----------
    name: str
        Name of the MiiDestroyy
    items: list
        A list of the enemies in the MiiDestroyy
    money: int
        The reward for killing all of the enemies

    Methods
    -------
    on_visit(player: Player)
        Do the correct output when player visits
    """

    def __init__(self, name, enemies, money):
        """Initialize the MiiDestroyy."""
        super().__init__(name)
        self.enemies = enemies
        self.money = money

    def on_visit(self, player, hcs):
        """Do the correct output when player visits."""
        total = 0
        for enemy in self.enemies:
            print("Your target is now: " + enemy.name)
            player.target = enemy
            while True:
                s = input(">>>").lower()
                player.do_command(s, hcs)
                if not player.attacking:
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
            player.money += self.money
        else:
            print("Good effort... Goodbye for now!")
