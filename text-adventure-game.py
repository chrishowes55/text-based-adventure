from Animates import Player
from Miscellaneous import HardCodedStuff
    
player = Player(input("Hello Player! What's your name?\n>>>"))
print("Hello there " + player.getName())
hcs = HardCodedStuff(player)
playing = True
while playing:
    s = input(">>>").lower()
    player.doCommand(s, hcs)
