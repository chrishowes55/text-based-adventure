from Animates import Player
from Miscellaneous import HardCodedStuff
    
player = Player(input("Hello Player! What's your name?\n>>>"))
print("Hello there " + player.getName())
hcs = HardCodedStuff(player)
print("For a tutorial and list of buildings/areas, please see the README at: https://github.com/chrishowes55/text-based-adventure")
playing = True
while playing:
    s = input(">>>").lower()
    player.doCommand(s, hcs)
