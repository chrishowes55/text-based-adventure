"""File running the main game loop."""
from Animates import Player
from Miscellaneous import HardCodedStuff

player = Player(input("Hello Player! What's your name?\n>>>"))
print("Hello there " + player.name)
hcs = HardCodedStuff(player)
print(
    "For a tutorial and list of buildings/areas, please see the README at: \
        https://github.com/chrishowes55/text-based-adventure"
)
print(
    "The Mii Plaza has been overrun by the Evil MICHAnEL, and it is your job \
        to stop him. Find your way east to Master Ozana, he will tell you \
            where to go next."
)
playing = True
while playing:
    s = input(">>>").lower()
    player.doCommand(s, hcs)
