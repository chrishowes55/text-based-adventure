"""File containing all the Inanimate objects."""


class Inanimate:
    """
    Class representing Inanimate objects.

    Attributes
    ---------
    name: str
        Name of inanimate
    location: int
        Index of current room of inanimate
    """

    def __init__(self, name, location):
        """Initialise the object."""
        self.name = name
        self.location = location


class Armour(Inanimate):
    """
    Class represents pieces of armour.

    Attributes
    ----------
    name: str
        Name of weapon
    location: int
        Index of current room of armour
    val: int
        How much the armour will decrease damage taken
    place: int
        Section of the room where the armour can be found

    Methods
    -------
    to_stats()
        Output the stats of the armour
    """

    def __init__(self, val, name, location, place):
        """Initialise the armour."""
        super().__init__(name, location)
        self.val = val
        self.place = place

    def to_stats(self):
        """Output the stats of the armour."""
        return self.name + ": Armour Points: " + str(self.val)


class Weapon(Inanimate):
    """
    Class to represent Weapons.

    Attributes
    ----------
    name: str
        Name of weapon
    location: int
        Index of current room of weapon
    damage: int
        How much damage the weapon can cause

    Methods
    -------
    to_stats()
        Output the stats of the weapon
    """

    def __init__(self, name, damage, location):
        """Initialise the weapon."""
        super().__init__(name, location)
        self.damage = damage

    def to_stats(self):
        """Output the stats of the weapon."""
        return self.name + ": Damage Given: " + str(self.damage)


class Item(Inanimate):
    """
    Class to represent an item.

    Attributes
    ----------
    name: str
        Name of item
    location: int
        Index of current room of item
    ability: Ability
        Ability of item
    """

    def __init__(self, name, ability, location):
        """Initialise the item."""
        super().__init__(name, location)
        self.ability = ability


class Shop:
    """
    Class to represent a shop.

    MAY NEED RETHINKINg

    Attributes
    ----------
    price: int
        Price of item
    """

    def __init__(self, price):
        """Initialise Shop."""
        self.price = price


class ShopItem(Item, Shop):
    """
    Class to represent an item in a shop.

    Attributes
    ----------
    name: str
        Name of item
    location: int
        Index of current room of item
    ability: Ability
        Ability of item
    price: int
        Price of item
    """

    def __init__(self, name, ability, location, price):
        """Initialize the ShopItem."""
        Item.__init__(self, name, ability, location)
        Shop.__init__(self, price)


class ShopWeapon(Weapon, Shop):
    """
    Class to represent a weapon in a shop.

    Attributes
    ----------
    name: str
        Name of weapon
    location: int
        Index of current room of weapon
    damage: int
        Damage the weapon can deal
    price: int
        Price of item
    """

    def __init__(self, name, damage, location, price):
        """Initialize the ShopWeapon."""
        Weapon.__init__(self, name, damage, location)
        Shop.__init__(self, price)


class ShopArmour(Weapon, Shop):
    """
    Class to represent an item in a shop.

    Attributes
    ----------
    name: str
        Name of armour
    location: int
        Index of current room of armour
    val: int
        How much the armour will decrease damage taken
    place: int
        Section of the room where the armour can be found
    price: int
        Price of armou
    """

    def __init__(self, val, name, location, place, price):
        """Initialize the ShopArmour."""
        Weapon.__init__(self, val, name, location, place)
        Shop.__init__(self, price)


class Ability:
    """
    Class to represent an ability.

    Attributes
    ----------
    type_of: str
        The type of ability
    val: int
        How powerful the ability is
    """

    def __init__(self, type_of, val):
        """Initialize the Ability."""
        self.type_of = type_of
        self.val = val
